# projecttwo
DE Bootcamp Project Two

# Exchange Rates ETL with AirByte, DBT & Snowflake

# Project plan 

## Objective 
What would you like people to do with the data you have produced? Are you supporting BI or ML use-cases? 

<blockquote>The goal is provide exchange rate data for BI purposes.</blockquote>

<br/>

## Consumers 
What users would find your data useful?

<blockquote>Investment bankers.</blockquote>

<br/>

## Questions 
What questions are you trying to solve with your data? 

1. Correlation between different currencies, for example AUD and USD, GBP, INR.
2. General price trends (economic events)

<br/>

## Source datasets 
What datasets are you sourcing from?


### Exchange Rates API

- https://exchangeratesapi.io/

# Project structure

```text
├── AirflowDAGs
├── Data Integration
├── docker
├── ExchangeRates
│   ├── analyses
│   ├── dbt_packages
│   │   └── dbt_utils
│   │       ├── docs
│   │       │   └── decisions
│   │       ├── etc
│   │       ├── integration_tests
│   │       │   ├── ci
│   │       │   ├── data
│   │       │   │   ├── cross_db
│   │       │   │   ├── datetime
│   │       │   │   ├── etc
│   │       │   │   ├── geo
│   │       │   │   ├── materializations
│   │       │   │   ├── schema_tests
│   │       │   │   ├── sql
│   │       │   │   └── web
│   │       │   ├── macros
│   │       │   ├── models
│   │       │   │   ├── cross_db_utils
│   │       │   │   ├── datetime
│   │       │   │   ├── generic_tests
│   │       │   │   ├── geo
│   │       │   │   ├── materializations
│   │       │   │   ├── sql
│   │       │   │   └── web
│   │       │   └── tests
│   │       │       ├── generic
│   │       │       ├── jinja_helpers
│   │       │       └── sql
│   │       ├── macros
│   │       │   ├── cross_db_utils
│   │       │   │   └── deprecated
│   │       │   ├── generic_tests
│   │       │   ├── jinja_helpers
│   │       │   ├── materializations
│   │       │   ├── sql
│   │       │   └── web
│   │       └── tests
│   │           └── functional
│   │               ├── cross_db_utils
│   │               └── data_type
│   ├── logs
│   ├── macros
│   ├── models
│   │   ├── Gold
│   │   └── Silver
│   ├── seeds
│   ├── snapshots
│   └── tests
└── logs
```

<br/>

## Technical Details
# Extraction Source
Exchange Rates API

# Destination
Snowflake

# Data integration tool
Airbyte

# Transformations
Snowflake

# Creation of dependencies
DBT

# Scheduling of tasks
Airflow

## DAG
The Airflow DAG allows you to orchestrate the ingestion via AIrflow including querying via API & loading data to Snowflake (via connection to Airbyte) and execute the ExchangeRates DBT Project on the Snowflake data to promote data to Silver & Gold.

## DAG Instructions
Fill in blanks in code as indicated in the file. See example below for guidance.
Add dag_exchangerates.py to your Airflow DAG folder.

![123123123123](https://user-images.githubusercontent.com/106643739/202979111-b3857dbc-203e-4df4-bba5-5762e6cdc610.png)

## DAG Assumptions
* Working Airflow environment with DBT setup and working as a sub-environment.
* AirByte running locally or dockerized + locally on port 8000. If dockerized locally, set server=host.docker.internal. If hosted locally, use server=localhost. If cloud-hosted, use appropriate IP address based on configuration.

## Airflow DAG Results

![shot_221121_172111](https://user-images.githubusercontent.com/106643739/202979366-4d5cd3e7-6978-455a-a7ba-becab04f599d.png)

# Hosting
Cloud - AWS, Snowflake. 

# Architecture
![ProjectTwp](https://user-images.githubusercontent.com/2142469/203002378-5c69ec87-044e-4e11-b778-4d43086fd0ca.svg)

<br/>
