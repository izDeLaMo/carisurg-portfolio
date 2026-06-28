# AI Harm Case Study — Root-Cause Analysis
**Prepared for:** Saint Cedric Ministry of Health / Week 4 Interim Submission  
**System in scope:** AI-assisted ED Triage Nationwide Rollout  
**Document:** `docs/ai-harm-case-study.md`

---

## Case: Epic Sepsis Model (ESM) — Systematic Under-Detection of Sepsis Across US Hospitals

### What Happened

Epic Systems' proprietary sepsis prediction algorithm — embedded in the electronic health record used by hundreds of US hospitals — was the subject of a landmark independent evaluation published in *JAMA Internal Medicine* in 2021 (Wong et al.). Researchers at the University of Michigan retrospectively validated the model on 38,455 patient encounters and found that **the algorithm missed 67% of sepsis cases** that a clinician-derived criterion (Sepsis-3) would have flagged. Put differently, the model's sensitivity for sepsis was approximately 33% — meaning two in three patients who developed sepsis were not flagged by the system intended to catch them early.

Simultaneously, the model generated a large volume of false positives: for every true sepsis case the model correctly identified, it also flagged roughly seven patients who did not have sepsis. This created a dual burden: genuine sepsis cases going undetected while nursing and medical staff were diverted to investigate false alerts.

The model had been deployed widely across health systems before this independent external validation was published. Internal Epic validation figures, shared with hospitals at the time of procurement, showed substantially better performance — figures that were later found to have been generated on the same data distribution used to develop the model (internal validation), not on held-out or external populations.

---

### Root-Cause Analysis

#### 1. What Happened

An AI sepsis prediction model was deployed at scale across US hospitals embedded within routine clinical workflows. It underperformed dramatically on independent evaluation, missing the majority of sepsis cases it was designed to catch — a condition where delays in recognition carry significant mortality risk.

#### 2. Why It Happened — Five Root Causes

**Root Cause 1: Internal-Only Validation**  
The model was validated by its developer on internal data before release. Internal validation consistently produces optimistic performance estimates because the model is tested on data drawn from the same distribution it was trained on. No mandatory external, prospective, or independent validation was required before widespread hospital deployment. When external researchers applied the model to a different hospital population, performance collapsed.

**Root Cause 2: Mismatch Between Training Population and Deployment Population**  
The model was trained on data from Epic's own client hospitals — a predominantly large, US-based, insured-population cohort. When applied to populations with different comorbidity profiles, documentation practices, or patient demographics, the model's learned associations no longer held. This is a classic distribution shift failure.

**Root Cause 3: Regulatory Gap for Software as a Medical Device (SaMD)**  
At the time of deployment, clinical decision support software embedded within existing EHR systems was not subject to FDA pre-market review under the enforcement discretion policies then in place. There was no regulatory requirement to demonstrate clinical efficacy before deployment. The model was treated as a quality improvement tool rather than a diagnostic medical device, sidestepping the evidentiary standards applied to equivalent diagnostic tests.

**Root Cause 4: Alert Fatigue Masking the Signal**  
The high false-positive rate meant that clinical staff were repeatedly responding to sepsis alerts that did not result in confirmed sepsis. This is a well-documented precondition for alert fatigue: when a signal fires frequently and is often wrong, clinicians begin to habituate and may respond more slowly or less thoroughly — including, potentially, to true positives. The model's failure mode was therefore self-amplifying.

**Root Cause 5: No Prospective Monitoring Obligation**  
Hospitals that adopted the ESM were not required to monitor its real-world performance prospectively. The gap between deployment and the Wong et al. publication was several years. During that period, there was no systematic mechanism to detect that the model was underperforming at participating sites.

#### 3. What the System Failed to Anticipate

The procurement and deployment process failed to anticipate that a model performing well under internal conditions would generalise poorly to heterogeneous real-world populations. It also failed to anticipate that embedding a high-false-positive model into a high-workload environment would generate clinician alert fatigue rather than heightened vigilance. The system assumed that deployment of an AI alert was inherently additive to care quality; it did not model the scenario in which the alert degrades clinical decision-making by crying wolf.

#### 4. What Would Have Caught It

- **Mandatory external prospective validation** on at least two geographically and demographically distinct hospital populations before commercial deployment — with performance reported stratified by subgroup
- **Regulatory classification as SaMD** requiring pre-market submission of clinical evidence to the FDA or equivalent national regulator
- **Post-market surveillance obligation** written into procurement contracts, requiring hospitals to monitor and report sensitivity/specificity quarterly against a ground-truth retrospective sepsis diagnosis
- **Alert burden monitoring** — a simple dashboard tracking alert volume per shift against confirmed sepsis rate would have made the false-positive excess visible within weeks of deployment

---

### Relevance to AI-Assisted ED Triage Rollout

The ESM case is directly applicable to the proposed Saint Cedric deployment. An ED triage model shares the same failure modes: it will be trained on data from a subset of hospitals, deployed into a heterogeneous national population, embedded in a high-workload environment, and will generate alerts that clinicians must respond to under time pressure. The lessons are clear:

1. External, site-specific validation before go-live is not optional
2. Performance must be reported by subgroup, not as a single headline figure
3. A regulatory classification decision must be made explicitly before deployment, not deferred
4. Post-deployment monitoring must be contractually required, not aspirational

---

### Source

Wong A, Otles E, Donnelly JP, et al. *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients.* JAMA Internal Medicine. 2021;181(8):1065–1070. doi:10.1001/jamainternmed.2021.2626

Additional context: Ross S, Adalja A. *Sepsis Algorithm Embedded in Health Records Misses Most Cases.* STAT News, 26 July 2021.

---

*Word count (case narrative and RCA): ~620 words*
