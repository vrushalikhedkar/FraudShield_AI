# FraudShield AI 💳

Credit Card Fraud Detection using Machine Learning & Deep Learning
FraudShield AI is a machine learning and deep learning project that
predicts whether a credit card transaction is Normal or
Fraudulent.

The project compares traditional machine learning models with a simple
Deep Neural Network and provides a Streamlit web application for making
predictions.


## Features
- Credit card transaction classification
- Logistic Regression model
- Random Forest model
- Deep Neural Network (DNN)
- StandardScaler for feature scaling
- Model evaluation using Accuracy, Confusion Matrix, and
  Classification Report
- Streamlit web application for prediction


## Input Features
The application uses the following transaction details:
- Transaction Amount
- Transaction Hour
- Location Change
- Online Transaction
- International Transaction
- Previous Transactions


## Models Used
## Machine Learning
- Logistic Regression
- Random Forest


## Deep Learning
- Dense Neural Network
- ReLU activation
- Sigmoid activation
- Adam optimizer
- Binary Cross-Entropy loss


## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Streamlit


## Project Structure
```text
FraudShield AI
|
├── fraudshield_model.h5
├── fraudshield_scaler.pkl
├── main.py
├── fraudshield_dataset_v2.csv
└── README.md
```


## How to Run
Install the required libraries:
```bash
pip install pandas numpy scikit-learn tensorflow streamlit
```


## Run the Streamlit application:
```bash
python -m streamlit run main.py
```
The application opens in the browser, where transaction details can be
entered and checked.


## Prediction
The application returns one of two results:
- ✅ Normal Transaction
- 🚨 Fraudulent Transaction


## Project Goal
The goal of this project is to demonstrate how Machine Learning and Deep
Learning can be applied to transaction fraud detection and deployed
through a simple interactive web application.


## Author
***Vrushali V. Khedkar***
