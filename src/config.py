from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
# data/gold, data/distilled — see data/README.md for what lives where and how
# each file is regenerated. data/train.jsonl (the combined set train.py reads)
# stays at the DATA_DIR root since it's the one file every pipeline user needs.
DATA_GOLD_DIR = DATA_DIR / "gold"
DATA_DISTILLED_DIR = DATA_DIR / "distilled"

OUTPUT_DIR = PROJECT_ROOT / "outputs"
# Each train.py run gets its own outputs/runs/<run_id>/ — checkpoints, the final
# LoRA adapter, the exact config used, and a metrics log all live together, so
# nothing from one run collides with or gets overwritten by the next. See
# `RUNS_DIR` / `LATEST_FILE` usage in train.py, export.py, evaluate.py.
RUNS_DIR = OUTPUT_DIR / "runs"
LATEST_FILE = OUTPUT_DIR / "latest.txt"

# Teacher model (pulled via: ollama pull qwen3:8b)
TEACHER_MODEL = "qwen3:8b"

# Student model
STUDENT_MODEL = "unsloth/Qwen3-0.6B"
# Measured over the current corpus: median 762 tokens, p99 1211, max 1558.
# 2048 wasted memory on padding no example needs; activation memory scales with
# this, which matters on a 4GB card. Raise it if the corpus ever grows longer —
# `evaluate.py` and the p99 above are how you check.
MAX_SEQ_LENGTH = 1600
LORA_R = 16
LORA_ALPHA = 16
LORA_DROPOUT = 0

# Training
BATCH_SIZE = 2
GRAD_ACCUM_STEPS = 4
EPOCHS = 3
LEARNING_RATE = 2e-4

# Data generation
PLAN_EXAMPLES_TARGET = 500
SCHEDULE_EXAMPLES_TARGET = 300
