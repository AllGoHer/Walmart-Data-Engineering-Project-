from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

@dag(
    dag_id='orchestrate',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['walmart', 'dbt']
)
def orchestrate():

    @task
    def ingest_cdc():
        return "CDC data ingested"

    clean_target = BashOperator(
        task_id='clean_target',
        bash_command='rm -rf /opt/airflow/walmart_project/target && rm -rf /opt/airflow/walmart_project/logs',
        cwd='/opt/airflow/walmart_project'
    )

    source_freshness = BashOperator(
        task_id='source_freshness',
        bash_command='dbt source freshness',
        cwd='/opt/airflow/walmart_project'
    )

    silver_technical = BashOperator(
        task_id='silver_technical',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select silver_t'
    )

    silver_technical_tests = BashOperator(
        task_id='silver_technical_tests',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt test --select silver_t'
    )

    silver_business = BashOperator(
        task_id='silver_business',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select silver_b'
    )

    silver_business_tests = BashOperator(
        task_id='silver_business_tests',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt test --select silver_b'
    )

    gold_eph = BashOperator(
        task_id='gold_ephemeral',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select gold'
    )

    gold_dimensions = BashOperator(
        task_id='gold_dimensions',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt snapshot'
    )

    gold_facts = BashOperator(
        task_id='gold_facts',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select gold/fact'
    )

    # Definir la dependencia
    ingest_cdc_task = ingest_cdc()
    
    # Cadena de ejecución
    ingest_cdc_task >> clean_target >> source_freshness >> silver_technical >> silver_technical_tests >> silver_business >> silver_business_tests >> gold_eph >> gold_dimensions >> gold_facts

orchestrate_dag = orchestrate()

