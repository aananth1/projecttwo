from airflow.models import Variable
import json
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash import BashOperator

with DAG(dag_id='trigger_exchangerate_ingestion',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
    ) as dag:

    exch_to_snowflake = AirbyteTriggerSyncOperator(
        task_id='exch_to_snowflake',
        airbyte_conn_id='airbyte_exchangerates',
        connection_id='a8cb1628-03af-456b-9dbb-e04b0e94128a',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    dbt_version = BashOperator(
        task_id="dbt_version",
        bash_command="<path to /bin/dbt on your airflow's dbt environment> --version",
    )

    dbt_env_json = Variable.get("DBT_ENV")

    dbt_build = BashOperator(
        task_id="dbt_build",
        env=json.loads(dbt_env_json),
        bash_command="cp -R <full path to dbt folder (which contains the ExchangeRates dbt project) in your airflow storage> /tmp;\
        cd /tmp/dbt/ExchangeRates;\
        <path to /bin/dbt on your airflow's dbt environment> deps;\
        <path to /bin/dbt on your airflow's dbt environment> build --project-dir /tmp/dbt/ExchangeRates/ --profiles-dir . --target prod;\
        cat /tmp/dbt/ExchangeRates/logs/dbt.log;\
        cp /tmp/dbt/ExchangeRates/logs/dbt.log <full path to dbt.log in your airflow storage>/~airflow/airflow/dags/dbt/ExchangeRates/logs/dbt.log"
    )

exch_to_snowflake >> dbt_version >> dbt_build