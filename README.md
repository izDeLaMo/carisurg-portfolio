# CariSurg MedTech Pathways — Portfolio
 
_Last updated: July 14, 2026_
 
A data science portfolio demonstrating clinical data cleaning, exploratory analysis, feasibility assessment, and baseline predictive modelling on real and synthetic ED triage datasets.
 
## 📋 Project Structure
 
```
carisurg-portfolio/
├── README.md                          # Project overview (this file)
├── LICENSE                            # MIT License
├── .gitignore                         # Git ignore rules (excludes /data — see below)
├── requirements.txt                   # Python dependencies
├── notebooks/
│   ├── README.md                      # Notebook-specific documentation
│   ├── Week_0_notebook.ipynb          # Data-cleaning fundamentals (synthetic dataset)
│   ├── Week_5_notebook.ipynb          # ED dataset exploration & feasibility assessment
│   └── Week_6_notebook.ipynb          # Baseline triage classification models
├── docs/
│   ├── feasibility_memo.docx          # Week 5 feasibility memo (ED Board deliverable)
│   ├── week5_missingness_heatmap.png  # Week 5 missingness visualisation
│   ├── week6_report.md                # Week 6 results, metric justification, failure modes
│   ├── week6_confusion_matrix_logreg.png
│   └── week6_confusion_matrix_tree.png
└── data/                              # Gitignored — see data/README.md if present locally
```
 
## 🎯 Overview
 
This portfolio contains:
- **Week 0**: Exploratory data analysis and cleaning fundamentals on a synthetic emergency triage dataset
- **Week 5**: Feasibility assessment of a real 225-feature ED triage dataset (`yaleemmlc_admissionprediction_triage.csv`), culminating in a feasibility memo for a clinical audience
- **Week 6**: Baseline classification models (logistic regression, decision tree) predicting ESI triage level, evaluated against a stratified random baseline, with clinically-justified metric selection
## 🔑 Key Results (Week 6)
 
Three models were trained on the Week 5 cleaned dataset to predict ESI triage level (1–5): a stratified random baseline, logistic regression, and a depth-bounded decision tree. **Recall on ESI Level 1 was selected as the primary evaluation metric**, since under-triaging a critically ill patient (a false negative at Level 1) is the failure mode with the greatest potential for patient harm — see `docs/week6_report.md` for full results, per-class breakdown, and reasoning.
 
**Reproducibility:** `RANDOM_SEED = 42` is used throughout Week 6 for the train/test split and all model initialisations.
 
## 🚀 Quick Start
 
### Option 1: Google Colab
1. Navigate to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Open Notebook**
3. Select the **GitHub** tab
4. Enter: `https://github.com/izDeLaMo/carisurg-portfolio`
5. Select a notebook from `notebooks/`
### Option 2: Local Jupyter
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Week_6_notebook.ipynb
```
 
Week 6 loads its input data via a path relative to the repo root (`data/triage_clean_interim.csv`), so it runs top-to-bottom locally without editing hardcoded paths — see `notebooks/README.md` for details on both run modes.
 
## 📦 Requirements
 
- Python ≥ 3.10
- See `requirements.txt` for dependencies (pandas, numpy, matplotlib, seaborn, scikit-learn)
## 🔒 Data & Privacy
 
The Week 5/6 dataset is a de-identified ED arrivals extract accessed via Mercer Research Ethics Committee approval. Raw and cleaned data files are excluded from this repo via `.gitignore` due to size and the sensitive nature of clinical data, even when de-identified. Only summary statistics, schemas, and column names — never row-level data — were shared with AI tools during analysis.
 
## 📄 License
 
MIT License — See [LICENSE](LICENSE) file
 
---
 
**Repository**: [izDeLaMo/carisurg-portfolio](https://github.com/izDeLaMo/carisurg-portfolio