# the-koorm-tasks

Fine-tune Qwen3-0.6B for on-device task planning and schedule adjustment, distilled from Qwen3-8B.

**Trained model:** [huggingface.co/sumitsrv/qwen3-0.6b-task-planner](https://huggingface.co/sumitsrv/qwen3-0.6b-task-planner)

Part of the **Koorm** project — a productivity app for people who struggle with perfectionism and overwhelm. The model turns a natural-language task into a structured, "good enough" plan, and slots new tasks into an existing daily schedule without breaking its constraints.

## Trained model

The fine-tuned model lives on the Hugging Face Hub, not in this repo (see [Model weights & GitHub](#model-weights--github) below):

| Artifact | Location in the HF repo | Use |
|----------|------------------------|-----|
| LoRA adapter | repo root (`adapter_model.safetensors`, …) | apply on top of `unsloth/Qwen3-0.6B` |
| GGUF (Q4_K_M, ~378 MB) | `gguf/qwen3-0.6b.Q4_K_M.gguf` | llama.cpp / MLC LLM / Ollama |
| Ollama `Modelfile` | `gguf/Modelfile` | `ollama create` |

### Download it

```bash
# whole repo
hf download sumitsrv/qwen3-0.6b-task-planner --local-dir model/

# just the GGUF + Modelfile
hf download sumitsrv/qwen3-0.6b-task-planner gguf/qwen3-0.6b.Q4_K_M.gguf gguf/Modelfile --local-dir model/
```

### Run it with Ollama

```bash
cd model/gguf
ollama create koorm-planner -f Modelfile
ollama run koorm-planner
```

### Use the adapter with Transformers / PEFT

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = AutoModelForCausalLM.from_pretrained("unsloth/Qwen3-0.6B")
model = PeftModel.from_pretrained(base, "sumitsrv/qwen3-0.6b-task-planner")
tok = AutoTokenizer.from_pretrained("sumitsrv/qwen3-0.6b-task-planner")
```

The model outputs **JSON only** (no reasoning trace). Recommended sampling: `temperature=0.6, top_p=0.95, top_k=20`. See `src/prompts.py` for the exact system prompts and the `PlanResponse` / `ScheduleResponse` schemas in `src/schema.py`.

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

Uses the local Qwen3-8B teacher (via Ollama) to distill training data for:
- **Task planning** — breaking down natural-language tasks into structured plans with priority, category, subtasks, and "good enough" criteria
- **Schedule adjustment** — fitting new tasks into an existing daily schedule while respecting constraints (meetings, lunch, buffers, no work past 17:00)

Each example stores the teacher's **final validated JSON only** — the `<think>` reasoning trace is discarded so the 0.6B student learns to emit compact, valid JSON directly (faster on-device, and no truncation at `MAX_SEQ_LENGTH`). Every example passes two gates:
1. **Schema validation** (`PlanResponse` / `ScheduleResponse`) — structural correctness
2. **Semantic filters** (`valid_plan` / `valid_schedule`) — subtask minutes roughly sum to the estimate, schedules have no overlaps, nothing runs past 17:00, deferred tasks are actually removed. Teacher outputs that fail are dropped.

Outputs:
- `data/descriptions.json` — expanded task descriptions (cached; tops up toward the target on re-run)
- `data/plan_train.jsonl` — task planning examples
- `data/schedule_train.jsonl` — schedule adjustment examples
- `data/train.jsonl` — combined, shuffled training set

**Resumable:** If interrupted, re-run the same command and it picks up where it left off. Run only **one** instance at a time — two processes hitting the same Ollama model serialize and duplicate rows.

Targets (configurable in `src/config.py`): 500 plan examples + 300 schedule examples (~a few hours on an RTX 4060).

### Step 2: Fine-tune the student model

```bash
python src/train.py
```

QLoRA fine-tunes Qwen3-0.6B on the distilled data using Unsloth.

- Base model: `unsloth/Qwen3-0.6B` (4-bit quantized)
- LoRA: r=16, alpha=16, targeting all attention + MLP projections
- Training: 3 epochs, lr=2e-4, batch=2, grad_accum=4, bf16 on Ada
- 90/10 train/eval split with periodic eval loss (catches overfitting on the limited schedule variety)
- VRAM usage: ~2-3 GB

Output: `outputs/lora/` — LoRA adapter weights.

### Step 3: Export to GGUF for phone deployment

```bash
python src/export.py
```

Merges LoRA weights into the base model and exports as GGUF Q4_K_M (~378 MB).

Output: `outputs/gguf_gguf/qwen3-0.6b.Q4_K_M.gguf` (+ `Modelfile`) — deploy with llama.cpp / MLC LLM on Android & iOS, or Ollama.

## Configuration

All hyperparameters and paths are in `src/config.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TEACHER_MODEL` | `qwen3:8b` | Ollama model for data generation |
| `STUDENT_MODEL` | `unsloth/Qwen3-0.6B` | HuggingFace model for fine-tuning |
| `MAX_SEQ_LENGTH` | 2048 | Max training sequence length |
| `PLAN_EXAMPLES_TARGET` | 500 | Number of task-plan training examples |
| `SCHEDULE_EXAMPLES_TARGET` | 300 | Number of schedule-adjustment examples |
| `LORA_R` | 16 | LoRA rank |
| `EPOCHS` | 3 | Training epochs |
| `LEARNING_RATE` | 2e-4 | Learning rate |

## Project structure

```
src/
├── config.py         # Paths, model names, hyperparameters
├── schema.py         # Pydantic models (mirrors Koorm project's Kotlin types)
├── prompts.py        # System prompts and prompt builders
├── scenarios.py      # Seed task descriptions + random schedule generator
├── generate.py       # Step 1: teacher distillation + quality filters via Ollama
├── train.py          # Step 2: QLoRA fine-tuning via Unsloth
├── export.py         # Step 3: GGUF export for phone deployment
└── test_filters.py   # Self-check for the data-quality filters
```

## Model weights & GitHub

The trained weights are **not committed to this repo**. GitHub rejects any single file over 100 MB, and the GGUF is ~378 MB — so the model's home is the [Hugging Face repo](https://huggingface.co/sumitsrv/qwen3-0.6b-task-planner), and `.gitignore` keeps `outputs/` (and the `.venv`, caches) out of git. Fetch the weights with the `hf download` commands above.

If you specifically want the binaries versioned inside this git repo, that requires [Git LFS](https://git-lfs.com) — note the free GitHub LFS tier is 1 GB storage / 1 GB bandwidth per month, which a 378 MB file exhausts in a couple of clones.

## License

The fine-tune inherits the [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) base-model license (Apache-2.0).
