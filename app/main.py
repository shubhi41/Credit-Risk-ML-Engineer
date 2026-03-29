from fastapi import FastAPI 
import pickle
import pandas as pd
import numpy as np

#Load model & pipeline
# with open ("models/model.pkl", "rb") as f:
    # model=pickle.load(f)

with open ("models/pipeline.pkl", "rb") as f:
    pipeline=pickle.load(f)

#Initialize app
app=FastAPI()
    
@app.get("/")
def home():
    return {"message": "Credit Risk API is running"}

@app.post("/predict")
def predict(data:dict):

    print("Incoming Data", data)
    #Convert input to DataFrame

    df=pd.DataFrame([data])
    print("DataFrame Columns",df.columns)
    #Add missing columns by with default values
    for col in pipeline.feature_names_in_:
        if col not in df.columns:
            df[col]=np.nan

    #Ensrue correct order
    df=df[pipeline.feature_names_in_]
    df.replace("missing", np.nan,inplace=True)

    num_cols=["Age", "Credit amount", "Duration","Job"]

    for col in num_cols:
        df[col]=pd.to_numeric(df[col], errors="coerce")
    print(df.dtypes)
    #Apply pipeline
    try:
        # processed=pipeline.transform(df)
        prediction=pipeline.predict(df)[0]

        if hasattr(pipeline,"predict_proba"):
            proba=pipeline.predict_proba(df)[0][1]
        else:
            proba=0.0
                    

        return {
            "risk_prediction": int(prediction),
            "probability":float(proba)
            }
    except Exception as e:
        print("Error:",e)
        return {"error": str(e)}


