"""Merge LoRA weights and export to GGUF for phone deployment.

Produces a Q4_K_M quantized GGUF file (~350 MB) suitable for
llama.cpp / MLC LLM on Android & iOS.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import OUTPUT_DIR, MAX_SEQ_LENGTH
from unsloth import FastLanguageModel


def main():
    lora_path = str(OUTPUT_DIR / "lora")
    gguf_dir = str(OUTPUT_DIR / "gguf")

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

    print(f"\nGGUF exported → {gguf_dir}/")
    print("Deploy this file with llama.cpp or MLC LLM on Android/iOS.")


if __name__ == "__main__":
    main()
