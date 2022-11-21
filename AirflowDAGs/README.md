# Airflow DAG
This allows you to orchestrate the ingestion via API, load data to Snowflake and execute the ExchangeRates DBT Project on the Snowflake data to promote data to Silver & Gold.

# Instructions
Fill in blanks in code as indicated. See example below for guidance.
Add dag_exchangerates.py to your Airflow DAG folder.

# Assumptions
-Working Airflow environment with DBT setup and working as a sub-environment.
-AirByte running locally or dockerized + locally on port 8000. If dockerized locally, set server=host.docker.internal. If hosted locally, use server=localhost. If cloud-hosted, use appropriate IP address based on configuration.