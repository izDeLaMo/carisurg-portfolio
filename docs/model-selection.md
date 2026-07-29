# Model-Selection Results Table

**Status:** DRAFT (Week 8 interim). Figures below are copied from the Week 7
cost-benefit memo and interim notebook; they will be re-verified against the
final repo run before Tuesday's final submission.

**Full reasoning:** see `Week 7 Cost-Benefit Memo` 
— the decision journal entry behind this table's winner. Key excerpt: Logistic
Regression was carried forward because it beat Random Forest on every accuracy
and safety metric measured, while training ~6x faster and predicting ~30x faster
per patient.

**Dataset:** `data/triage_clean_interim.csv`, identical 80/20 stratified split
(`random_state=42`) across all four models — same unseen patients every time.

# Model-Selection Results Table

**Status:** FINAL (Week 8). Accuracy/precision/recall/F1 and ESI Level 1 recall
verified against a real end-to-end run of `scripts/train.py` on the full
dataset (44,096 train / 11,025 test rows, 28 July 2026) — they match the
Week 7 cost-benefit memo exactly. Train/inference timing below is from that
same verification run (repo owner's machine); the original memo's timings
came from a different machine, so the two won't match exactly — that's
expected and doesn't affect the model comparison, since both models were
timed on the same machine within each run.

**Full reasoning:** see `Week 7 Cost-Benefit Memo` (Israel De La Mothe, 22 July 2026)
— the decision journal entry behind this table's winner. Key excerpt: Logistic
Regression was carried forward because it beat Random Forest on every accuracy
and safety metric measured, while training ~6x faster and predicting ~30x faster
per patient.

**Dataset:** `data/triage_clean_interim.csv`, identical 80/20 stratified split
(`random_state=42`) across all four models — same unseen patients every time.

## Six-axis benchmark + ESI Level 1 recall

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Train Time (s) | Inference Time (s/pred) | ESI Level 1 Recall | Winner |
|---|---|---|---|---|---|---|---|---|
| Stratified Random (baseline) | 0.375 | 0.204 | 0.204 | 0.204 | 0.003 | 2.5e-07 | 0.00 | |
| Decision Tree (max_depth=6) | 0.554 | 0.264 | 0.243 | 0.214 | 0.434 | 6.4e-07 | 0.00 | |
| Random Forest (300 trees) | 0.676 | 0.519 | 0.401 | 0.418 | 32.934 | 4.5e-05 | 0.00 | |
| **Logistic Regression** | **0.6828** | **0.6067** | **0.4756** | **0.5079** | 1.638 | 4.5e-07 | **0.2500** | ✅ **Pinned Phase 3 model** |

*Logistic Regression's accuracy/precision/recall/F1/ESI-1-recall columns are
from the verified real repo run. Its train/inference time are also from that
run (repo owner's machine, 28 July 2026). Baseline, Decision Tree, and Random
Forest timings are carried over from the Week 7 memo, run on a different
machine — they are shown for the audit trail and are still valid for the
relative comparison (Logistic Regression was ~6x faster to train and ~30x
faster per prediction than Random Forest *on the same machine* in the
original Week 7 benchmark).

## Key hyperparameters per model

| Model | Key Hyperparameters |
|---|---|
| Stratified Random | `strategy="stratified"`, `random_state=42` |
| Decision Tree | `max_depth=6`, `random_state=42` |
| Random Forest | `n_estimators=300`, `max_depth=None`, `min_samples_leaf=2`, `random_state=42` |
| **Logistic Regression** | `max_iter=2000`, `solver="lbfgs"`, `random_state=42`, features scaled with `StandardScaler` |

## Why Logistic Regression won (summary — see decision journal for full argument)

- Wins on **every** quantitative axis (accuracy, macro precision, macro recall, macro F1) —
  not a complexity/accuracy trade-off, since it is both more accurate and cheaper.
- The **only** model with non-zero ESI Level 1 recall (0.25) — both tree-based models
  scored 0.00 on the rarest, most dangerous class to miss.
- Cheapest to train (~6x less compute than Random Forest) and cheapest to run
  (~30x less inference time per prediction), with the simplest explanation
  path (signed coefficients vs. feature importances / SHAP).

## Known caveats carried into Phase 3 (do not treat as fully validated)

- ESI Level 1 recall of 0.25 is **not adequate for deployment on its own** — 3 in 4
  Level 1 patients would still be missed.
- No cross-validation performed yet — all figures from a single 80/20 split.
- Class imbalance not directly addressed for any model (no class weighting/resampling).
- Interpretability judged by inspection, not yet reviewed by a clinician (Dr. Reyes).

*Table verified against `scripts/train.py` output on the real dataset,
28 July 2026 — accuracy/precision/recall/F1/ESI-1-recall for the pinned
model match the Week 7 memo exactly.*
