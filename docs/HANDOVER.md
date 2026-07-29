# Handover Document

**Status:** Final (Week 8). Test passed: a new hire can clone this repo, read
this document, and be running the model within minutes.

## 1. Project Summary

> This repo builds an ED triage classifier for Mercer that predicts ESI
> (Emergency Severity Index) level from vital signs and chief-complaint
> flags. Four candidate models were compared across Weeks 6-7 (baseline,
> decision tree, random forest, logistic regression); Logistic Regression
> was selected as the Phase 3 model and is the only model trained by
> `scripts/train.py`.

## 2. Final Model Decision
- **Model:** Logistic Regression (`solver="lbfgs"`, `max_iter=2000`, scaled features)
- **One-sentence why:** It beat every other candidate on all four accuracy
  metrics *and* was the only model to catch any ESI Level 1 patients, while
  costing far less to train and run than Random Forest.
- Full reasoning: `docs/model-selection.md` + Week 7 cost-benefit memo.

## 3. How to Run
```bash
git clone https://github.com/izDeLaMo/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv venv && source venv/Scripts/activate   # Git Bash on Windows; use venv/bin/activate on macOS/Linux
pip install -r requirements.txt
python scripts/train.py --config config.yaml
```
- **Python version:** 3.12.10
- **Expected runtime:** ~2 seconds total on the full dataset (44,096 train / 11,025
  test rows) — training takes ~1.6s, inference is effectively instant
  (~0.0000005s per prediction). No GPU or special hardware required.
- Confirmed working from a clean venv on the training machine (see verification
  run, 28 July 2026).

## 4. Where the Data Lives (and governance status)
- **Location:** `data/triage_clean_interim.csv`, committed directly in this repo.
- **Governance status:** Fully synthetic/fake data generated for coursework — not
  real or identifiable patient data. No PHI, no de-identification process required.
- **Access:** Open to anyone with access to this repo. No approval process,
  named contact, or external data request needed — a new hire can clone and
  run immediately.

## 5. Known Limitations
- ESI Level 1 recall is only 0.25 — **not adequate for clinical deployment
  as-is**; 3 in 4 of the most critical patients would still be missed.
- No cross-validation performed; results come from a single 80/20 split and
  could shift under a different split or k-fold evaluation.
- Class imbalance (ESI Level 1 is rare) was not directly addressed via class
  weighting or resampling for any model, including the pinned one.

---
