from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import XCom
from airflow.models import Variable

from _01_data_ingestion import load_data
from _02_data_validation import validate_data
from _03_data_preprocessing import preprocess_data
from _04_model_training import train_model, train_model, save_model
from _05_performance_evaluation import  evaluate_model
from _06_model_prediction import load_and_preprocess_image, predict

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
kaggle_key = Variable.get("KAGGLE_KEY")
kaggle_username = Variable.get("KAGGLE_USERNAME")


task_1= PythonOperator(
    task_id='data_ingestion',
    dag=my_dag,
    python_callable = load_data,
    op_args=[kaggle_username, kaggle_key],
    retries=5,
    retry_delay=timedelta(seconds = 15)
)


