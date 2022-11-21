# Airflow DAG
This Airflow DAG allows you to orchestrate the ingestion via AIrflow including querying via API & loading data to Snowflake (via connection to Airbyte) and execute the ExchangeRates DBT Project on the Snowflake data to promote data to Silver & Gold.

# Instructions
Fill in blanks in code as indicated in the file. See example below for guidance.
Add dag_exchangerates.py to your Airflow DAG folder.

![123123123123](https://user-images.githubusercontent.com/106643739/202979111-b3857dbc-203e-4df4-bba5-5762e6cdc610.png)

# Assumptions
* Working Airflow environment with DBT setup and working as a sub-environment.
* AirByte running locally or dockerized + locally on port 8000. If dockerized locally, set server=host.docker.internal. If hosted locally, use server=localhost. If cloud-hosted, use appropriate IP address based on configuration.

# Results

![shot_221121_172111](https://user-images.githubusercontent.com/106643739/202979366-4d5cd3e7-6978-455a-a7ba-becab04f599d.png)
