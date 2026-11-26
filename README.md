# cs-178-TacoTeam

CS 178 class project: applying classical ML models (numpy, pandas, scikit-learn, matplotlib — **no PyTorch**) to the `<DATASET NAME>` dataset.

## Setup

```bash
git clone <repo-url>
cd cs-178-TacoTeam

python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -e ".[dev]"
nbstripout --install          # strips notebook outputs on commit
nbdime config-git --enable    # readable notebook diffs/merges
```

Then put the dataset files in `data/` (they are not tracked by git).

## Folder layout

| Folder | What goes there |
|---|---|
| `data/` | Raw/processed dataset files. Git-ignored — share data outside git. |
| `notebooks/` | Jupyter notebooks, one per person/experiment. |
| `src/mlproj/` | Shared Python code (loading, preprocessing, evaluation helpers). Import with `from mlproj import ...`. |
| `results/` | Metrics saved as CSV files. |
| `figures/` | Plots saved as PNG/PDF. |

## Team rules

1. **One notebook per person/experiment**, named `<name>_<experiment>.ipynb` (e.g. `nick_rf.ipynb`). Don't edit someone else's notebook.
2. **Shared code goes in `src/mlproj/`**, not copy-pasted between notebooks.
3. **Don't commit data** (or model `.pkl` files).
4. **Save metrics to `results/` as CSV and plots to `figures/`** so everyone can compare runs.
5. **Use branches + PRs.** Don't push directly to `main`; get a teammate to review before merging.
