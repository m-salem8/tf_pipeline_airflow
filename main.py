from _01_data_ingestion import load_data
from _02_data_validation import validate_data
from _03_data_preprocessing import preprocess_data
from _04_model_training import train_model, build_model, save_model
from _05_performance_evaluation import evaluate_model
from _06_model_prediction import predict

def main():
    # Step 1: Data Ingestion
    load_data() #TODO uncomment for github

    # Step 2: Data Validation
    # validate_data(data)

    # Step 3: Data Preprocessing
    train_generator, validation_generator = preprocess_data()

    # Step 4: Model Training
    # instantiate and build the model
    model = build_model()

    # train the model
    model = train_model(model, train_generator, validation_generator, epochs=1, batch_size=1) # TODO change epochs to 60, batch size to 64

    # Step 5: Performance Evaluation
    evaluate_model(model, train_generator, validation_generator)
    #TODO improve this part
    save_model(model)


    """# Step 6: Model Prediction
    prediction = predict(model, preprocessed_data)"""

if __name__ == "__main__":
    main()
