# Project: Anomaly Generators

## Overview

This project is focused on the development of a series of anomaly generators, designed to inject different types of anomalies into datasets. The main objective of these anomaly generators is to facilitate testing of data quality tools, as well as simulating anomalous conditions for system behavior analysis.

Our anomaly generators have been designed to produce different kinds of anomalies. These include missing values in a column, duplicate values in a column, outliers in numeric distributions, unexpected variance in numeric values, skewed distribution in numeric values, unusual kurtosis in numeric values, and invalid UUID formats in a column.

## Anomaly Generators

The following anomaly generators have been developed:

1. **Missing Values (null) in a Column:** This generator introduces missing values (null) in a specific column of a dataset.

2. **Duplicate Values in a Column:** This generator creates duplicate values in a column.

3. **Outliers in Numeric Distributions:** This generator introduces outliers in numeric distributions within a dataset.

4. **Unexpected Variance in Numeric Values:** This generator introduces unexpected variance in numeric values.

5. **Skewed Distribution in Numeric Values:** This generator creates skewed distributions in numeric values within a dataset.

6. **Unusual Kurtosis in Numeric Values:** This generator introduces unusual kurtosis in numeric values.

7. **Invalid UUID Format in a Column:** This generator introduces invalid UUID format in a specific column.

Detailed descriptions and instructions for each anomaly generator can be found in the 'Anomaly Generator Descriptions' document.

## Usage

To use these generators, select the desired generator and provide it with your dataset and the necessary parameters such as target columns, percentage of anomalies, type of skewness, kurtosis, and others as specified by the respective generator.

The generator will then modify the dataset to inject the desired anomalies.

## Contributions

This project is open for contributions. If you want to add new types of anomaly generators or have suggestions to improve the existing ones, please feel free to open an issue or submit a pull request.

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any queries or suggestions, please contact us at [Email](mailto:[paul@lgis.ca]).