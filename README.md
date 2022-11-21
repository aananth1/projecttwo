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

1. 7 day moving average different currencies, for example AUD and USD, GBP, INR.
2. Daily percentage change in Exchange rates.
3. General price trends (economic events)

<br/>

## Source datasets 
What datasets are you sourcing from?


### Exchange Rates API

- https://exchangeratesapi.io/

# Architecture
![ProjectTwp](https://user-images.githubusercontent.com/2142469/203002378-5c69ec87-044e-4e11-b778-4d43086fd0ca.svg)

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

## Extract and Load
Exchange Rates API connector is available in Airbyte. The data is extracted using credentials and loaded into the Bronze layer of Snowflake.
There are 3 raw tables conatining similar data. These are:
1. Exchange_Rates
2. Exchange_Rates_Rates
3. Exchange_Rates_SCD

The Exchange_Rates_SCD table conatins data such as Base currency, Date, Rates, etc at Daily level. 

![Bronze](https://user-images.githubusercontent.com/2142469/203020403-6c0a0389-d152-4bfc-ab15-1017b26b8fff.png)

## Transformation

### Silver
The Exchange_Rates_SCD tables data is incrementally ingested into the silver at daily interval. Here the data is unpacked from the JSON format for the prices and stored in individual columns for the required currencies. This table contains data such as Base, date, AUD_Daily_Price, BTC_Daily_price, etc.

![Silver](https://user-images.githubusercontent.com/2142469/203020657-28e918d3-b83d-40b4-94e3-cfb18ffef1da.png)


### Gold

Thge Gold layer tables is a full-refresh table. The transformations done at this stage are:
1. All other currencies were dropped except AUD.
2. A new column was created based on the 7 day rolling average.
3. Another new column was created to calculate daily price changes. 
4. Only Active records are used for the calcuations (where row_active_ind = 1)

![Gold](https://user-images.githubusercontent.com/2142469/203020694-f7c01a69-9385-47ae-b5ec-a10c36779d88.png)

## DBT Docs


![dbt-dag](https://user-images.githubusercontent.com/2142469/203021318-ec8fb41f-de0f-493e-a023-31130a1ed7fc.png)


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
Snowflake. 

# Lessons Learnt

1. Make sure your Docker Images are not cooked.


<br/>
