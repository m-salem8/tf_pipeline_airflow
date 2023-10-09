import numpy as np
from keras.preprocessing import image

def load_and_preprocess_image(image_path, target_size=(48, 48), color_mode="grayscale"):
    """
    Load and preprocess an image for model prediction.
    Args:
        image_path (str): Path to the image file.
        target_size (tuple): Target size for resizing the image.
        color_mode (str): Color mode for the image.
    Returns:
        numpy.ndarray: Preprocessed image as a NumPy array.
    """
    img = image.load_img(image_path, target_size=target_size, color_mode=color_mode)
    img = image.img_to_array(img)
    img = img / 255.0  # Normalize the pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def predict(model, image_data):
    """
    Make predictions using the trained model.
    Args:
        model (tf.keras.models.Model): Trained machine learning model.
        image_data (numpy.ndarray): Preprocessed image data.
    Returns:
        str: Predicted class label.
    """
    # Perform the prediction
    result = model.predict(image_data)

    # Determine the predicted class label
    img_index = np.argmax(result)
    label_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}
    predicted_label = label_dict[img_index]

    return predicted_label

if __name__ == "__main__":
    # You can include test code here to run the module independently if needed.
    pass

