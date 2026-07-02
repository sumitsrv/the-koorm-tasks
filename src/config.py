from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Teacher model (pulled via: ollama pull qwen3:8b)
TEACHER_MODEL = "qwen3:8b"

# Student model
STUDENT_MODEL = "unsloth/Qwen3-0.6B"
MAX_SEQ_LENGTH = 2048
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
