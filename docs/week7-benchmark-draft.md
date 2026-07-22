# Week 7 (Interim) — Draft Benchmark Table

**Student:** Israel De La Mothe
**Status:** DRAFT — quantitative columns are real output from
`notebooks/week7_complex_model_interim.ipynb` run against `data/triage_clean_interim.csv`.
ESI Level 1 recall and the interpretability column are still outstanding (see Notes below).

## Six-Axis Benchmark (+ interpretability)

| Model                | Accuracy | Macro Precision | Macro Recall | Macro F1 | Train Time (s) | Inference Time (s/pred) | Interpretability (1 min to explain to Dr. Reyes?) |
|-----------------------|----------|------------------|--------------|----------|-----------------|--------------------------|----------------------------------------------------|
| Stratified Random     | 0.375    | 0.204            | 0.204        | 0.204    | 0.0031          | 2.48e-07                 | Trivial — no reasoning to explain                   |
| Decision Tree (depth 6)| 0.554   | 0.264            | 0.243        | 0.214    | 0.434           | 6.37e-07                 | Yes — single traversal path                         |
| Logistic Regression   | 0.683    | 0.607            | 0.476        | 0.508    | 5.393           | 1.41e-06                 | Yes — coefficient signs and magnitudes              |
| Random Forest (300 trees) | 0.676| 0.519            | 0.401        | 0.418    | 32.934          | 4.51e-05                 | Partial — feature importances are global; a single prediction needs either one illustrative tree or SHAP |

## ESI Level 1 Recall (primary clinical metric — carried over from Week 6)

| Model                 | ESI Level 1 Recall  |
|------------------------|---------------------|
| Stratified Random      | 0.00                |
| Logistic Regression    | 0.25                |
| Decision Tree          | 0.00                |
| Random Forest          | 0.00                |

*(Run the `esi1_table` cell in the notebook — you have everything else, just haven't pasted this back yet.)*

## What the interim numbers are already telling you

This is a **draft note to yourself for the final memo**, not the memo itself:

- **Random Forest is not the best model on any of the four quantitative metrics.** Logistic
  Regression beats it on accuracy (0.683 vs 0.676), macro precision (0.607 vs 0.519), macro
  recall (0.476 vs 0.401), and macro F1 (0.508 vs 0.418) — while training ~6x faster (5.4s vs
  32.9s) and predicting ~32x faster per patient (1.4e-6s vs 4.5e-5s).
- **Random Forest did clearly beat the Decision Tree** on every metric (e.g. macro F1 0.418 vs
  0.214), so "more complex than Week 6's tree" is a real win — just not "more complex than
  every Week 6 model."
- This is a legitimate, defensible finding, not a failed experiment: the honest headline right
  now is *"the extra compute cost of Random Forest over Decision Tree bought real gains, but
  Logistic Regression already captures those gains more cheaply and just as interpretably."*
  That's exactly the kind of trade-off the ED Board asked you to investigate.
- Before writing the final memo, get the ESI Level 1 recall numbers — it's possible Random
  Forest catches more Level 1 patients even with lower macro F1 (macro F1 averages across all
  5 classes; Level 1 recall is the one number that overrides everything else clinically). That
  could still justify recommending it, or could confirm Logistic Regression as the pick.

## Notes for the final memo

- Fill in ESI Level 1 recall for all four models before drafting the memo's verdict.
- Report training time and inference time as absolute numbers (seconds / seconds-per-prediction) —
  Martina Griffith's question was about compute cost, which needs a number, and you have them.
- Whatever model you recommend, name this Logistic-Regression-vs-Random-Forest result explicitly —
  it's the most interesting and defensible finding in your results so far.
