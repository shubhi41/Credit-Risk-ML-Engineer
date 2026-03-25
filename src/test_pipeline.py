import pandas as pd
from pipeline import create_pipeline

df=pd.read_csv(r"C:\Users\USER\Documents\AI_Projects\credit-risk-ml-engineer\data\credit_data.csv")

pipeline=create_pipeline(df)
print("Pipeline created successfully")