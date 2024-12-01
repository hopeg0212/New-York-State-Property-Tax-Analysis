# CTA Bus Ridership Daily Trends Analysis

## Company Description
The Chicago Transit Authority (CTA) is the second-largest public transportation system in the U.S., serving the city of Chicago and its surrounding suburbs. CTA strives to provide reliable, efficient, and accessible transit services to enhance the quality of life in the Chicago area.

## Business Problem / Problem Statement
The CTA aims to utilize detailed daily ridership data to optimize bus route schedules, improve service frequency, and enhance passenger experiences by understanding patterns across different routes and times.

## Functional Requirements
1. **Ridership Analysis:** Explore daily ridership figures by route to identify trends and demand cycles.
2. **Peak Traffic Identification:** Analyze traffic to determine high-demand periods across routes.
3. **Service Optimization:** Use data insights to propose adjustments that improve efficiency and meet passenger needs.
4. **Compliance and Reporting:** Ensure data accuracy and privacy in reporting, adhering to regulatory standards.

## Data Requirements
- **Data Source:** CTA Ridership - Bus Routes - Daily Totals by Route, sourced from https://catalog.data.gov/dataset/cta-ridership-bus-routes-daily-totals-by-route
- **Characteristics:** Includes detailed entries of daily bus route usage, necessary for comprehensive service analysis.

## Data Collection Methodology
This dataset captures daily ridership metrics, reflecting passenger counts and route utilization. The data is gathered from electronic ticketing data and validated against manual counts for accuracy.

## Business Impact
By analyzing this data, the CTA can:
- Enhance route planning based on actual usage patterns.
- Adjust schedules to better align with passenger demand peaks.
- Improve resource allocation, thereby increasing operational efficiency and passenger satisfaction.

## Project Structure
- **Data Sourcing:** Automated scripts fetch and store data daily from designated repositories.
- **Data Transformation:** Use dbt to standardize and clean the data, ensuring it is analysis-ready.
- **Data Modeling:** Construct a data warehouse in AWS Redshift, organizing data into dimensional models for efficient querying.
- **Data Analysis and Reporting:** Develop dynamic dashboards in Tableau to visualize trends and support decision-making processes.

## Technologies Used
- **Data Storage and Transformation:** AWS S3, dbt
- **Data Warehousing:** AWS Redshift
- **Data Visualization:** Tableau
- **Scripting and Automation:** Python, SQL

