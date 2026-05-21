# CariSurg MedTech Pathways — Week 0 
## Assignment 1
### Overview

This task cleans the Gender column in the Emergency Triage dataset using Python and Pandas in Google Colab.
### Tasks
This assignment focused on cleaning and standardizing the Gender column in the Emergency Triage dataset using Python and Pandas in Google Colab. The dataset was loaded from Google Drive, and the values in the Gender column were examined to identify inconsistent formats such as uppercase text and numeric strings. A mapping method was used to convert all male values to 1, all female values to 0 and all other values to 2, creating a clean and consistent dataset. After cleaning, the original column was removed, the cleaned column was renamed to Gender and the final dataset was verified to ensure there were no missing values.

## Assignment 2
### Overview

This task focused on cleaning and standardising the Pulse column in the Emergency Triage dataset using Python and Pandas in Google Colab. The goal was to identify invalid entries, handle outliers, and produce a reliable dataset suitable for analysis and visualization.
### Tasks
The Pulse column was first examined to understand its structure and identify inconsistencies such as non-numeric entries (e.g., “error”) and extreme values like 0 and 300. It was then converted from an object type to a numeric format using pd.to_numeric(errors='coerce'), which automatically replaced invalid values with NaN. After conversion, the data was explored using descriptive statistics, a histogram (with 10-bpm bins), and a box plot to understand the distribution and highlight outliers. Based on clinical reasoning, valid pulse values were defined as 50–250 bpm, and values outside this range were treated as invalid. These outliers, along with existing NaN values, were replaced using median imputation to reduce the influence of extreme values while preserving overall data structure. After cleaning, the Pulse column showed a more realistic distribution with no missing values and significantly reduced extreme outliers.
