# CariSurg MedTech Pathways — Week 0 
## Setup Instructions
 
### Method 1: Direct GitHub Integration (Recommended)
 
1. **Open Google Colab**
   - Navigate to [colab.research.google.com](https://colab.research.google.com)
2. **Load Notebook from GitHub**
   - Click **File → Open Notebook**
   - Select the **GitHub** tab
   - Enter repository URL: `https://github.com/izDeLaMo/CariSurg-MedTech-Week0`
   - Choose the notebook you want to run (e.g., `01_gender_cleaning.ipynb`)
---
## Assignment 1: Gender Column Cleaning
### Overview

This task cleans the Gender column in the Emergency Triage dataset using Python and Pandas in Google Colab.
### Tasks

This assignment focused on cleaning and standardizing the Gender column in the Emergency Triage dataset using Python and Pandas in Google Colab. The dataset was loaded from Google Drive, and the values in the Gender column were examined to identify inconsistent formats such as uppercase text and numeric strings. A mapping method was used to convert all male values to 1, all female values to 0 and all other values to 2, creating a clean and consistent dataset. After cleaning, the original column was removed, the cleaned column was renamed to Gender and the final dataset was verified to ensure there were no missing values.

**Process:**
1. Loaded the dataset from Google Drive
2. Examined the Gender column to identify inconsistent formats (uppercase text, numeric strings, etc.)
3. Applied a mapping method to standardize values:
   - Male → `1`
   - Female → `0`
   - Other/Unknown → `2`
4. Removed the original column and renamed the cleaned column to `Gender`
5. Verified the final dataset for missing values
**Outcome:** A clean, consistent Gender column with standardized numeric encoding.

---
## Assignment 2: Clinical Variables Cleaning
### Overview

This task focused on cleaning and standardising the Pulse column in the Emergency Triage dataset using Python and Pandas in Google Colab. The goal was to identify invalid entries, handle outliers, and produce a reliable dataset suitable for analysis and visualization.
### Tasks

The Pulse column was first examined to understand its structure and identify inconsistencies such as non-numeric entries (e.g., “error”) and extreme values like 0 and 300. It was then converted from an object type to a numeric format using pd.to_numeric(errors='coerce'), which automatically replaced invalid values with NaN. After conversion, the data was explored using descriptive statistics, a histogram (with 10-bpm bins), and a box plot to understand the distribution and highlight outliers. Based on clinical reasoning, valid pulse values were defined as 50–250 bpm, and values outside this range were treated as invalid. These outliers, along with existing NaN values, were replaced using median imputation to reduce the influence of extreme values while preserving overall data structure. After cleaning, the Pulse column showed a more realistic distribution with no missing values and significantly reduced extreme outliers.
The GCS, SBP, and Temperature columns were cleaned by first converting all values to numeric format and handling non-numeric entries by replacing them with NaN. Each variable was then explored using histograms and box plots to identify invalid or out-of-range values based on clinical expectations (GCS: 3–15, SBP: 50–250, Temp: 32–43°C after standardisation). These invalid values were removed and replaced using median imputation to ensure a consistent and realistic dataset suitable for analysis.

**Process:**
1. Identified inconsistencies (non-numeric entries like "error", extreme values like 0 and 300)
2. Converted to numeric format using `pd.to_numeric(errors='coerce')`
3. Explored data distribution using:
   - Descriptive statistics
   - Histogram (10-bpm bins)
   - Box plot
4. Defined valid range: **50–250 bpm** (based on clinical reasoning)
5. Replaced outliers and NaN values using **median imputation**
**Outcome:** A realistic Pulse distribution with no missing values and minimal outliers.

---
## Assignment 3: Clinical Data Visualisation  
### Overview

This task focused on creating meaningful visualisations from the cleaned Emergency Triage dataset using Python and Matplotlib in Google Colab. The goal was to explore clinically relevant patterns in patient vital signs and better understand distributions and relationships within the data.

### Tasks

This assignment focused on creating clinically meaningful visualisations from the cleaned Emergency Triage dataset using Python and Matplotlib in Google Colab. A histogram was used to examine the distribution of patient pulse rates and identify whether most values fell within normal or abnormal clinical ranges, with reference zones added for low (<60 bpm) and high (>100 bpm) pulse rates. A scatter plot was also created to explore the relationship between patient age and respiratory rate (RR), with reference lines showing the normal adult respiratory rate range (12–20 bpm). These visualisations helped highlight patterns, identify abnormal observations, and improve interpretation of the clinical data.

A scatter plot was also created to explore the relationship between patient age and respiratory rate (RR), helping assess whether respiratory rate patterns varied across different age groups in emergency department patients. Horizontal reference lines were added to indicate the typical adult respiratory rate range (12–20 breaths per minute), providing clinical context for identifying potentially abnormal observations. These visualisations helped transform cleaned data into interpretable insights suitable for clinical analysis.

**Process:**  
1. Selected clinically relevant variables from the cleaned dataset  
2. Created a histogram to visualise the distribution of Pulse values  
3. Added clinical reference zones and threshold lines for abnormal pulse ranges (<60 bpm and >100 bpm)  
4. Created a scatter plot to analyse the relationship between Age and Respiratory Rate (RR)  
5. Added clinical reference lines for normal respiratory rate values (12–20 bpm)  
6. Labelled axes, titles, and legends clearly to improve readability and interpretation  
7. Saved the generated plots as PNG image files for reporting and presentation purposes  

**Outcome:** Clear clinical visualisations showing pulse distribution patterns and the relationship between age and respiratory rate, with clinically meaningful annotations to support interpretation.

---
---

 
## Prerequisites
 
- **Python** ≥ 3.10
- **Jupyter Notebook** or **JupyterLab** (or Google Colab)
- **Required Python libraries:**
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
---
-Required libraries:
--pandas
--numpy
