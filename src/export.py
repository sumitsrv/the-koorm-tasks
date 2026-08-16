"""Merge LoRA weights and export to GGUF for phone deployment.

Produces a Q4_K_M quantized GGUF file (~350 MB) suitable for
llama.cpp / MLC LLM on Android & iOS.

Exports the LoRA from the latest training run (outputs/latest.txt, written by
train.py) unless --run names a specific outputs/runs/<run_id>/ directory.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import LATEST_FILE, MAX_SEQ_LENGTH, RUNS_DIR
from unsloth import FastLanguageModel


def resolve_run(run_id: str | None) -> Path:
    if run_id is None:
        if not LATEST_FILE.exists():
            raise SystemExit(f"no {LATEST_FILE} — run train.py first, or pass --run <run_id>")
        run_id = LATEST_FILE.read_text(encoding="utf-8").strip()
    run_dir = RUNS_DIR / run_id
    if not (run_dir / "lora").exists():
        raise SystemExit(f"no LoRA adapter at {run_dir / 'lora'}")
    return run_dir


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", help="run_id under outputs/runs/ (default: outputs/latest.txt)")
    args = ap.parse_args()

    run_dir = resolve_run(args.run)
    lora_path = str(run_dir / "lora")
    gguf_dir = str(run_dir / "gguf")

    print(f"Loading LoRA adapter from {lora_path} …")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=lora_path,
        max_seq_length=MAX_SEQ_LENGTH,
        load_in_4bit=True,
    )

    print("Merging LoRA and exporting to GGUF (q4_k_m) …")
    model.save_pretrained_gguf(
        gguf_dir,
        tokenizer,
        quantization_method="q4_k_m",
    )

    # Unsloth writes the merged fp16 model to gguf_dir itself and the quantized
    # .gguf + Modelfile to a sibling "<gguf_dir>_gguf" directory.
    print(f"\nGGUF exported → {gguf_dir}_gguf/")
    print("Deploy this file with llama.cpp or MLC LLM on Android/iOS.")


if __name__ == "__main__":
    main()
