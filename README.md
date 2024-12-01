# New York State Traffic Ticket Analysis

## Overview
This project analyzes traffic ticket data issued in New York State over a four-year period. It explores patterns and trends in traffic violations across different regions and times, providing insights that could help in traffic management and law enforcement efficiency.

## Company Description
The New York State Department of Motor Vehicles (NYSDMV) is responsible for vehicle registration, driver licensing, and the adjudication of traffic violations across New York State. The NYSDMV maintains a robust database of traffic tickets issued, which serves as a critical tool for law enforcement and public safety. By analyzing this comprehensive data, NYSDMV aims to enhance road safety, ensure compliance with traffic laws, and reduce traffic-related incidents.

## Business Problem / Problem Statement
The NYSDMV seeks to derive actionable insights from the vast amounts of traffic ticket data collected over the years. The objective is to analyze traffic violation patterns, identify high-risk areas, and understand the effectiveness of traffic law enforcement strategies. Insights from this analysis are intended to guide policy adjustments, improve traffic law enforcement, and ultimately enhance road safety across New York State.

## Functional Requirements
- **Violation Analysis:** Examine the distribution and frequency of traffic violations to identify common trends and outlier incidents.
- **Temporal Trends:** Investigate the variation in traffic tickets issued across different times of the day, days of the week, and seasons to determine peak periods of violations.
- **Geographic Insights:** Map out the geographic distribution of violations to pinpoint high-risk locations and zones of frequent incidents.
- **Demographic Correlations:** Analyze violator demographic data to assess correlations between violator profiles and types of violations.
- **Enforcement Effectiveness:** Evaluate the impact of enforcement strategies and the outcomes of traffic tickets on improving road safety.

## Data Requirements
- **Data Source:** Traffic Tickets Issued: Four Year Window dataset from New York State Open Data.
- **Data Characteristics:** The dataset contains detailed records of every traffic ticket issued, including date, location, violator demographics, and violation type.
- **Data Collection Methodology:** Data is collected at the point of issuance by law enforcement officers and compiled into the NYSDMV database. The dataset is updated periodically to reflect new data and changes.
- https://data.ny.gov/Transportation/Traffic-Tickets-Issued-Four-Year-Window/q4hy-kbtf/about_data
- https://data.ny.gov/api/views/q4hy-kbtf/files/C6gwPCdHCxpNxC0szKY_tXKFORek72pOffkDhBqgFXU?download=true&filename=NYSDMV_Ticket_Data_Overview.pdf
- https://data.ny.gov/api/views/q4hy-kbtf/files/YpjZeFFvj4Xc5kAgir7bkIx2GfhhKwfOpQUmKvrwWRE?download=true&filename=NYSDMV_OpenData_Tickets_DataDictionary.pdf

## Technologies Used
- **Data Storage and Transformation:** Utilizes PostgreSQL for data storage and dbt (Data Build Tool) for data transformation.
- **Data Analysis:** SQL for structured queries and data manipulation.
- **Visualization and Reporting:** PowerBI for dynamic, interactive dashboards and visualizations.



