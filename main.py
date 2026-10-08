import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

st.set_page_config(page_title="FraudShield AI", layout="centered")

st.title("💳 FraudShield AI")
st.write("Credit Card Fraud Detection")

# Load model
model = load_model("fraudshield_model.h5")

# Load scaler
with open("fraudshield_scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


# Input fields
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=500.0
    )

    location_change = st.number_input(
        "Location Change",
        min_value=0,
        max_value=1,
        value=0
    )

    international_transaction = st.number_input(
        "International Transaction",
        min_value=0,
        max_value=1,
        value=0
    )


with col2:
    hour = st.number_input(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        value=14
    )

    online_transaction = st.number_input(
        "Online Transaction",
        min_value=0,
        max_value=1,
        value=1
    )

    previous_transactions = st.number_input(
        "Previous Transactions",
        min_value=0,
        value=10
    )


# Prediction
if st.button("🔍 Check Transaction"):

    data = np.array([
        amount,
        hour,
        location_change,
        online_transaction,
        international_transaction,
        previous_transactions
    ]).reshape(1, -1)

    data = scaler.transform(data)

    prediction = model.predict(data, verbose=0)

    if prediction[0][0] > 0.5:
        st.error("🚨 Fraudulent Transaction")
    else:
        st.success("✅ Normal Transaction")