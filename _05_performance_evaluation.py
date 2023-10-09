import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate_model(model, train_generator, validation_generator):
    """
    Evaluate the performance of the trained model on the validation dataset.
    Args:
        model (tf.keras.models.Model): Trained machine learning model.
        data: Validation data (features and labels).
    """
    
    train_loss, train_acc = model.evaluate(train_generator)
    test_loss, test_acc   = model.evaluate(validation_generator)
    
    print("final train accuracy = {:.2f} , validation accuracy = {:.2f}".format(train_acc*100, test_acc*100))

    # TODO add confusion matrix and classification report 

    """# Generate a confusion matrix
    conf_matrix = confusion_matrix(np.argmax(y_val, axis=1), y_pred_labels)
    print("Confusion Matrix:")
    print(conf_matrix)

    # Generate a classification report
    class_report = classification_report(np.argmax(y_val, axis=1), y_pred_labels)
    print("Classification Report:")
    print(class_report)"""

if __name__ == "__main__":
    # You can include test code here to run the module independently if needed.
    pass
