# Anomaly Generator Software - Software Requirement Specification (SRS)

## Table of Contents
1. Introduction
2. System Features
3. Functional Requirements
4. Non-Functional Requirements
5. Performance Criteria
6. Security Considerations
7. Design Constraints

## 1. Introduction
The Anomaly Generator software is a robust tool designed to assist organizations in testing their data quality tools and simulating how their systems behave under anomalous conditions. This software tool enables users to inject a wide range of anomalies into databases, covering three main areas: pipeline reliability, data quality, and business insights. By generating anomalies, users can evaluate the effectiveness of their data quality tools and infrastructure resilience.

## 2. System Features
The Anomaly Generator software provides the following key features:
- Pipeline Reliability Anomalies: Allows users to simulate anomalies related to the reliability of data pipelines, such as delayed data updates, unexpected data volumes, and monitoring data freshness.
- Data Quality Anomalies: Enables users to introduce anomalies related to data quality, including variations in numeric distributions, string format changes, null value percentage fluctuations, and date format inconsistencies.
- Business Insights Anomalies: Supports the generation of anomalies that reflect changes in the data, highlighting significant business-related or external events that may impact data analytics and decision-making.

## 3. Functional Requirements
The functional requirements of the Anomaly Generator software are as follows:

### Connection and Data Selection
- Users should be able to establish connections to databases by providing connection details such as hostname, port, username, password, and database name.
- The software should allow users to browse the available tables and columns in the selected database and select the target tables/columns for anomaly injection.
- Important information about the selected tables, such as the minimum and maximum dates, record count, and daily record distribution, should be displayed to assist users in making informed decisions.

### Database Connectivity
- The software should support various database systems, including but not limited to MySQL, PostgreSQL, Oracle, and SQL Server.
- It should provide the necessary connectivity libraries and drivers to establish secure and reliable connections to the selected databases.
- Robust error handling and logging mechanisms should be implemented to capture and report any connectivity issues or exceptions.

### Anomaly Selection
- Users should have the ability to choose from a predefined list of anomaly types suitable for each selected column. Anomalies can be categorized based on their impact on pipeline reliability, data quality, or business insights.
- The software should provide clear descriptions and explanations of each anomaly type to help users understand their effects and implications.

### Anomaly Parameters
- Each anomaly type should have default parameter values, including frequency, volume, amplitude, and duration, which define the characteristics of the anomaly.
- Users should be able to modify these parameter values according to their specific requirements, allowing customization of the anomalies.

### Execution Options
- The software should support both periodic runs and one-time injections. Users can schedule periodic runs to simulate recurring anomalies, or perform one-time injections to introduce anomalies for a specific time period.
- For periodic runs, users should be able to set the frequency and duration of the anomaly occurrences.

### Warning and Security Measures
- Users should be provided with clear and prominent warnings about the potentially destructive nature of the anomaly injection process.
- Confirmation prompts or additional authentication steps should be implemented to ensure that users fully understand the implications and consequences of applying the anomalies.
- Customer credentials and sensitive information should be securely stored, adhering to best practices and utilizing services like AWS Secrets Manager or similar secure storage solutions.

## 4. Non-Functional Requirements
The non-functional requirements of the Anomaly Generator software are as follows:

### Performance
- The software should be designed to consume minimal resources, ensuring optimal performance and efficiency.
- It should be able to handle a reasonable number of concurrent database connections and perform anomaly injection within acceptable time frames.

### Reliability and High Availability
- While the software should be reliable, there are no specific high availability (HA) requirements.
- Proper error handling, fault tolerance, and recovery mechanisms should be implemented to handle unexpected failures gracefully and minimize downtime.

### User Targeting
- The software should primarily target data engineers and individuals with a good operating knowledge of the selected database systems.
- User-friendly interfaces and intuitive workflows should be provided, but advanced technical capabilities and understanding may be required to effectively utilize the software's features.

## 5. Performance Criteria
The performance criteria for the Anomaly Generator software are as follows:
- The software should be scalable and capable of generating anomalies for multiple customers simultaneously.
- It should be able to create anomalies for 10 different customers within one hour.
- The number of target tables can range from 3 to 50 for each customer.

## 6. Security Considerations
The security considerations for the Anomaly Generator software are as follows:

### Secure Storage of Customer Credentials
- Customer credentials, such as database connection details, should be securely stored using industry-standard encryption and secure storage solutions.
- Services like AWS Secrets Manager or similar technologies can be employed to store and manage sensitive information.

### Protection of Credentials
- Measures should be in place to prevent unauthorized access to customer credentials.
- Credentials should never be exposed to developers or customers in any way and should be kept confidential.

### Compliance with Security Standards
- The software should adhere to industry security standards, such as SOC2 guidelines, to ensure the confidentiality, integrity, and availability of customer data.

## 7. Design Constraints
The design constraints for the Anomaly Generator software are as follows:

### Flexibility in Technology Choices
- The software development should allow flexibility in technology choices, including programming languages, frameworks, and libraries, to best accommodate the needs of the project and leverage existing expertise within the development team.

### Open to Collaboration and Decision-Making
- Collaboration and joint decision-making among the development team and stakeholders are encouraged to ensure the software meets the desired objectives and fulfills customer requirements.

