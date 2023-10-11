import numpy as np 
import pandas as pd
import os
import tensorflow as tf
import keras
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten,Dense,Dropout,BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16, InceptionResNetV2
from keras import regularizers
from tensorflow.keras.optimizers import Adam,RMSprop,SGD,Adamax
from PIL import Image
from _03_data_preprocessing import preprocess_data


save_path = '/app/tf_pipeline_data/model_with_epoch'
def build_model():

    # instantiate the model
    model= tf.keras.models.Sequential()
    
    # convolutional layers
    model.add(Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(48, 48,1)))
    model.add(Conv2D(64,(3,3), padding='same', activation='relu' ))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(128,(5,5), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
        
    model.add(Conv2D(512,(3,3), padding='same', activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(512,(3,3), padding='same', activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    # flatten layer
    model.add(Flatten()) 
    model.add(Dense(256,activation = 'relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.25))

    # dense layer
    model.add(Dense(512,activation = 'relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.25))

    model.add(Dense(7, activation='softmax'))

    model.compile(
        optimizer = Adam(lr=0.0001), 
        loss='categorical_crossentropy', 
        metrics=['accuracy']
    )

    # model.summary()

    #TODO add plot_model

    """plot_model(model, show_shapes=True,
    show_layer_names=False,
    expand_nested=True,
    rankdir="TB",
    dpi=100)"""

    return model


def process_train_save(epochs=1):
    model = build_model()
    train_generator, validation_generator = preprocess_data(img_size=48, batch_size=64)
    model.fit(x = train_generator, epochs = epochs, validation_data = validation_generator)
    model.save(save_path)


  






