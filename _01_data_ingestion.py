import os
import zipfile
import random
import shutil

os.environ["KAGGLE_USERNAME"] = "salem852"
os.environ["KAGGLE_KEY"] = "f74678e6ea765844e93503c0b914afcc"

import kaggle

def reduce_dataset(source_dir, destination_dir, percent_to_keep=0.10):

    for class_dir in os.listdir(source_dir):
        source_class_path = os.path.join(source_dir, class_dir)
        destination_class_path = os.path.join(destination_dir, class_dir)

        os.makedirs(destination_class_path, exist_ok=True)

        image_files = os.listdir(source_class_path)
        num_images_to_keep = int(len(image_files) * percent_to_keep)

        selected_images = random.sample(image_files, num_images_to_keep)

        for image_file in selected_images:
            source_image_path = os.path.join(source_class_path, image_file)
            destination_image_path = os.path.join(destination_class_path, image_file)
            shutil.copy(source_image_path, destination_image_path)

def load_data():
    # Kaggle identifiers are defined in Github as secrets
    # Or in Airflow as Variables
    dataset_name = 'msambare/fer2013'
    download_path = 'app/tf_pipeline_data/'  # Absolute path to make sure we're downloading to the right location
    
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

    # Create reduced train dataset (10% of the original)
    source_train_dir = 'app/tf_pipeline_data/train'
    destination_train_dir = 'app/tf_pipeline_data/train_reduced'
    reduce_dataset(source_train_dir, destination_train_dir, 0.10)

    # Create reduced test dataset (10% of the original)
    source_test_dir = 'app/tf_pipeline_data/test'
    destination_test_dir = 'app/tf_pipeline_data/test_reduced'
    reduce_dataset(source_test_dir, destination_test_dir, 0.10)

if __name__ == "__main__":
    load_data()
