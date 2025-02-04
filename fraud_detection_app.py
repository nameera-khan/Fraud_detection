import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained fraud detection model
model = joblib.load("fraud_detection_model.pkl")

# Streamlit App Title
st.title("🔍 Fraud Detection App")
st.write("This application predicts whether a financial transaction is **fraudulent or legitimate**.")

# Sidebar - User Instructions
st.sidebar.header("ℹ️ How to Use")
st.sidebar.write("Enter transaction details below and click **Predict** to check for fraud.")

# User Input Fields
st.subheader("Enter Transaction Details")

step = st.number_input("Step (Hour of Transaction)", min_value=1, max_value=744, value=1)
type_input = st.selectbox("Transaction Type", ["CASH-IN", "CASH-OUT", "TRANSFER", "PAYMENT", "DEBIT"])
amount = st.number_input("Transaction Amount", min_value=1.0, max_value=1000000.0, value=100.0)
oldbalanceOrg = st.number_input("Sender's Old Balance", min_value=0.0, max_value=1000000.0, value=5000.0)
newbalanceOrig = st.number_input("Sender's New Balance", min_value=0.0, max_value=1000000.0, value=4000.0)
oldbalanceDest = st.number_input("Recipient's Old Balance", min_value=0.0, max_value=1000000.0, value=2000.0)
newbalanceDest = st.number_input("Recipient's New Balance", min_value=0.0, max_value=1000000.0, value=3000.0)
isFlaggedFraud = st.selectbox("Is Flagged Fraud?", [0, 1])

# Convert Inputs to DataFrame
input_data = pd.DataFrame({
    "step": [step],
    "type": [type_input],
    "amount": [amount],
    "oldbalanceOrg": [oldbalanceOrg],
    "newbalanceOrig": [newbalanceOrig],
    "oldbalanceDest": [oldbalanceDest],
    "newbalanceDest": [newbalanceDest],
    "isFlaggedFraud": [isFlaggedFraud]
})

# Mapping transaction type to numerical values (if needed)
type_mapping = {"CASH-IN": 0, "CASH-OUT": 1, "TRANSFER": 2, "PAYMENT": 3, "DEBIT": 4}
input_data["type"] = input_data["type"].map(type_mapping)

# Make Prediction
if st.button("🔍 Predict Fraud"):
    # Ensure the input data has the same columns as the training data
    expected_columns = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else None
    if expected_columns is not None:
        input_data = input_data[expected_columns]
    
    probability = model.predict_proba(input_data)[:, 1][0]  # Get fraud probability
    prediction = "🚨 Fraudulent Transaction" if probability > 0.5 else "✅ Legitimate Transaction"
    
    # Display Results
    st.subheader("Prediction Result")
    st.write(f"**Result:** {prediction}")
    st.write(f"**Fraud Probability:** {probability:.2f}")

    # Add warning if fraud probability is high
    if probability > 0.8:
        st.warning("⚠️ High fraud risk detected! Consider reviewing this transaction.")
