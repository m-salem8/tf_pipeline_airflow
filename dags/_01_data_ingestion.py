import os
import zipfile
import kaggle


def load_data():
    # Kaggle identifiers are defined in Github as secrets
    # Or in Airflow as Variables
    dataset_name = 'msambare/fer2013'
    download_path = '/app/tf_pipeline_data/'  # Absolute path to make sure we're downloading to the right location
    
    # Download the dataset as a zip file
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=False)

    # Construct the expected path of the downloaded zip file
    zip_file_name = f"{dataset_name.split('/')[-1]}.zip"
    zip_file_path = os.path.join(download_path, zip_file_name)
    
    print(f"ZIP file saved at: {zip_file_path}")

    # Unzip the dataset
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    # Print the extracted contents
    for root, dirs, files in os.walk(download_path):
        for file in files:
            print(os.path.join(root, file))

    os.remove(zip_file_path)