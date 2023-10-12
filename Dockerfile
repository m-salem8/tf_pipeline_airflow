# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.1.1
# Set user to root for installations
USER root
# Update the system
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*
# Update the PATH to include /root/.local/bin
ENV PATH="/root/.local/bin:${PATH}"
# Upgrade pip to the latest version
RUN pip install --upgrade pip
# If you have any Python requirements, copy the requirements file and install them
COPY requirements.txt /home/
RUN pip install --default-timeout=300 --no-cache-dir -r /home/requirements.txt
# Copy your Kaggle API key to the appropriate locations in the container
COPY .kaggle/ /home/airflow
# Switch back to the airflow user for running Airflow
USER airflow