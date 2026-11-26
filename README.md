# cs-178-TacoTeam

CS 178 class project on the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset.

## Setup

```bash
git clone <repo-url>
cd cs-178-TacoTeam

uv sync --extra dev           # creates .venv and installs everything

# activate the venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

nbstripout --install          # strips notebook outputs on commit
nbdime config-git --enable    # readable notebook diffs/merges
```

Don't have uv? Install it from https://docs.astral.sh/uv/getting-started/installation/. In VS Code, pick `.venv` as your Python interpreter / notebook kernel.

**Then put the dataset files in `data/`** (they are not tracked by git). Download the [CIFAR-10 python version](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) and extract it so you have `data/cifar-10-batches-py/` containing `data_batch_1` … `data_batch_5` and `test_batch`. Load it with:

```python
from mlproj.data import load_cifar10
Xtr, ytr, Xte, yte = load_cifar10()  # (50000, 3072) (50000,) (10000, 3072) (10000,)
```

## Folder layout

| Folder | What goes there |
|---|---|
| `data/` | Raw/processed dataset files. Git-ignored — share data outside git. |
| `notebooks/<name>/` | Your own Jupyter notebooks — one folder per person. |
| `src/mlproj/` | Shared Python code (loading, preprocessing, evaluation helpers). Import with `from mlproj import ...`. |
| `results/` | Metrics saved as CSV files. |
| `figures/` | Plots saved as PNG/PDF. |

## Team rules

1. **Only work in your own `notebooks/<name>/` folder. Don't edit or run-and-save other people's notebooks** — copy one into your folder if you want to build on it.
2. **Shared code goes in `src/mlproj/`**, not copy-pasted between notebooks.
3. **Don't commit data** (or model `.pkl` files).
4. **Save metrics to `results/` as CSV and plots to `figures/`** so everyone can compare runs.
5. **Use branches + PRs.** Don't push directly to `main`; get a teammate to review before merging.
