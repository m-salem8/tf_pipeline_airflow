# Facial Expression Recognition with Deep Learning

## Project Overview

This project showcases my skills in data engineering and data science by creating a deep learning model for facial expression recognition. The objective is to accurately categorize facial expressions into seven distinct classes: Angry, Disgust, Fear, Happy, Sad, Surprise, and Neutral.

## Data Description

- **Dataset:** A dataset of 24,400 images, with 22,968 images for training and 1,432 images for public testing.
- **Data Source:** Accessed via Kaggle API.

## Data Preparation

Data was prepared using Keras' `ImageDataGenerator` for data augmentation, enhancing the model's ability to generalize from the training data.

## Model

A Convolutional Neural Network (CNN) architecture was used for image classification. The model was designed with convolutional layers, batch normalization, max-pooling, dropout, and dense layers to achieve accurate facial expression recognition.

## Airflow Orchestration

- Apache Airflow was employed for data ingestion, validation, preprocessing, and model training, creating an automated workflow from data acquisition to model evaluation.
- Implementation through docker-compose **(add details to the architecture)**

## Challenges Faced

- Deployment to Heroku (tensorflow is around 500MB which goes above Heroku’s max limit)
- Model is very slow to run
- Timeout connection between containers when running the model

## Improvement points

- Implementing the app on AWS instead of Heroku
- Optimize tensorflow parameters
- Creating an airflow image from scratch to decrease the time downloading dependencies

## Details about Dockerfile

- This Dockerfile customizes an Apache Airflow image by updating system packages and upgrading pip while maintaining Kaggle API credentials for access within the container. It ensures a prepared environment for running Apache Airflow tasks and workflows with external data source integration.
- This image is exported to Docker hub to be used in docker-compose

## Details about Docker-compose

1. It uses the official Airflow image created in the docker file and extends it with custom environment variables, volumes, and dependencies. This environment is configured to handle ML projects, including dependencies like TensorFlow, Keras, and more, as specified in **`_PIP_ADDITIONAL_REQUIREMENTS`**.
2. It sets up a PostgreSQL database container for Airflow's metadata and a Redis container for Celery as the message broker.
3. The **`airflow-init`** service initializes the Airflow database and creates an initial admin user if needed.
4. The **`airflow-webserver`**, **`airflow-scheduler`**, and **`airflow-worker`** services run the core components of Apache Airflow. The **`airflow-webserver`** exposes the Airflow web interface on port 8080, **`airflow-scheduler`** schedules and triggers workflows, and **`airflow-worker`** performs task execution.
5. The **`flower`** service runs a web-based tool for monitoring the Celery workers.

## Running the project

- In docker-compose, insert your KAGGLE_USERNAME and KAGGLE_KEY in order to authenticate to Kaggle’s API
- Make sure that no other containers are running Airflow as this might lead to confusion.
- Run docker-compose airflow-init
- Run docker-compose up -d. Wait until containers run in healthy mode.
- Access Airflow [localhost:8080](http://localhost:8080) where you can run the ML model