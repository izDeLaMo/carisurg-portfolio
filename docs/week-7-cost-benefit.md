# Cost-Benefit Memo: Model Selection for Phase 3

**To:** Dr. De Fretias; the ED Board; Martina Griffith, Clinical IT Lead (Mercer IT Governance)
**From:** Israel De La Mothe
**Date:** 22 July 2026
**Re:** Week 7 model optimisation — recommendation for the ED triage classifier

## Verdict

Phase 3 should proceed with the **Logistic Regression** model from Week 6, not the more complex Random Forest built this week: Logistic Regression beats Random Forest on every accuracy and safety metric measured, while costing roughly six times less to train and around thirty times less to run per prediction — meaning the added complexity did not buy anything this time, on this dataset.

## Recap: dataset and method

Both models were trained and tested on the same cleaned Mercer triage dataset used in Week 6 (`data/triage_clean_interim.csv`), using the identical 80/20 stratified train/test split (fixed random seed, so both models were evaluated on exactly the same unseen patients). The feature set is unchanged from Week 6: numeric vital-sign fields and binary chief-complaint flags, with outcome-leaking fields (disposition, previous disposition) removed. Four models were compared: a stratified-random baseline (the "coin flip" floor), the Week 6 Decision Tree, the Week 6 Logistic Regression, and this week's new model, a Random Forest of 300 trees. Random Forest was the complexity option chosen over gradient boosting or a small neural network because it fits the same unscaled, sparse binary features the Decision Tree already used, and because it comes with a built-in, clinician-explainable route to interpretability (feature importances) without needing an additional library.

Two families of metric were tracked, matching the ED Board's brief: (1) six quantitative axes — accuracy, macro precision, macro recall, macro F1, training time, and inference time per prediction — and (2) the qualitative axis of interpretability, i.e. whether a single prediction can be explained to Dr. Reyes in under a minute. A seventh, clinically-weighted number was also carried forward from Week 6: recall on ESI Level 1, the rarest and most dangerous class to miss, since a model can look strong on aggregate accuracy while still failing the patients it is most important not to fail.

## Benchmark results

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Train Time (s) | Inference Time (s/pred) | ESI Level 1 Recall |
|---|---|---|---|---|---|---|---|
| Stratified Random | 0.375 | 0.204 | 0.204 | 0.204 | 0.003 | 2.5e-07 | 0.00 |
| Decision Tree | 0.554 | 0.264 | 0.243 | 0.214 | 0.434 | 6.4e-07 | 0.00 |
| Random Forest | 0.676 | 0.519 | 0.401 | 0.418 | 32.934 | 4.5e-05 | 0.00 |
| **Logistic Regression** | **0.683** | **0.607** | **0.476** | **0.508** | 5.393 | 1.4e-06 | **0.25** |

The single most important row in this table is the last column. Both tree-based models — the Week 6 Decision Tree and this week's Random Forest — correctly identify **zero** ESI Level 1 patients in the test set: an ESI Level 1 recall of 0.00. Logistic Regression is the only model that identifies any of them at all, catching one in four. Aggregate accuracy and macro F1 tell a similar but less stark story: Logistic Regression leads on every one of the four quantitative accuracy metrics, and does so while training in roughly a sixth of the time and predicting in roughly a thirtieth of the time, per patient, compared with Random Forest.

Interpretability is comparable between the two leading models but not identical. Logistic Regression's explanation is a direct one: each feature has a signed coefficient, so a clinician can be told plainly that a given vital sign or complaint flag pushed the predicted urgency up or down, and by roughly how much. Random Forest's explanation is necessarily indirect: feature importances describe the model's behaviour in general, but explaining one specific prediction requires either walking through a single illustrative tree (which is not actually the tree that produced the forest's answer) or bringing in an additional interpretability method such as SHAP, which was not built this week and would itself add compute cost.

## Three arguments for Logistic Regression

1. **It wins on every quantitative axis, not just one.** Higher accuracy, macro precision, macro recall, and macro F1 than Random Forest — this is not a case of trading accuracy for cost, since Logistic Regression is both more accurate and cheaper.
2. **It is the only model that catches any ESI Level 1 patients at all.** Given that missing a Level 1 patient is the highest-harm failure mode identified back in Week 6, a model with 0.00 recall on that class — true of both tree-based models here — is a patient-safety concern independent of its other scores.
3. **Its cost profile and its explanation are both simpler**, which matters directly to Martina Griffith's brief: roughly a sixth of the training compute and a thirtieth of the inference-time cost of Random Forest, with an explanation (signed coefficients) that does not depend on an additional library or a caveat about which tree was used.

## Three arguments against (risks in taking this as the final word)

1. **A recall of 0.25 on ESI Level 1 is not good enough to deploy on its own.** "Best of the four models tested" is not the same as "clinically adequate" — missing three out of every four of the most critical patients would still be an unacceptable outcome in a live system, and this result should not be read as validating Logistic Regression for deployment as-is.
2. **Logistic Regression assumes an essentially additive relationship** between each feature and the predicted log-odds of an ESI category. If the true clinical picture depends on interactions between vitals and complaints (for example, a moderately raised heart rate mattering far more in combination with a specific complaint than alone), a linear model may be systematically underfitting relationships that a tree-based or neural model could, in principle, capture — and this comparison does not rule that out.
3. **Random Forest's weak showing may partly be an artefact of how it was configured, not a fundamental limit of tree ensembles.** It was run this week with default-leaning settings (300 trees, no depth limit beyond a minimum leaf size, no class weighting) and no hyperparameter search. Class imbalance in particular — ESI Level 1 is rare in this dataset — is known to hurt tree-based recall on minority classes unless addressed directly (e.g. `class_weight="balanced"`), and that step was not taken for either tree-based model this week. A fairer contest would tune both models properly before drawing a final conclusion about tree ensembles specifically.

## Risks and unknowns

- **No cross-validation was performed.** All figures above come from a single 80/20 split; the ranking of models, and especially the Level 1 recall figures (which are computed from a small number of true Level 1 patients in one test set), could shift under a different split or a k-fold evaluation.
- **Class imbalance was not directly addressed for any model.** None of the four models used class weighting or resampling to counter the rarity of ESI Level 1; the low Level 1 recall across the board may be as much a symptom of this as of model choice.
- **Interpretability was assessed by inspection, not by an actual clinician.** Dr. Reyes has not yet reviewed either the coefficient-based or the tree-based explanation; "explainable in under a minute" is currently the author's judgement, not a validated one.
- **No comparison against WHO ETAT guidance has been carried out yet**, a gap already flagged at the end of Week 6 and still open.

## Recommendation

Carry **Logistic Regression** forward as the Phase 3 baseline in place of Random Forest, on cost and on every accuracy metric measured; but treat its ESI Level 1 recall of 0.25 as inadequate for any deployment discussion, and prioritise class-imbalance handling (class weighting or resampling) and a clinician review of the model's explanations before that discussion happens — with Random Forest and other tree-based or boosted models left open to revisit only after they, too, have been properly tuned and weighted for class imbalance, rather than ruled out on this week's default configuration alone.
