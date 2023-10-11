### 1. Kaggle API Key Setup
- Visit your Kaggle account settings page to generate an API key.
- Once generated, the key will be automatically downloaded as `kaggle.json`.

### 2. Setting Up the Environment

Execute the following commands in order:

```bash
# Clone the repository
git clone https://github.com/m-salem8/tf_pipeline.git

# Navigate to the project directory
cd tf-pipeline-airflow

# Update the docker-compose.yaml file with your Kaggle credentials
# Ensure to modify the 'environment' section:
# KAGGLE_USERNAME: <your_kaggle_username>
# KAGGLE_KEY: <your_kaggle_key>

# Start the initialization
docker-compose up airflow-init

# Bring up the Docker services
docker-compose up -d