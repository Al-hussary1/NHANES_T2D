# Consensus-derived cardiometabolic phenotypes and cause-specific mortality in US adults with type 2 diabetes (NHANES 1999–2018)

Code accompanying the manuscript. The analysis is organized as an ordered set
of Jupyter notebooks that reproduce the full pipeline: cohort derivation from
public NHANES files, consensus clustering into metabolic phenotypes
(SIDD / MARD / SOIRD), Cox proportional-hazards mortality models with
age-scale sensitivity analyses, and all figures and tables.

## What this repository does and does not contain

- **Does not** redistribute NHANES data. All inputs are public; notebook `00`
  fetches them from the CDC. See *Data availability* below.
- **Does** contain every notebook needed to go from those public inputs to the
  numbers, figures, and tables in the paper.

## Repository structure

```
.
├── README.md
├── LICENSE                       # MIT (code)
├── requirements.txt              # Python dependencies (freeze real versions before committing)
├── CITATION.cff                  # machine-readable citation
├── notebooks/                    # run in numeric order
│   ├── 00_download.ipynb         # fetch NHANES cycles + Linked Mortality Files
│   ├── 01_derive_cohort.ipynb    # inclusion/exclusion, T2D definition, feature derivation
│   ├── 02_impute.ipynb           # MICE multiple imputation
│   ├── 03_cluster.ipynb          # consensus clustering, phenotype assignment
│   ├── 04_describe.ipynb         # Table 1 baseline characteristics
│   ├── 05_cox_primary.ipynb      # primary HR models (Table 3a/3b)
│   ├── 06_cox_sensitivity.ipynb  # age-stratified, age-restricted (Supp table)
│   └── 07_figures.ipynb          # heatmap, radar, forest plots
├── src/
│   └── utils.py                  # shared helpers (paths, HR extraction, figure saving, colors)
├── data/
│   ├── raw/                      # NHANES files land here (git-ignored)
│   └── derived/                  # analytic cohort, imputed sets (git-ignored)
└── output/
    ├── figures/                  # generated figures
    └── tables/                   # generated LaTeX/CSV tables
```

Shared constants and helpers live in `src/utils.py` so every notebook uses the
same paths, the same phenotype colors, and the same HR-extraction logic. Each
notebook starts with `import sys; sys.path.append('../src')` then
`from utils import ...`.

## Reproducing the analysis

1. Create an environment and install dependencies:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Launch Jupyter and run the notebooks in order, `00` → `07`:
   ```bash
   jupyter lab
   ```
   Each notebook reads a known input from `data/` and writes a known output,
   so stages can be re-run independently once earlier ones have completed.

Runtime is dominated by consensus clustering and MICE; budget
[VERIFY: e.g. ~30 min] on a modern laptop.

## A note on committing notebooks

Notebook output cells bloat diffs and can leak data previews. Strip outputs
before committing:

```bash
pip install nbstripout
nbstripout --install        # registers a git filter; outputs are cleaned on commit
```

Keep outputs only in notebooks you deliberately want rendered on GitHub.

## Data availability

Data are from the National Health and Nutrition Examination Survey (NHANES),
National Center for Health Statistics (NCHS):
https://www.cdc.gov/nchs/nhanes/

- Cycles: continuous NHANES 1999–2018 [VERIFY exact cycles included]
- Mortality: NCHS Public-Use Linked Mortality Files, linkage through
  31 December [VERIFY year]
- Notebook `00_download.ipynb` retrieves every required file; no manual
  download needed.

No new data were generated. NHANES was approved by the NCHS Research Ethics
Review Board and all participants provided informed consent at collection.

## Citation

> [Author list]. [Title]. [Journal]. [Year]. doi:[DOI]

## Contact

[Name] — [ORCID] — [corresponding email]
