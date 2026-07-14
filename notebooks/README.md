# CariSurg MedTech Pathways — Notebooks
 
_Last updated: July 14, 2026_
 
This folder contains the notebooks for the CariSurg AI Programme, tracking progress from data-cleaning fundamentals through to a baseline triage classification model.
 
## Contents
 
| File | Description |
|---|---|
| `Week_0_notebook.ipynb` | Foundational data-cleaning exercises (Assignments 2 & 3) using a synthetic "dirty" ED triage dataset. Covers type coercion, range validation, unit standardisation, median imputation, and clinically-annotated visualisations. |
| `Week_5_notebook.ipynb` | Data exploration and feasibility assessment on the real `yaleemmlc_admissionprediction_triage.csv` dataset (225 features, ED arrivals). |
| `Week_6_notebook.ipynb` | Baseline triage classification models (logistic regression, decision tree) trained on the Week 5 cleaned dataset, evaluated against a stratified random baseline. Final submission. |
 
---
 
## Week 0 — Data Cleaning Fundamentals
 
**Dataset:** `EmergencyTriageDataset_Reduced_Dirty.csv` (synthetic, intentionally messy)
 
**What it does:**
- Cleans and standardises core vitals: GCS, SBP, DBP, Temp, Pulse, RR, FiO2, MAP
- Applies type coercion (`pd.to_numeric`, `errors='coerce'`) to fix mixed-type columns
- Applies clinically valid range filters, flags out-of-range values as NaN
- Standardises inconsistent units (e.g. Temp in mixed C/F strings → Celsius)
- Imputes missing values using median (justified by skew/outlier presence)
- Produces distribution plots (histogram + boxplot) before and after cleaning
**Status:** Complete.
 
---
 
## Week 5 — AI-Assisted Triage: Data Exploration
 
**Dataset:** `yaleemmlc_admissionprediction_triage.csv` (225 clinical features, ~55,000 real de-identified ED encounters)
 
**Key finding:** the dataset contains **zero missing values** across all 225 columns, confirmed via a sentinel-value investigation (checked for disguised missingness such as `-1`, `999`, blank strings — none found). This indicates upstream cleaning by the original curators before the data was shared for this course, which is itself a governance consideration since that upstream process isn't visible to us. Primary quality concerns are sparsity in the ~200 `cc_*` chief-complaint columns and this lack of upstream visibility, not missing data.
 
**What it does:**
- Loads and profiles the dataset (`.info()`, `.describe()`, shape)
- Clinical context for ESI, vitals, chief complaints, demographics, and arrival mode
- Missing value analysis, missingness heatmap, and sentinel-value investigation
- Demographic breakdowns, vital sign distributions and correlations, outlier boxplots
- Top 20 chief complaints and their correlation with ESI/vitals
- Feasibility memo outline
- Saves cleaned dataset (`triage_clean_interim.csv`) used as input to Week 6
**Status:** Complete. See `docs/feasibility_memo.docx`.
 
---
 
## Week 6 — Baseline Triage Classification Model
 
**Input:** `triage_clean_interim.csv` (output of Week 5 notebook)
 
**What it does:**
- Loads the cleaned dataset via a relative path (no hardcoded Colab paths)
- Defines target (`esi`) and feature set, dropping outcome-leaking columns (`disposition`, `previousdispo`)
- Stratified 80/20 train/test split, `RANDOM_SEED = 42`
- Scales features for logistic regression (`StandardScaler`)
- Trains and evaluates three models: stratified random baseline (`DummyClassifier`), logistic regression, and a depth-bounded decision tree
- Produces clinically-labelled confusion matrices (integer ESI levels, "True/Predicted ESI Level" axes) for each model
- Compares macro vs. weighted F1 across models with a plain-language explanation of the difference
- States and justifies the primary metric (recall on ESI Level 1) with clinical reasoning
- Documents the model's failure mode and its patient-safety implications
**Status:** Final submission. See `docs/week6_report.md` and the Loom clinical explainer video linked there.
 
---
 
## Running the notebooks
 
Both Week 5 and Week 6 are designed to run either in Google Colab or locally from a repo clone:
1. **Colab:** open via the "Open in Colab" badge, or upload directly. Mount Google Drive when prompted and update the data path if your Drive folder structure differs.
2. **Local:** `pip install -r requirements.txt`, then run top to bottom from the repo root — Week 6 resolves `data/triage_clean_interim.csv` relative to the repo, no path edits needed.
**Reproducibility:** `RANDOM_SEED = 42` is used for the train/test split and all model initialisations in Week 6.
 
**Data files are not included in this repo** (see `.gitignore`) due to size and the sensitive/de-identified nature of the clinical dataset.