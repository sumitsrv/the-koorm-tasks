"""Fine-tune Qwen3-0.6B on distilled training data using Unsloth + QLoRA.

Requirements:
  pip install unsloth    # pulls torch, transformers, peft, bitsandbytes, trl
  Python 3.10-3.12 recommended (3.13 may not be supported by PyTorch/Unsloth)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import (
    DATA_DIR, OUTPUT_DIR,
    STUDENT_MODEL, MAX_SEQ_LENGTH,
    LORA_R, LORA_ALPHA, LORA_DROPOUT,
    BATCH_SIZE, GRAD_ACCUM_STEPS, EPOCHS, LEARNING_RATE,
)

from unsloth import FastLanguageModel, is_bfloat16_supported
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig


def main():
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
    data_path = str(DATA_DIR / "train.jsonl")
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
    output = str(OUTPUT_DIR)
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        args=SFTConfig(
            per_device_train_batch_size=BATCH_SIZE,
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
            output_dir=output,
            dataset_text_field="text",
            max_seq_length=MAX_SEQ_LENGTH,
            seed=42,
        ),
    )

    print("Training …")
    trainer.train()

    # ── 5. Save LoRA adapter ────────────────────────────────────────────
    lora_path = str(OUTPUT_DIR / "lora")
    model.save_pretrained(lora_path)
    tokenizer.save_pretrained(lora_path)
    print(f"\nLoRA adapter saved → {lora_path}")
    print("Next step: python src/export.py")


if __name__ == "__main__":
    main()
