https://credit-risk-level.onrender.com/docs
### Credit Risk Prediction System

An end-to-end Machine Learning project that predicts whether a customer is **High Risk or Low Risk** based on financial and demographic inputs. Built with a production-ready pipeline and deployed using FastAPI.

-

#### Live Demo
- API (Swagger UI): https://credit-risk-level.onrender.com/docs  


---

#### Tech Stack
- Python, Pandas, NumPy  
- Scikit-learn, XGBoost  
- FastAPI (Backend API)  
- Streamlit (Frontend UI)  
- Render (Cloud Deployment)

---

#### Features
- End-to-end ML pipeline (preprocessing + prediction)
- Real-time predictions via REST API
- Interactive UI for user input
- Handles missing values and categorical encoding
- Deployed and accessible via cloud

---

#### ML Workflow
1. Data cleaning and preprocessing  
2. Feature transformation using ColumnTransformer  
3. Model training using XGBoost Classifier  
4. API deployment using FastAPI  
5. UI integration using Streamlit  

---

#### API Usage

#### Endpoint:
POST `/predict`

#### Sample Input:
```json
{
  "Age": 30,
  "Sex": "male",
  "Job": 2,
  "Housing": "own",
  "Saving accounts": "little",
  "Checking account": "little",
  "Credit amount": 5000,
  "Duration": 24,
  "Purpose": "car"
}
