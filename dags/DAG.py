from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import XCom
from airflow.models import Variable
from _01_data_ingestion import load_data
from _02_data_validation import validate_data
from _03_data_preprocessing import preprocess_data
from _04_model_training import process_train_save
import os 


############################### DAG Definition ########################################
my_dag=DAG(
    dag_id='tf_pipeline',
    description='tf_pipline orchestration',
    tags=['tf_pipeline'],
    schedule_interval= None,
    default_args={
        'owner':'airflow', 
        'start_date': days_ago(0, minute=1)
    },
    catchup=False
)

################################ TASKS ##########################################

kaggle_key = os.environ.get('KAGGLE_KEY')
user_name = os.environ.get("KAGGLE_USERNAME")

task_1= PythonOperator(
    task_id='data_ingestion',
    dag=my_dag,
    python_callable = load_data,
    retries=5,
    retry_delay=timedelta(seconds = 15)
)

task_2 = PythonOperator(
    task_id='data_validation',
    dag=my_dag,
    op_kwargs={"data": None},
    python_callable=validate_data
)

task_3 = PythonOperator(
    task_id='data_processing_training_save', 
    dag = my_dag,
    python_callable=process_train_save

)

task_1 >> task_2
task_2 >> task_3
