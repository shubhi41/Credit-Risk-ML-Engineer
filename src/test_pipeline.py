import pandas as pd
from pipeline import create_pipeline

df=pd.read_csv(r"data\credit_data.csv")

pipeline=create_pipeline(df)
print("Pipeline created successfully")
