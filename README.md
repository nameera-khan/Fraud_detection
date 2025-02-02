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

- **Model Type**: Random Forest Classifier
- **Library**: Scikit-learn
- **Performance**:
  - Precision: `96.33%`
  - Recall: `73.58%`
  - F1 Score: `83.44%`
- **Custom Threshold**: The default decision threshold (0.5) was optimized to `0.9781` to balance precision and recall.

---

## **Usage Instructions**

### **1. Requirements**
Ensure the following libraries are installed:
```bash
pip install scikit-learn pandas streamlit joblib
