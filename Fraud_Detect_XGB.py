# prompt: Write code to build a streamlit app for the XGBoost model above

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the trained model
model = joblib.load('XGBmodel.pkl')

# Load the label encoder (assuming it's saved as 'label_encoder.pkl')
label_enc = LabelEncoder()


# Function to preprocess input data
def preprocess_input(input_data):
    input_df = pd.DataFrame([input_data])  # Convert input to DataFrame
    input_df["type"] = label_enc.fit_transform(input_df["type"])

    # Scale the numerical features using the same scaler used during training
    scaler = StandardScaler()
    numerical_cols = ["amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]
    input_df[numerical_cols] = scaler.fit_transform(input_df[numerical_cols])
    return input_df

# Streamlit app
st.title("Fraud Detection App")

# Input features
st.header("Input Transaction Details")
step = st.number_input("Step", min_value=1, step=1)
transaction_type = st.selectbox("Type", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
amount = st.number_input("Amount", min_value=0.0, step=0.01)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, step=0.01)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, step=0.01)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, step=0.01)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, step=0.01)
isFlaggedFraud = st.number_input("Is Flagged Fraud", min_value=0, max_value=1, step=1)

# Prediction button
if st.button("Predict"):
    input_data = {
        "step": step,
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "isFlaggedFraud": isFlaggedFraud
    }

    # Preprocess the input
    preprocessed_input = preprocess_input(input_data)

    # Make prediction
    prediction = model.predict(preprocessed_input)[0]

    # Display prediction
    st.header("Prediction")
    if prediction == 0:
        st.write("Legitimate Transaction")
    else:
        st.write("Fraudulent Transaction")
        
