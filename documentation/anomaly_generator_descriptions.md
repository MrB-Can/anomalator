# Anomaly Generator Descriptions

## Introduction
The following document provides descriptions for various types of anomalies that can be generated. Each anomaly corresponds to a specific data quality dimension and provides instructions for creating anomaly generators to simulate and inject anomalies into datasets. These anomaly generators can assist in testing data quality tools and simulating anomalous conditions for system behavior analysis.

## Sudden Drop in Data
This anomaly refers to a sudden lack of incoming data. For example, if you are collecting data every minute and suddenly you stop receiving data for an hour. This could be caused by various issues like network problems, issues with the data provider, or bugs in your data collection code.

## Unexpected Increase in Data Volume
This anomaly refers to a sudden surge in the volume of incoming data, which could potentially overwhelm your systems or lead to increased processing times. It could be caused by issues like errors in data generation or changes in user behavior.

## Unusual Distribution Shifts
This anomaly refers to when the distribution of a variable significantly shifts. For example, a variable that is usually normally distributed suddenly becomes heavily skewed.

## Inconsistencies in Data Associations
This anomaly refers to when the usual correlation or association between two or more variables changes suddenly. For example, if two variables are usually strongly correlated, and suddenly this correlation weakens or disappears.

## Changes in Data Trend
This anomaly refers to an unexpected change in the trend of a variable. For example, a variable that was steadily increasing suddenly starts decreasing.

## Inconsistent Capitalization or Formatting in Text Fields
This anomaly refers to inconsistencies in text field formatting, such as a mix of uppercase and lowercase entries, a mix of abbreviated and full versions of the same word, etc.

## Missing Values (null) in a Column
**Description:** This anomaly involves introducing missing values (null) in a specific column of a dataset. The generated anomaly generator should target a chosen column and replace a certain percentage of its values with null.

**Anomaly Generator Instructions:**
- Select the target dataset.
- Choose the column for introducing missing values.
- Determine the percentage of values in the column to replace with null.
- Implement the anomaly generator to modify the dataset accordingly.

## Duplicate Values in a Column
**Description:** This anomaly focuses on creating duplicate values in a column. The generated anomaly generator should identify a column and introduce duplicate entries, replicating existing values within the same column.

**Anomaly Generator Instructions:**
- Identify the dataset and the target column.
- Determine the percentage of duplicate entries to introduce.
- Implement the anomaly generator to duplicate values in the specified column.

## Outliers in Numeric Distributions
**Description:** This anomaly involves generating outliers in numeric distributions within a dataset. The anomaly generator should identify numeric columns and generate extreme values that lie outside the normal distribution range.

**Anomaly Generator Instructions:**
- Select the dataset and the numeric columns to target.
- Choose the method for generating outliers (e.g., random extreme values, statistical deviation).
- Determine the percentage of outliers to generate in each column.
- Implement the anomaly generator to introduce outliers in the numeric distributions.

## Unexpected Variance in Numeric Values
**Description:** This anomaly focuses on introducing unexpected variance in numeric values. The anomaly generator should modify the numeric values in a column to deviate significantly from their typical range or pattern.

**Anomaly Generator Instructions:**
- Identify the dataset and the target numeric column.
- Choose the method for introducing variance (e.g., random variation, mathematical transformations).
- Determine the degree of variance or the range of acceptable deviation.
- Implement the anomaly generator to introduce unexpected variance in the numeric column.

## Skewed Distribution in Numeric Values
**Description:** This anomaly aims to create skewed distributions in numeric values within a dataset. The anomaly generator should modify the distribution of values in a numeric column to exhibit a significant skewness.

**Anomaly Generator Instructions:**
- Select the dataset and the numeric column to skew.
- Choose the type of skewness (left-skewed or right-skewed).
- Determine the degree of skewness or the range of skewness coefficient.
- Implement the anomaly generator to skew the distribution of values in the numeric column.

## Unusual Kurtosis in Numeric Values
**Description:** This anomaly involves generating unusual kurtosis in numeric values. The anomaly generator should modify the distribution of values in a numeric column to exhibit a higher or lower kurtosis than expected.

**Anomaly Generator Instructions:**
- Identify the dataset and the target numeric column.
- Choose the type of kurtosis (excess kurtosis, positive or negative).
- Determine the degree of kurtosis or the acceptable range of kurtosis coefficient.
- Implement the anomaly generator to modify the kurtosis of the numeric column.

## Invalid UUID Format in a Column
**Description:** This anomaly focuses on introducing invalid UUID format in a specific column. The anomaly generator should identify the column containing UUID values and replace them with invalid UUIDs.

**Anomaly Generator Instructions:**
- Select the dataset and the column with UUID values.
- Determine the percentage of UUID values to modify.
- Implement the anomaly generator to replace valid UUIDs with invalid ones.

## Invalid Perm ID Format in a Column
**Description:** This anomaly involves generating invalid Perm ID format in a specific column. The anomaly generator should identify the column containing Perm IDs and replace them with incorrect or invalid formats.

**Anomaly Generator Instructions:**
- Identify the dataset and the column with Perm ID values.
- Determine the percentage of Perm ID values to modify.
- Implement the anomaly generator to replace valid Perm IDs with invalid formats.

## Invalid Social Security Number Format in a Column
**Description:** This anomaly focuses on creating invalid Social Security Number formats in a specific column. The anomaly generator should identify the column with Social Security Number values and introduce incorrect or invalid formats.

**Anomaly Generator Instructions:**
- Select the dataset and the column with Social Security Number values.
- Determine the percentage of Social Security Number values to modify.
- Implement the anomaly generator to replace valid formats with invalid ones.

## Invalid USA Phone Number Format in a Column
**Description:** This anomaly involves generating invalid USA phone number formats in a specific column. The anomaly generator should identify the column containing phone numbers and introduce incorrect or invalid formats.

**Anomaly Generator Instructions:**
- Identify the dataset and the column with phone number values.
- Determine the percentage of phone number values to modify.
- Implement the anomaly generator to replace valid phone number formats with invalid ones.

---

These descriptions provide guidance for creating anomaly generators to simulate and inject various anomalies into datasets. By following the instructions for each anomaly, we can create anomaly generators that facilitate data quality testing and analysis of system behavior under anomalous conditions.

# Additional Anomalies List

Introduction:
In addition to the previously described anomaly generators, here is a list of 90 more anomalies that can be generated using our system. These anomalies cover various data quality dimensions and provide opportunities for simulating and injecting anomalous conditions into datasets.

List of Anomalies:
1. Anomaly: Missing timestamp values in a column.
2. Anomaly: Unexpected values in categorical variables.
3. Anomaly: Data inconsistencies between related tables.
4. Anomaly: Invalid email addresses in a column.
5. Anomaly: Data truncation or data loss during data migration.
6. Anomaly: Fluctuating data quality metrics over time.
7. Anomaly: Introducing duplicate records across tables.
8. Anomaly: Introducing incorrect foreign key relationships.
9. Anomaly: Inconsistent data formats for date/time values.
10. Anomaly: Data entry errors or typos in text fields.
11. Anomaly: Introducing missing or incomplete metadata.
12. Anomaly: Introducing corrupted or unreadable file formats.
13. Anomaly: Inconsistent units of measurement in numeric values.
14. Anomaly: Introducing incorrect or outdated reference data.
15. Anomaly: Shuffling or randomizing data order in a column.
16. Anomaly: Unusual patterns or anomalies in geolocation data.
17. Anomaly: Data discrepancies between production and backup systems.
18. Anomaly: Introducing outliers in textual data fields.
19. Anomaly: Inconsistent or unexpected data patterns in time series.
20. Anomaly: Introducing data inconsistencies across data partitions.
21. Anomaly: Swapping or mislabeling categorical values.
22. Anomaly: Introducing errors in calculated or derived columns.
23. Anomaly: Inconsistent data normalization across tables.
24. Anomaly: Introducing incorrect or misleading data labels.
25. Anomaly: Introducing data gaps or intervals in time series.
26. Anomaly: Data discrepancies between different data sources.
27. Anomaly: Introducing biases or skewness in data sampling.
28. Anomaly: Inconsistent encoding or character set in textual data.
29. Anomaly: Introducing missing or corrupted image files.
30. Anomaly: Data discrepancies between different versions of the same dataset.
31. Anomaly: Introducing unusual patterns or anomalies in network traffic data.
32. Anomaly: Inconsistent or unexpected data patterns based on data indexing or partitioning strategies.
33. Anomaly: Introducing data discrepancies or inconsistencies between compression algorithms.
34. Anomaly: Introducing unusual patterns or anomalies in data encryption.
35. Anomaly: Inconsistent handling of missing data across different data processing stages.
36. Anomaly: Introducing incorrect or misleading data annotations or labels.
37. Anomaly: Inconsistent or unexpected patterns in data deduplication processes.
38. Anomaly: Introducing outliers or anomalies in sentiment analysis scores.
39. Anomaly: Inconsistent or unexpected patterns in data anonymization or pseudonymization.
40. Anomaly: Introducing incorrect or misleading data transformations.
41. Anomaly: Inconsistent or unexpected patterns in data summarization or aggregation.
42. Anomaly: Introducing data discrepancies or inconsistencies in data replication processes.
43. Anomaly: Inconsistent or unexpected patterns in machine learning model predictions.
44. Anomaly: Introducing missing or corrupted audio files.
45. Anomaly: Inconsistent or unexpected patterns in natural language processing outputs.
46. Anomaly: Introducing incorrect or misleading data imputation techniques.
47. Anomaly: Inconsistent or unexpected patterns in data clustering or segmentation results.
48. Anomaly: Introducing data discrepancies or inconsistencies in data merging or joining processes.
49. Anomaly: Inconsistent or unexpected patterns in data discretization or binning outputs.
50. Anomaly: Introducing incorrect or misleading data filtering or selection criteria.
51. Anomaly: Inconsistent or unexpected patterns in data standardization or normalization outputs.
52. Anomaly: Introducing data discrepancies or inconsistencies in data transformation pipelines.
53. Anomaly: Inconsistent or unexpected patterns in data feature extraction or engineering outputs.
54. Anomaly: Introducing incorrect or misleading data scaling or rescaling techniques.
55. Anomaly: Inconsistent or unexpected patterns in data augmentation or synthesis outputs.
56. Anomaly: Introducing data discrepancies or inconsistencies in data augmentation pipelines.
57. Anomaly: Inconsistent or unexpected patterns in data splitting or partitioning outputs.
58. Anomaly: Introducing incorrect or misleading data sampling or stratification techniques.
59. Anomaly: Inconsistent or unexpected patterns in data shuffling or randomization outputs.
60. Anomaly: Introducing data discrepancies or inconsistencies in data sampling pipelines.
61. Anomaly: Inconsistent or unexpected patterns in data balancing or rebalancing outputs.
62. Anomaly: Introducing incorrect or misleading data weighting or importance techniques.
63. Anomaly: Inconsistent or unexpected patterns in data ensemble or fusion outputs.
64. Anomaly: Introducing data discrepancies or inconsistencies in data ensemble pipelines.
65. Anomaly: Inconsistent or unexpected patterns in data dimensionality reduction outputs.
66. Anomaly: Introducing incorrect or misleading data feature selection or extraction techniques.
67. Anomaly: Inconsistent or unexpected patterns in data classification or prediction outputs.
68. Anomaly: Introducing data discrepancies or inconsistencies in model training processes.
69. Anomaly: Inconsistent or unexpected patterns in model evaluation or validation outputs.
70. Anomaly: Introducing incorrect or misleading hyperparameter tuning techniques.
71. Anomaly: Inconsistent or unexpected patterns in model deployment or inference outputs.
72. Anomaly: Introducing data discrepancies or inconsistencies in model deployment pipelines.
73. Anomaly: Inconsistent or unexpected patterns in model monitoring or drift detection outputs.
74. Anomaly: Introducing incorrect or misleading anomaly detection techniques.
75. Anomaly: Inconsistent or unexpected patterns in anomaly detection or outlier detection outputs.
76. Anomaly: Introducing data discrepancies or inconsistencies in anomaly detection pipelines.
77. Anomaly: Inconsistent or unexpected patterns in fraud detection or cybersecurity outputs.
78. Anomaly: Introducing incorrect or misleading data privacy or protection techniques.
79. Anomaly: Inconsistent or unexpected patterns in data privacy or protection outputs.
80. Anomaly: Introducing data discrepancies or inconsistencies in data privacy pipelines.
81. Anomaly: Inconsistent or unexpected patterns in data governance or compliance outputs.
82. Anomaly: Introducing incorrect or misleading data quality assessment techniques.
83. Anomaly: Inconsistent or unexpected patterns in data quality assessment outputs.
84. Anomaly: Introducing data discrepancies or inconsistencies in data quality pipelines.
85. Anomaly: Inconsistent or unexpected patterns in data profiling or metadata management outputs.
86. Anomaly: Introducing incorrect or misleading data integration or data synchronization techniques.
87. Anomaly: Inconsistent or unexpected patterns in data integration or data synchronization outputs.
88. Anomaly: Introducing data discrepancies or inconsistencies in data integration pipelines.
89. Anomaly: Inconsistent or unexpected patterns in data visualization or reporting outputs.
90. Anomaly: Introducing incorrect or misleading data visualization or reporting techniques.

---

This list provides a wide range of additional anomalies that can be generated for simulating and injecting anomalous conditions into datasets. Each anomaly presents opportunities for data quality testing, system behavior analysis, and anomaly detection.

