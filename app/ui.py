
import streamlit as st
import requests

st.set_page_config(page_title="Credit Risk Predictor", page_icon="💳")
st.title("Credit Risk Predictor")
st.markdown("Enter customer details below:")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100)
    job = st.selectbox("Job", [0, 1, 2, 3])
    housing = st.selectbox("Housing", ["own", "rent", "free"])

with col2:
    credit_amount = st.number_input("Credit Amount")
    duration = st.number_input("Duration")

sex = st.selectbox("Sex", ["male", "female"])
saving = st.selectbox("Saving accounts", ["little", "moderate", "rich"])
checking = st.selectbox("Checking account", ["little", "moderate", "rich"])
purpose = st.selectbox(
    "Purpose",
    ["car", "furniture", "radio/TV", "education", "business"]
)

# Button
if st.button("Predict Risk"):
    try:
        data = {
            "Age": int(age),
            "Sex": str(sex),
            "Job": int(job),
            "Housing": str(housing),
            "Saving accounts": str(saving),
            "Checking account": str(checking),
            "Credit amount": float(credit_amount),
            "Duration": float(duration),
            "Purpose": str(purpose),
        }

        response = requests.post(
            "https://credit-risk-level.onrender.com/predict",
            json=data,
            timeout=60
        )

        st.write("Status Code:", response.status_code)
        st.write("Raw Response:", response.json())

        if response.status_code == 200:
            result = response.json()

            if "error" in result:
                st.error(f"API Error: {result['error']}")
            else:
                risk = "Low Risk" if result["risk_prediction"] == 1 else "High Risk"
                st.success(f"Prediction: {risk}")

        else:
            st.error("API Error")

    except Exception as e:
        st.error(f"Error: {e}")
