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

## Design principle: the student extracts, the app resolves

A 0.6B model is a good extractor and a poor oracle. v1 ignored that and asked it
for a `due_date` — it has no clock, so 73% of the training targets came back
dated 2023 and the shipped model answered "next Monday" with a date three years
in the past.

The schema now asks only for things the model can actually know:

| The model does | The app does |
|---|---|
| Quotes the deadline words already in the task (`due_phrase`) | Resolves them against the real clock (`DeadlineParser`) |
| Breaks the task into ordered steps | Scores priority (`PriorityAssessmentService`) |
| Names a category and a stopping point | Supplies facts as context — today's date, calendar, open tasks |

`quality.check_due_phrase` enforces the first row mechanically: a `due_phrase`
must be a **literal substring of the task text**, so an invented deadline fails
by construction. Anything else the model would have to guess is passed *in*
instead, via the optional context block on the user turn:

```python
plan_user("Book the dentist", {"today": "2026-08-15 (Saturday)"})
```

That block is where the app's own knowledge lands — including anything it
fetches over MCP or its existing connectors (calendar availability, the user's
open tasks, email context). The 0.6B student never calls a tool itself; the app
resolves the facts and hands them over, which is both more reliable and cheaper
than teaching a model this size to orchestrate.

## Data quality gates

`src/quality.py` is what stands between a teacher's output and the training set,
and it is tested like code (`python src/test_filters.py`). Every gate exists
because its absence produced a measured defect in v1:

| Gate | v1 defect it prevents |
|---|---|
| `check_good_enough` | 28% of criteria demanded perfection or named a deadline |
| `check_subtasks` | 27 plans had no steps; 28 had 7-11; steps repeated verbatim |
| `check_duration` | totals contradicted their own steps ("24 minutes" for 51) |
| `check_ordering` | "File tax returns" as step 1; opening a tap without the water off |
| `check_due_phrase` | dates invented out of thin air |
| `check_invention` | a "travel agent" for a self-service booking |
| `label_distribution_report` | HIGH on 80% of rows, `LOW` on exactly one |

The gates apply identically to distilled and hand-authored data, so swapping to
a cheaper teacher lowers yield — never the floor.

## Pipeline

### Step 1: Generate training data

The teacher is chosen at runtime; **both backends are first-class**:

```bash
python src/generate.py --teacher ollama              # local qwen3:8b — free, offline
python src/generate.py --teacher claude --workers 8  # Anthropic API — needs a key
python src/generate.py --teacher claude --model claude-opus-5
```

| | `ollama` | `claude` |
|---|---|---|
| Cost | free | per-token |
| Needs | `ollama pull qwen3:8b` | `ANTHROPIC_API_KEY` or `ant auth login` |
| Offline | yes | no |
| Schema | validated after the fact | pinned server-side (structured outputs) |
| Concurrency | keep `--workers 1` | raise it |

Output is per-teacher (`data/distilled/plan_<teacher>.jsonl`), so runs accumulate side by
side rather than overwriting each other.

### Step 1b: Repair the v1 data instead of discarding it

```bash
python src/repair.py            # dry run, reports what it would change
python src/repair.py --apply    # rewrites data/distilled/plan_train.jsonl (backs up first)
```

Salvages 312 of the original 492 examples: remaps the `SOCIAL` category the app
never had, drops `due_date`, relabels priority against the stated rubric
(HIGH 80% → MEDIUM 53% / HIGH 34% / URGENT 13%), makes each total match its own
steps, and softens perfectionist criteria. What can't be fixed honestly is
dropped, with a count and a reason for each.

### Step 1c: Hand-authored gold examples

```bash
python src/gold.py              # validate all modules, write data/gold/plan_gold.jsonl
python src/gold.py --only gold_craft --check
```

237 examples across `src/gold_*.py`, covering what distillation missed: physical
procedures with real prerequisites, unglamorous admin, creative work,
caregiving, and the `LOW` priority label v1 had exactly one example of. Add a
module by dropping a new `gold_<name>.py` in `src/` that exports `GOLD`.

Whichever sources exist are merged by `python src/generate.py --combine-only`.

The distillation step itself covers:
- **Task planning** — breaking down natural-language tasks into structured plans with priority, category, subtasks, and "good enough" criteria
- **Schedule adjustment** — fitting new tasks into an existing daily schedule while respecting constraints (meetings, lunch, buffers, no work past 17:00)

Each example stores the teacher's **final validated JSON only** — the `<think>` reasoning trace is discarded so the 0.6B student learns to emit compact, valid JSON directly (faster on-device, and no truncation at `MAX_SEQ_LENGTH`). Every example passes two gates:
1. **Schema validation** (`PlanResponse` / `ScheduleResponse`) — structural correctness
2. **Semantic filters** (`valid_plan` / `valid_schedule`) — subtask minutes roughly sum to the estimate, schedules have no overlaps, nothing runs past 17:00, deferred tasks are actually removed. Teacher outputs that fail are dropped.

Outputs (see [`data/README.md`](data/README.md) for the full map):
- `data/distilled/descriptions.json` — expanded task descriptions (cached; tops up toward the target on re-run)
- `data/distilled/plan_train.jsonl` — task planning examples
- `data/distilled/schedule_train.jsonl` — schedule adjustment examples
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

Every run gets its own `outputs/runs/<run_id>/` (timestamped), so nothing from
one run overwrites another:

```
outputs/runs/<run_id>/
├── config.json         # hyperparams, git commit, data file + example count used
├── metrics.jsonl        # trainer.state.log_history — one line per logged/eval step
├── checkpoint-*/        # periodic trainer checkpoints (save_total_limit=2)
└── lora/                # final LoRA adapter — this is what export.py reads
```

`train.py` also writes `outputs/latest.txt` with the run's id, which
`export.py` reads by default. `outputs/` itself is gitignored (see
[Model weights & GitHub](#model-weights--github)) — this structure is local
bookkeeping, not something that gets committed.

### Step 3: Export to GGUF for phone deployment

```bash
python src/export.py                    # exports outputs/latest.txt's run
python src/export.py --run 20260816-143200   # or a specific run
```

Merges LoRA weights into the base model and exports as GGUF Q4_K_M (~378 MB).

Output: `outputs/runs/<run_id>/gguf_gguf/qwen3-0.6b.Q4_K_M.gguf` (+ `Modelfile`) — deploy with llama.cpp / MLC LLM on Android & iOS, or Ollama. (Unsloth writes the merged fp16 model to `gguf/` and the quantized file to the sibling `gguf_gguf/` — that suffix is Unsloth's naming, not a typo.)

### Step 4: Evaluate against the held-out set

```bash
ollama create koorm-planner -f Modelfile
python src/evaluate.py koorm-planner --baseline qwen2.5:0.5b
```

v1 had no evaluation beyond training loss, which is why its defects shipped — a
loss curve cannot show you that `priority` collapsed to HIGH, that every date is
in 2023, or that the "good enough" criterion is demanding perfection.
`src/evaluate.py` measures each of those on 20 held-out tasks (none appear in
`data/`), plus structure, latency, templating, and first-step size. Full
per-task results are written to `outputs/eval/<timestamp>.json` (override with
`--out`).

**v1 baseline, for comparison:** 20/20 parseable and schema-valid, **0/20 passing
the quality gates**; priority HIGH on 95%; category PERSONAL on 75%;
`estimated_duration` disagreeing with its own steps on 20/20; perfectionist or
deadline-bearing criteria on 10/20.

## Configuration

All hyperparameters and paths are in `src/config.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TEACHER_MODEL` | `qwen3:8b` | Default model for the `ollama` teacher (the `claude` teacher defaults to `claude-sonnet-5`; override either with `--model`) |
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
├── schema.py         # Pydantic models — MUST match the app's Kotlin types
├── prompts.py        # System prompts; SYSTEM_PLAN is shared with the app verbatim
├── quality.py        # The data-quality gates (see table above)
├── scenarios.py      # Seed tasks, diversity axes, random schedule generator
├── teacher.py        # Teacher backends: OllamaTeacher | ClaudeTeacher
├── generate.py       # Step 1:  distillation pipeline (--teacher picks the backend)
├── repair.py         # Step 1b: salvage the v1 data rather than discard it
├── goldlib.py        # Step 1c: Gold dataclass + validation
├── gold.py           #          aggregates every src/gold_*.py module
├── gold_*.py         #          hand-authored examples, one module per domain
├── train.py          # Step 2:  QLoRA fine-tuning via Unsloth
├── export.py         # Step 3:  GGUF export for phone deployment
├── evaluate.py       # Step 4:  held-out eval against a trained checkpoint
└── test_filters.py   # Self-check for the gates — run it after touching quality.py

data/                 # tracked in git — see data/README.md for what's where and how to regenerate it
├── train.jsonl        # combined training set (what train.py reads)
├── gold/               # hand-authored examples (src/gold_*.py -> gold.py)
└── distilled/           # teacher-generated + repaired v1 data

outputs/               # gitignored — local training artifacts, not committed
├── latest.txt          # run_id of the most recent train.py run
└── runs/<run_id>/       # one dir per run: config.json, metrics.jsonl, checkpoints, lora/, gguf/
```

> ⚠️ **`SYSTEM_PLAN` is a contract in three places**: what the teacher is asked
> for, what the student is trained on, and what the app sends at inference time
> (`PlannerPrompts.SYSTEM_PLAN` in the Koorm app's `TaskPlan.kt`). Measured on
> v1: given a different planning prompt the model drifts to `[STEP 1: ...]`
> pseudo-arrays; given none it answers in prose. Change it in both repos in the
> same commit, and re-run `evaluate.py`.

## Model weights & GitHub

The trained weights are **not committed to this repo**. GitHub rejects any single file over 100 MB, and the GGUF is ~378 MB — so the model's home is the [Hugging Face repo](https://huggingface.co/sumitsrv/qwen3-0.6b-task-planner), and `.gitignore` keeps `outputs/` (and the `.venv`, caches) out of git. Fetch the weights with the `hf download` commands above.

If you specifically want the binaries versioned inside this git repo, that requires [Git LFS](https://git-lfs.com) — note the free GitHub LFS tier is 1 GB storage / 1 GB bandwidth per month, which a 378 MB file exhausts in a couple of clones.

## License

The fine-tune inherits the [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) base-model license (Apache-2.0).
