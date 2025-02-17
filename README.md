# **Fraud Detection Model**

This repository contains a trained machine learning model for detecting fraudulent financial transactions. The model is saved as a `.pkl` file for easy loading and integration into applications such as Streamlit dashboards, APIs, or other real-time systems.

---

## **Overview**

The fraud detection model was trained using a synthetic dataset of financial transactions. The model predicts whether a transaction is **fraudulent** or **legitimate** based on several key features like transaction type, amount, and account balances.

---

## **Features Used**

The following features were used to train the model:

- **`step`**: Time in hours since the start of the simulation.
- **`type`**: Type of transaction (e.g., CASH-IN, CASH-OUT, TRANSFER, PAYMENT, DEBIT).
- **`amount`**: Amount of the transaction in local currency.
- **`oldbalanceOrg`**: Initial balance of the sender before the transaction.
- **`newbalanceOrig`**: New balance of the sender after the transaction.
- **`oldbalanceDest`**: Initial balance of the recipient before the transaction.
- **`newbalanceDest`**: New balance of the recipient after the transaction.
- **`isFlaggedFraud`**: Whether the transaction was flagged as suspicious based on business rules.

---

## **Model Details**

- **Model Type**: XGBoost 
- **Library**: Scikit-learn
- **Performance**:
  - Precision: `99.33%`
  - Recall: `99.61%`
  - F1 Score: `99.47%`

## **Run the App Online (No Installation Needed)**

Click the link below to access the app instantly on Streamlit Cloud:
https://frauddetection-gwewmettkfc6ynvh2q4uzz.streamlit.app



