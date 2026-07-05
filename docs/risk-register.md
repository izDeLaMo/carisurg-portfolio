# Risk Register — AI-Assisted ED Triage System
**Prepared for:** Saint Cedric Ministry of Health  
**Prepared by:** Clinical AI & Innovation Unit, Mercer Hospital  
**Date:** June 2026  
**System in scope:** AI-assisted triage deployed across the public hospital network ED

---

## Risk Register Table

| # | Risk Name | Category | Likelihood | Impact | Mitigation | Signal of Success |
|---|-----------|----------|------------|--------|------------|-------------------|
| R01 | Algorithmic Bias from Non-Representative Training Data | AI-Technical | H | H | Audit training data demographics against national ED census before deployment; mandate prospective bias monitoring by subgroup (age, sex, ethnicity, postcode) quarterly | Subgroup sensitivity and specificity within ±5% of overall model performance at 6-month review |
| R02 | Distribution Shift at Deployment Sites | AI-Technical | H | H | Establish site-specific validation cohorts before go-live; implement statistical process control charts to detect performance drift; define re-training triggers | Alert fires and investigated within 14 days; model performance does not degrade >3% AUC between quarterly audits |
| R03 | Hallucination / Spurious Clinical Output | AI-Technical | M | H | Constrain model outputs to structured triage categories (e.g., Manchester Triage Scale levels); prohibit free-text clinical reasoning generation; enforce output schema validation | Zero incidents of unconstrained text output reaching clinical staff in post-go-live incident log |
| R04 | Automation Bias — Clinician Over-Reliance | Ethical | H | H | Mandatory training on AI limitations pre-deployment; display model confidence intervals and uncertainty flags at point of care; rotating "AI-off" shifts to maintain clinical baseline skills | Clinical override rate remains ≥15% (indicating active independent judgment); surveyed clinician confidence in independent triage does not decline at 12 months |
| R05 | Alert Fatigue from High False-Positive Rate | Operational | H | M | Set precision thresholds conservatively (favour recall for high-acuity cases); implement tiered alert severity; review alert burden monthly for first 6 months | Clinician-reported alert fatigue score (validated scale) does not increase from baseline; false positive rate for ESI-1/2 flags <10% |
| R06 | Clinician Workflow Overload During Transition | Operational | M | M | Phased rollout (pilot 2 sites before national); dedicated AI liaison nurse per shift during first 3 months; parallel manual triage retained for 6-month overlap | No increase in median triage-to-physician time during transition period; staff sickness absence rate does not rise >2% above baseline |
| R07 | Lack of Informed Consent for AI-Assisted Assessment | Ethical | M | H | Display patient-facing notice at triage point (all languages spoken by ≥5% of local population); provide opt-out pathway documented in policy; legal review of consent framework before go-live | 100% of sites have compliant signage at audit; opt-out requests documented and honoured within same attendance |
| R08 | Data Privacy and Secondary Use Risk | Ethical | M | H | All triage data processed under existing health data governance; no sharing with third-party AI vendors without explicit data-sharing agreement and ethics board approval; de-identification before model re-training | Zero data governance incidents at annual DPA audit; ethics board renewal completed annually |
| R09 | Equity Gap — Paediatric Patients | Equity | H | H | Ensure training dataset contains ≥20% paediatric cases proportional to national ED attendance; stratify validation metrics by age band (<2, 2–12, 13–17); paediatrician review of paediatric triage outputs pre-deployment | Paediatric under-triage rate ≤ adult under-triage rate at 6-month evaluation |
| R10 | Equity Gap — Rural and Low-Resource Deployment Sites | Equity | M | H | Assess connectivity and device infrastructure at all sites before rollout; provide offline fallback triage protocol; rural sites included in pilot cohort | Rural sites achieve same system uptime SLA (≥99%) as urban sites; no documented instances of AI system failure causing triage delay at rural sites |
| R11 | Regulatory and Liability Ambiguity | Operational | M | H | Engage national medical device regulator early; classify system under appropriate SaMD framework; define in writing whether AI is decision-support or decision-making; obtain indemnity clarity from MoH before go-live | Regulatory approval documented; liability framework signed off by hospital legal counsel and MoH before any patient contact |
| R12 | Model Opaqueness Undermining Clinical Trust | AI-Technical | M | M | Require explainability layer (e.g., SHAP values or equivalent) surfaced to senior clinicians on request; include interpretability requirements in procurement specification | ≥70% of ED clinicians report understanding why the model flagged a case in post-deployment survey (6 months) |

---

## Risk Memo — Top 3 Risks Explained

*Prepared for non-technical Ministry stakeholders.*

---

### 1. Algorithmic Bias (R01) — The System May Discriminate Without Anyone Noticing

**What is the risk?**  
AI triage models learn patterns from historical data. If the data that trained this model came predominantly from one type of hospital — say, a large urban centre serving a working-age population — the model will perform well for patients who look like that training set, and worse for patients who do not: elderly patients, children, women with atypical presentations, or patients from ethnic minority communities.

**Why does it matter here?**  
Under-triage — classifying a critically ill patient as lower priority — can cause death or permanent harm. If the model systematically under-triages a particular demographic group, we have embedded discrimination into a life-and-death decision.

**What do we propose?**  
Before deployment, the Ministry should commission an independent demographic audit of the training data. At every participating site, the model's accuracy must be reported separately for each population subgroup, not just as a single headline figure. If subgroup performance falls outside an acceptable band, deployment at that site must pause. This is not optional — it is the minimum standard of care.

**Can we defend this mitigation?**  
Partially. Bias auditing catches known demographic categories, but may miss intersectional gaps (e.g., elderly rural women). Ongoing monitoring is essential; a one-time pre-deployment audit is necessary but not sufficient.

---

### 2. Automation Bias (R04) — Clinicians May Stop Thinking

**What is the risk?**  
When a computer gives a confident-sounding recommendation, humans tend to follow it — even when their own clinical instinct disagrees. This is called automation bias, and it is well-documented in aviation, radiology, and increasingly in emergency medicine. If ED nurses and physicians defer to the AI instead of independently assessing the patient, the AI's errors become clinical errors with no human safety net.

**Why does it matter here?**  
A nationwide rollout means this risk scales across every ED in the country simultaneously. One model failure pattern could affect thousands of patients before it is detected.

**What do we propose?**  
Training before deployment must explicitly teach clinicians *when and why to override* the system, not just how to use it. The interface should display model uncertainty, not just a triage category. Critically, we recommend periodic "AI-off" triage shifts so that clinical skills do not atrophy. We should track the override rate: if clinicians almost never override the system, that is a warning sign — not a sign the model is performing well.

**Can we defend this mitigation?**  
Yes, with caveats. Override rate is an imperfect proxy; clinicians may override for social reasons (e.g., patient insistence) rather than clinical ones. Qualitative audits of documented overrides are needed alongside the quantitative signal.

---

### 3. Equity Gap — Paediatric Patients (R09) — Children Are Not Small Adults

**What is the risk?**  
Paediatric emergency medicine has different normal ranges, different presentations, and different risk stratification rules from adult medicine. If the training dataset under-represents children — which is common, because paediatric ED attendances are a minority of total ED volume — the model will be less accurate for children. Misclassifying a seriously ill child has catastrophic consequences.

**Why does it matter here?**  
A single nationwide AI system, if not explicitly validated on paediatric populations, will be deployed into paediatric waiting rooms by default unless we act.

**What do we propose?**  
Paediatric validation must be treated as a separate workstream, not a footnote. We recommend a minimum paediatric representation threshold in training data, a dedicated paediatrician review of model outputs in this age group, and age-stratified performance metrics as a go/no-go criterion at every site. If the model cannot meet the same performance standards for children as for adults, it should not be deployed in any department that sees children — which is most EDs.

**Can we defend this mitigation?**  
Yes. This is standard practice in paediatric medical device validation and aligns with existing NHS and WHO guidance on inclusive AI development.

---

*"Do not flinch. If you cannot defend a mitigation, say so."*  
Risks R01 and R04 carry partial defences only. This register should be treated as a living document, reviewed at 3, 6, and 12 months post-deployment with updated evidence.*
