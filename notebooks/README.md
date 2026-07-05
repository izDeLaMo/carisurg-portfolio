# CariSurg MedTech Pathways — Notebooks

This folder contains two notebooks from the CariSurg AI Programme, tracking progress from initial data-cleaning fundamentals through to feasibility assessment of a real clinical dataset.

## Contents

| File | Description |
|---|---|
| `Week_0_notebook.ipynb` | Foundational data-cleaning exercises (Assignments 2 & 3) using a synthetic "dirty" ED triage dataset. Covers type coercion, range validation, unit standardisation, median imputation, and clinically-annotated visualisations. |
| `Week_5_notebook.ipynb` | Data exploration and feasibility assessment on the real `yaleemmlc_admissionprediction_triage.csv` dataset (225 features, ED arrivals). Interim submission for the Week 5–6 AI-Assisted Triage project. |

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
- Includes a custom visualisation task: pulse distribution and Age vs. RR scatter plot, both annotated with clinical reference ranges

**Status:** Complete — cleaning pipeline consolidated at the top of Assignment 3 section for reuse.

---

## Week 5 — AI-Assisted Triage: Data Exploration (Interim)

**Dataset:** `yaleemmlc_admissionprediction_triage.csv` (225 clinical features, real de-identified ED data)

**Objective:** Determine whether this dataset is suitable for building an AI-assisted triage prediction model, ahead of a feasibility memo to the ED Board.

**What it does:**
- Loads and profiles the dataset (`.info()`, `.describe()`, shape)
- Clinical context section explaining ESI, vitals, chief complaints, demographics, and arrival mode
- Missing value analysis: summary table + missingness heatmap
- Duplicate record check
- Demographic breakdowns: age, gender, race, ethnicity, arrival mode
- Vital sign distributions, correlation matrix, and boxplots for outlier detection
- Top 20 chief complaints by frequency
- Correlation between top chief complaints, ESI, and vital signs
- Documents columns with >20% missingness
- Feasibility memo outline (verdict, dataset summary, top concerns, reasons to proceed, caveats)
- Saves an interim cleaned dataset (`triage_clean_interim.csv`)

**Status:** Interim submission. Full cleaning pipeline, final feasibility memo, and top-10 feature shortlist to follow in the final submission.

**Note on AI usage:** Clinical interpretations in this notebook were drafted with AI (Claude) assistance per programme guidance, and cross-checked against standard references before inclusion. Only summary statistics and column names were shared with the AI tool — no raw patient-level data.

---

## Running the notebooks

Both notebooks are designed for Google Colab:
1. Open via the "Open in Colab" badge at the top of each notebook, or upload directly to Colab.
2. Mount Google Drive when prompted (Week 5) or update `FILE_PATH` to point to your local copy of the dataset.
3. Run all cells top to bottom.

**Data files are not included in this repo** (see `.gitignore`) due to size and the sensitive/de-identified nature of the Week 5 clinical dataset.