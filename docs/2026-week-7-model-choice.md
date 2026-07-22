# Decision Journal: Week 7 Model Choice

**Date:** 22 July 2026
**Author:** Israel De La Mothe

## Context

- The ED Board and Martina Griffith (Mercer IT Governance) asked whether a more complex model than the Week 6 baselines is worth its added compute and interpretability cost for the triage classifier.
- Random Forest (300 trees) was built this week as the complexity candidate and benchmarked against the three Week 6 models — stratified random, Decision Tree, and Logistic Regression — on the same train/test split.

## Alternatives considered

- **Random Forest**, the model actually implemented this week: bagged decision trees, chosen for compatibility with the existing unscaled feature set and built-in feature-importance interpretability.
- **Gradient boosting (XGBoost/LightGBM)**: considered but not built this week, on the reasoning that a bagged-tree method should be tried and honestly benchmarked before adding a boosted method's extra tuning surface and compute cost.
- **A small MLP**: also considered and set aside for now, since it would need feature scaling work already done for Logistic Regression but would add a harder-to-explain "why did it say that" story than either tree-based or linear methods — a cost not worth paying before the simpler options were exhausted.

## Decision

Recommend **Logistic Regression** (the existing Week 6 model), not Random Forest, as the model to carry forward into Phase 3.

## Reasoning

- Logistic Regression outperformed Random Forest on every quantitative axis measured — accuracy, macro precision, macro recall, and macro F1 — while training roughly six times faster and predicting roughly thirty times faster per patient.
- Logistic Regression was the only one of the four models to catch any ESI Level 1 patients at all (recall 0.25); both Decision Tree and Random Forest scored 0.00 recall on this class, which is the single highest-harm failure mode identified back in Week 6.
- Random Forest's interpretability, while workable, is less direct than Logistic Regression's signed coefficients — explaining one specific forest prediction needs either an illustrative single tree (not the actual decision path) or an added method such as SHAP, neither of which was necessary for the linear model.

## Things I do not yet know

- Whether these results hold up under cross-validation, rather than a single train/test split — the ESI Level 1 recall figures in particular come from a small number of true Level 1 cases in one test set and could look different on another split.
- Whether Random Forest (or gradient boosting) would close the gap, or even overtake Logistic Regression, once properly tuned and given class weighting to address the rarity of ESI Level 1 — the version built this week used default-leaning settings and no class-imbalance handling, so this comparison may understate what tree-based methods can do.
