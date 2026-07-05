## Feasibility Memo Outline (Draft — to be expanded into full memo)

**(a) One-sentence verdict**
Proceed with caution — the dataset is large and clinically rich enough to support a baseline triage model, but several missingness and encoding issues must be addressed first.

**(b) Dataset summary**
- ~55,000+ ED patient encounters, 225 clinical features
- Covers demographics, vital signs, chief complaints, and ESI (target variable)
- De-identified, single-source EHR extract

**(c) Top 3 quality concerns**
1. Missing values concentrated in specific clinical measurement columns
2. Very high sparsity across the `cc_*` chief complaint columns
3. Potential outliers in vital sign readings requiring clinical review before removal

**(d) Top 3 reasons to proceed**
1. Sample size is large enough to support robust model training
2. ESI provides a clean, clinically standard target variable
3. Core physiological features (vitals) are largely complete and usable

**(e) Caveats**
- Findings are based on exploratory analysis only; no modelling has been done yet
- Chief complaint sparsity may require grouping/dimensionality reduction before use
- Demographic variables should be handled carefully to avoid introducing bias
- Final imputation and outlier-handling decisions will be documented in Week 6