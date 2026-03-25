import streamlit as st
import requests

st.title("Credit Risk Predictor")

#Input Fields
age=st.number_input("Age", 18, 100)
job=st.selectbox("Job",[0,1,2,3])
housing=st.selectbox("Housing",["own","rent","free"])
credit_amount=st.number_input("Credit Amount")
duration=st.number_input("Duration")

sex = st.selectbox("Sex", ["male", "female"])
saving = st.selectbox("Saving accounts", ["little", "moderate", "rich"])
checking = st.selectbox("Checking account", ["little", "moderate", "rich"])
purpose = st.selectbox("Purpose", ["car", "furniture", "radio/TV", "education", "business"])

# required_cols = [
#     "Age", "Sex", "Job", "Housing",
#     "Saving accounts", "Checking account",
#     "Credit amount", "Duration", "Purpose"
# ]

# for col in required_cols:
#     if col not in df.columns:
#         df[col] = "missing"  # or np.nan
# required_cols = [
#     "Age", "Sex", "Job", "Housing",
#     "Saving accounts", "Checking account",
#     "Credit amount", "Duration", "Purpose"
# ]

# for col in required_cols:
#     if col not in df.columns:
#         df[col] = "missing"  # or np.nan

# df = df[required_cols]

#Button
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

        response=requests.post("http://127.0.0.1:8000/predict",json=data)

        st.write("Status Code:",response.status_code)
        st.write("Raw Response",response.text)
        if response.status_code==200:
            result=response.json()
            st.success(f"Prediction:{result}")
        else:
            st.error("API Error")

    except Exception as e:
        st.error(f"Error: {e}")
