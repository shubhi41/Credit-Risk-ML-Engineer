import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def create_pipeline(df):
    #Separate Feature types
    numerical_features=df.select_dtypes(include=['int64','float64']).columns
    categorical_features=df.select_dtypes(include=['object']).columns

    #Numeric
    numeric_pipeline=Pipeline([
        ("scaler",StandardScaler())
    ])

    #Categorical
    categorical_pipeline=Pipeline([
        ("encoder", OneHotEncoder(handle_unknown='ignore'))
    ])

    #Combine both
    preprocessor=ColumnTransformer([
        ("num",numeric_pipeline,numerical_features),("cat",categorical_pipeline, categorical_features)
    ])

    return preprocessor