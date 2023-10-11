import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from PIL import Image

def preprocess_data(img_size=48, batch_size=64):
    train_datagen = ImageDataGenerator(rotation_range = 180,
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    horizontal_flip = True,
    rescale = 1./255,
    zoom_range = 0.2,
    validation_split = 0.2
    )

    validation_datagen = ImageDataGenerator(rescale = 1./255,
    validation_split = 0.2)

    # path to local directory
    train_dir = "/app/tf_pipeline_data/train"
    test_dir = "/app/tf_pipeline_data/test"
    if os.path.exists(train_dir):
        print("Train directory exists:", train_dir)
    else:
        print("Train directory does NOT exist:", train_dir)

    if os.path.exists(test_dir):
        print("Test directory exists:", test_dir)
    else:
        print("Test directory does NOT exist:", test_dir)   

    train_generator = train_datagen.flow_from_directory(directory = train_dir,
    target_size = (img_size,img_size),
    batch_size = batch_size,
    color_mode = "grayscale",
    class_mode = "categorical",
    subset = "training"
    )

    validation_generator = validation_datagen.flow_from_directory( directory = test_dir,
    target_size = (img_size,img_size),
    batch_size = batch_size,
    color_mode = "grayscale",
    class_mode = "categorical",
    subset = "validation"
    )

    return train_generator, validation_generator

