# the-koorm-tasks

Fine-tune Qwen3-0.6B for on-device task planning and schedule adjustment, distilled from Qwen3-8B.

## Prerequisites

- Python 3.12 (3.13 not supported by Unsloth/PyTorch)
- NVIDIA GPU with CUDA (tested on RTX 4060 Laptop, 8GB VRAM)
- [Ollama](https://ollama.com) installed and running

## Setup

```bash
# Create Python 3.12 venv
py -3.12 -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Install PyTorch with CUDA first
pip install torch==2.10.0 torchvision==0.25.0 torchaudio==2.10.0 --index-url https://download.pytorch.org/whl/cu126

# Install Unsloth (pulls transformers, peft, trl, etc.)
pip install unsloth==2026.6.9

# Force-reinstall CUDA torch (Unsloth may overwrite with CPU-only)
pip install --force-reinstall torch==2.10.0 torchvision==0.25.0 --index-url https://download.pytorch.org/whl/cu126 --no-deps

# Install remaining deps
pip install ollama==0.6.2 pydantic==2.13.4 tqdm==4.68.3 datasets==4.3.0

# Pull the teacher model
ollama pull qwen3:8b
```

## Pipeline

### Step 1: Generate training data

```bash
python src/generate.py
```

Uses the local Qwen3-8B teacher (via Ollama) to generate chain-of-thought reasoning traces for:
- **Task planning** — breaking down natural-language tasks into structured plans with priority, category, subtasks, and "good enough" criteria
- **Schedule adjustment** — fitting new tasks into an existing daily schedule while respecting constraints (meetings, lunch, buffers)

Outputs:
- `data/descriptions.json` — expanded task descriptions (cached, stable across runs)
- `data/plan_train.jsonl` — task planning examples
- `data/schedule_train.jsonl` — schedule adjustment examples
- `data/train.jsonl` — combined, shuffled training set

**Resumable:** If interrupted, re-run the same command and it picks up where it left off.

Targets (configurable in `src/config.py`):
- 500 plan examples + 300 schedule examples
- ~50s per example → ~6 hours total on RTX 4060

### Step 2: Fine-tune the student model

```bash
python src/train.py
```

QLoRA fine-tunes Qwen3-0.6B on the distilled training data using Unsloth.

- Base model: `unsloth/Qwen3-0.6B` (4-bit quantized)
- LoRA: r=16, alpha=16, targeting all attention + MLP projections
- Training: 3 epochs, lr=2e-4, batch=2, grad_accum=4
- VRAM usage: ~2-3 GB

Outputs:
- `outputs/lora/` — LoRA adapter weights

### Step 3: Export to GGUF for phone deployment

```bash
python src/export.py
```

Merges LoRA weights into the base model and exports as GGUF Q4_K_M (~350 MB).

Output:
- `outputs/gguf/` — GGUF file for llama.cpp / MLC LLM on Android & iOS

## Configuration

All hyperparameters and paths are in `src/config.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TEACHER_MODEL` | `qwen3:8b` | Ollama model for data generation |
| `STUDENT_MODEL` | `unsloth/Qwen3-0.6B` | HuggingFace model for fine-tuning |
| `PLAN_EXAMPLES_TARGET` | 500 | Number of task-plan training examples |
| `SCHEDULE_EXAMPLES_TARGET` | 300 | Number of schedule-adjustment examples |
| `LORA_R` | 16 | LoRA rank |
| `EPOCHS` | 3 | Training epochs |
| `LEARNING_RATE` | 2e-4 | Learning rate |

## Project structure

```
src/
├── config.py       # Paths, model names, hyperparameters
├── schema.py       # Pydantic models (mirrors Koorm project's Kotlin types)
├── prompts.py      # System prompts and prompt builders
├── scenarios.py    # Seed task descriptions + random schedule generator
├── generate.py     # Step 1: teacher distillation via Ollama
├── train.py        # Step 2: QLoRA fine-tuning via Unsloth
└── export.py       # Step 3: GGUF export for phone deployment
```
