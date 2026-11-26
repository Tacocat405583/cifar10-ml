# cifar10-ml

CS 178 class project on the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset.

## Setup

```bash
git clone https://github.com/Tacocat405583/cifar10-ml.git
cd cifar10-ml
```

Then install with **either** uv or pip:

**Option A: uv** ([install uv](https://docs.astral.sh/uv/getting-started/installation/))

```bash
uv sync --extra dev           # creates .venv and installs everything
```

**Option B: pip**

```bash
python -m venv .venv
# (activate it, see below)
pip install -e ".[dev]"
```

Activate the venv (both options):

```bash
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

Finally, set up the notebook git tools (one time):

```bash
nbstripout --install          # strips notebook outputs on commit
nbdime config-git --enable    # readable notebook diffs/merges
```

In VS Code, pick `.venv` as your Python interpreter / notebook kernel.

**Then put the dataset files in `data/`** (they are not tracked by git). Download the [CIFAR-10 python version](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) and extract it so you have `data/cifar-10-batches-py/` containing `data_batch_1` … `data_batch_5` and `test_batch`. Load it with:

```python
from mlproj.data import load_cifar10
Xtr, ytr, Xte, yte = load_cifar10()  # (50000, 3072) (50000,) (10000, 3072) (10000,)
```

## Folder layout

| Folder | What goes there |
|---|---|
| `data/` | Raw/processed dataset files. Git-ignored — share data outside git. |
| `notebooks/<name>/` | Jupyter notebooks, one folder per person. |
| `src/mlproj/` | Shared Python code (loading, preprocessing, evaluation helpers). Import with `from mlproj import ...`. |
| `results/` | Metrics saved as CSV files. |
| `figures/` | Plots saved as PNG/PDF. |

## Guidelines

1. **One folder per person for notebooks** (`notebooks/<name>/`).
2. **Shared code goes in `src/mlproj/`**, not copy-pasted between notebooks.
3. **Keep shared code backwards compatible.** Add new scripts/functions instead of modifying existing ones, so you don't break other people's notebooks.
4. **Don't commit data** (or model `.pkl` files).
5. **Save metrics to `results/` as CSV and plots to `figures/`** so everyone can compare runs.
6. **Use branches + PRs.** Don't push directly to `main`; open a PR and I'll merge PRs at the end of each day.
