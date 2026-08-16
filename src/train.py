"""Fine-tune Qwen3-0.6B on distilled training data using Unsloth + QLoRA.

Requirements:
  pip install unsloth    # pulls torch, transformers, peft, bitsandbytes, trl
  Python 3.10-3.12 recommended (3.13 may not be supported by PyTorch/Unsloth)
"""

import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import (
    DATA_DIR, LATEST_FILE, RUNS_DIR,
    STUDENT_MODEL, MAX_SEQ_LENGTH,
    LORA_R, LORA_ALPHA, LORA_DROPOUT,
    BATCH_SIZE, GRAD_ACCUM_STEPS, EPOCHS, LEARNING_RATE,
)

from unsloth import FastLanguageModel, is_bfloat16_supported
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig


def git_commit() -> str | None:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=Path(__file__).parent, capture_output=True, text=True, timeout=5,
        ).stdout.strip() or None
    except Exception:  # noqa: BLE001 — best-effort provenance, never fatal
        return None


def main():
    # ── 0. Set up a run directory ─────────────────────────────────────────
    # Every run gets its own outputs/runs/<run_id>/, so checkpoints, the final
    # adapter and this run's config/metrics never collide with another run's.
    run_id = time.strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    data_path = str(DATA_DIR / "train.jsonl")
    with open(data_path, encoding="utf-8") as f:
        n_examples = sum(1 for line in f if line.strip())

    hyperparams = {
        "run_id": run_id,
        "git_commit": git_commit(),
        "student_model": STUDENT_MODEL,
        "max_seq_length": MAX_SEQ_LENGTH,
        "lora_r": LORA_R,
        "lora_alpha": LORA_ALPHA,
        "lora_dropout": LORA_DROPOUT,
        "batch_size": BATCH_SIZE,
        "grad_accum_steps": GRAD_ACCUM_STEPS,
        "epochs": EPOCHS,
        "learning_rate": LEARNING_RATE,
        "train_data": data_path,
        "train_data_examples": n_examples,
    }
    (run_dir / "config.json").write_text(json.dumps(hyperparams, indent=2), encoding="utf-8")
    print(f"Run {run_id} → {run_dir}")

    # ── 1. Load base model (4-bit quantized) ─────────────────────────────
    print(f"Loading {STUDENT_MODEL} …")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=STUDENT_MODEL,
        max_seq_length=MAX_SEQ_LENGTH,
        load_in_4bit=True,
    )

    # ── 2. Attach LoRA adapters ──────────────────────────────────────────
    model = FastLanguageModel.get_peft_model(
        model,
        r=LORA_R,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        use_gradient_checkpointing="unsloth",
    )

    # ── 3. Load & format dataset ─────────────────────────────────────────
    print(f"Loading dataset from {data_path} …")
    dataset = load_dataset("json", data_files=data_path, split="train")

    def apply_template(example):
        text = tokenizer.apply_chat_template(
            example["messages"],
            tokenize=False,
            add_generation_prompt=False,
        )
        return {"text": text}

    dataset = dataset.map(apply_template, remove_columns=dataset.column_names)
    split = dataset.train_test_split(test_size=0.1, seed=42)
    train_ds, eval_ds = split["train"], split["test"]
    print(f"Training on {len(train_ds)} examples, evaluating on {len(eval_ds)}")

    # ── 4. Train ─────────────────────────────────────────────────────────
    # Checkpoints land inside run_dir (via output_dir below), not shared across
    # runs — a second run can't stomp on a first run's checkpoint-N.
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        args=SFTConfig(
            per_device_train_batch_size=BATCH_SIZE,
            # HF defaults eval batch to 8 regardless of the train batch, so on a
            # small card evaluation OOMs while training itself fits — the crash
            # lands in accelerate's _convert_to_fp32, upcasting gathered logits.
            per_device_eval_batch_size=1,
            # We only ever report eval *loss*, so don't let the trainer gather
            # and upcast prediction logits: with a ~152k vocab that tensor is
            # gigabytes on its own, and it is pure waste here.
            prediction_loss_only=True,
            gradient_accumulation_steps=GRAD_ACCUM_STEPS,
            num_train_epochs=EPOCHS,
            learning_rate=LEARNING_RATE,
            bf16=is_bfloat16_supported(),       # Ada (RTX 4060) supports bf16 — more stable than fp16
            fp16=not is_bfloat16_supported(),
            logging_steps=10,
            eval_strategy="steps",
            eval_steps=20,
            save_steps=100,
            save_total_limit=2,
            output_dir=str(run_dir),
            dataset_text_field="text",
            max_seq_length=MAX_SEQ_LENGTH,
            seed=42,
        ),
    )

    print("Training …")
    trainer.train()

    # ── 5. Log metrics ───────────────────────────────────────────────────
    # trainer.state.log_history already has every logged/eval step; write it
    # out flat so a run's loss curve survives without re-parsing trainer_state
    # out of whichever checkpoint directory happened to be saved last.
    metrics_path = run_dir / "metrics.jsonl"
    with metrics_path.open("w", encoding="utf-8") as f:
        for entry in trainer.state.log_history:
            f.write(json.dumps(entry) + "\n")

    # ── 6. Save LoRA adapter ────────────────────────────────────────────
    lora_path = str(run_dir / "lora")
    model.save_pretrained(lora_path)
    tokenizer.save_pretrained(lora_path)
    print(f"\nLoRA adapter saved → {lora_path}")

    LATEST_FILE.write_text(run_id, encoding="utf-8")
    print(f"Run metrics → {metrics_path}")
    print(f"Marked {run_id} as latest ({LATEST_FILE})")
    print("Next step: python src/export.py")


if __name__ == "__main__":
    main()
