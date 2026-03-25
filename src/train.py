import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer   
from sklearn.pipeline import Pipeline
from pipeline import create_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from config import DATA_PATH, MODEL_PATH, PIPELINE_PATH, TARGET_COLUMN


num_cols=["Age", "Credit amount", "Duration","Job"]
cat_cols=["Sex", "Housing","Saving accounts","Checking account", "Purpose"]
num_pipeline= Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

cat_pipeline=Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])
preprocessor=ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])
#Load DataSet
df=pd.read_csv(DATA_PATH)
print("Target Column", TARGET_COLUMN)
print("Unique Values",df[TARGET_COLUMN].unique())
#Split features and target


df[TARGET_COLUMN]=df[TARGET_COLUMN].str.strip()
df=df[df[TARGET_COLUMN].isin(['good','bad'])]
df=df.dropna(subset=[TARGET_COLUMN])

print("Cleaned Values",df[TARGET_COLUMN].unique())


X=df.drop(TARGET_COLUMN, axis=1)
Y=df[TARGET_COLUMN]

le=LabelEncoder()
Y=le.fit_transform(Y)

pipeline=create_pipeline(X)

#fit pipeline on full data
# X_processed=pipeline.fit_transform(X)
X_processed = preprocessor.fit_transform(X)
# pickle.dump(preprocessor, f)
#Train_test_split
X_train, X_test, y_train, y_test=train_test_split(X_processed, Y, test_size=0.2, random_state=42)

#Train Model
model=XGBClassifier(use_label_encoder=False,eval_metric='logloss')
model.fit(X_train,y_train)

#Save model
with open(MODEL_PATH,"wb") as f:
    pickle.dump(model,f)

#Save pipeline
with open(PIPELINE_PATH, "wb") as f:
    pickle.dump(preprocessor,f)

print("Model and pipeline saved successfully!!")