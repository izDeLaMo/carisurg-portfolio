# Handover Document (DRAFT — Week 8 Interim)

**Status:** Outline only. Full prose to be written for the Tuesday final submission.
Test: could a new hire, arriving Monday morning, clone this repo, read this
document, and be running the model by end of day?

## 1. Project Summary
*(one paragraph — draft below, expand for final)*

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
git clone <repo-url>
cd <repo-name>
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python scripts/train.py --config config.yaml
```
*(To fill in for final: exact Python version pinned, expected runtime, where
requirements.txt versions come from — Week 2.)*

## 4. Where the Data Lives (and governance status)
- Path: `data/triage_clean_interim.csv`
- *(To fill in for final: is this file committed to the repo, or governed/
  access-controlled by Mercer IT? If access-controlled, state who to contact
  and what approval is needed — this is a Martina Griffith governance
  question, not optional.)*

## 5. Known Limitations
- ESI Level 1 recall is only 0.25 — **not adequate for clinical deployment
  as-is**; 3 in 4 of the most critical patients would still be missed.
- No cross-validation performed; results come from a single 80/20 split and
  could shift under a different split or k-fold evaluation.
- Class imbalance (ESI Level 1 is rare) was not directly addressed via class
  weighting or resampling for any model, including the pinned one.

---
*Remaining work before final submission: expand section 1 to full paragraph,
confirm exact run time and Python version in section 3, fill in data
governance status in section 4, and reconcile section 5 with any new
findings from finishing the pytest suite.*
