# TensorFlow Face Classification Project

This project utilizes TensorFlow to train a machine learning model for face classification. The objective is to accurately categorize faces based on various expressions/emotions.

## Overview

Faces convey a wealth of information in our daily lives. With advancements in artificial intelligence and deep learning, it is now possible to train models that can interpret human faces and categorize them based on the displayed emotion. This project seeks to leverage TensorFlow's powerful capabilities to achieve this.

## Installation

1. **Kaggle API Key Setup**:
    - Go to your Kaggle account settings page to generate an API key.
    - Save the key, which will be downloaded as `kaggle.json`.
    - Set the Kaggle API key as environment variables:
    ```bash
    export KAGGLE_USERNAME=your_username
    export KAGGLE_KEY=your_key
    ```

2. **Setting up the Environment**:
    - Clone this repository:
    ```bash
    git clone https://github.com/m-salem8/tf_pipeline.git
    ```
    - Navigate to the project directory and install the required packages:
    ```bash
    cd tf_pipeline
    pip install -r requirements.txt
    ```

3. **Download the Training and Test Data**:
    - The data will be automatically downloaded when you run the appropriate script or command. [Provide specific instructions or script to run if needed.]

4. **Saving the Trained Model**:
    - After training, the model can be saved to be integrated into applications, such as a Flask web application.
    - The model will be saved in a format that can be easily loaded and used for inference.
