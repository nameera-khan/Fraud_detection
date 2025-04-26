
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained XGBoost model
model = joblib.load('XGBmodel-2.pkl')

# Function to preprocess input data
def preprocess_input(input_data):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])
    
    # Feature engineering (same as in your training script)
    input_df['balanceDiffOrig'] = input_df['oldbalanceOrg'] - input_df['newbalanceOrig']
    input_df['balanceDiffDest'] = input_df['oldbalanceDest'] - input_df['newbalanceDest']
    input_df['amountToBalanceRatio'] = input_df['amount'] / (input_df['oldbalanceOrg'] + 1e-9)
    input_df['origZeroBal'] = (input_df['oldbalanceOrg'] == 0).astype(int)
    input_df['destZeroBal'] = (input_df['oldbalanceDest'] == 0).astype(int)
    input_df['hour'] = input_df['step'] % 24
    input_df['day'] = input_df['step'] // 24
    
    # Ensure consistent column order
    required_cols = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud', 'type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER', 'balanceDiffOrig', 'balanceDiffDest', 'amountToBalanceRatio', 'origZeroBal', 'destZeroBal', 'hour', 'day']
    input_df = input_df[required_cols]

    return input_df

# Streamlit app
st.title("Fraud Detection App")

# Input features
step = st.number_input("Step", min_value=0)
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0)
isFlaggedFraud = st.selectbox("Is Flagged Fraud", [0, 1])
type_CASH_OUT = st.selectbox("Type CASH_OUT", [0, 1])
type_DEBIT = st.selectbox("Type DEBIT", [0, 1])
type_PAYMENT = st.selectbox("Type PAYMENT", [0, 1])
type_TRANSFER = st.selectbox("Type TRANSFER", [0, 1])


# Prediction button
if st.button("Predict"):
    input_data = {
        'step': step, 'amount': amount, 'oldbalanceOrg': oldbalanceOrg, 'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest, 'newbalanceDest': newbalanceDest, 'isFlaggedFraud': isFlaggedFraud,
        'type_CASH_OUT': type_CASH_OUT, 'type_DEBIT': type_DEBIT, 'type_PAYMENT': type_PAYMENT,
        'type_TRANSFER': type_TRANSFER
    }

    input_df = preprocess_input(input_data)
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Fraudulent Transaction")
    else:
        st.success("Legitimate Transaction")
