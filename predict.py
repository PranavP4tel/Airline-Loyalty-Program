import pickle
import pandas as pd
from train import load_data
from typing import Dict, Any, Literal, Annotated
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

#Request validation
class Customer(BaseModel):
    Postal_Code: str
    Gender: Literal['Female', 'Male']
    Education: Literal['Bachelor', 'High School or Below', 'Doctor', 'Master']
    Marital_Status: Literal['Married', 'Divorced', 'Single']
    Loyalty_Card: Literal['Star', 'Nova', 'Aurora']
    Enrollment_Type: Literal['Standard', '2018 Promotion']
    
    Total_Flights: Annotated[int, Field(ge=0)]
    Distance: Annotated[float, Field(ge=0)]
    Points_Accumulated: Annotated[float, Field(ge=0)]
    Points_Redeemed: Annotated[int, Field(ge=0)]
    Dollar_Cost_Points_Redeemed: Annotated[int, Field(ge=0)]
    tenure_months: Annotated[float, Field(ge=0)]
    Salary: Annotated[float, Field(ge=0)]
    CLV: Annotated[float, Field(ge=0)]


#Response validation
class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool

app = FastAPI(title = "customer_churn")


with open('pipeline_model.bin', 'rb') as file:
    pipeline = pickle.load(file)

#numerical = [
#        'Total_Flights', 'Distance', 'Points_Accumulated', 'Points_Redeemed',
#        'Dollar_Cost_Points_Redeemed', 'tenure_months', 'Salary', 'CLV'
#    ]
#categorical = [
#        'Postal_Code', 'Gender', 'Education', 'Marital_Status', 'Loyalty_Card', 'Enrollment_Type'
#    ]
#features = categorical + numerical

#df = load_data()

#test_record = df[features].iloc[0,:].to_dict()
#def predict_single(customer):
#    result = pipeline.predict_proba(pd.DataFrame([customer]))[0][1]
#    return float(result)

#def predict(customer):
#    prob = predict_single(customer)

#    return {
#        "churn_probability": prob,
#        "churn": bool(prob>=0.5)
#    }

#print(predict(test_record))
#print(test_record)

def predict_single(customer):
    input_dict = customer.dict()  # convert to dictionary
    input_df = pd.DataFrame([input_dict])
    result = pipeline.predict_proba(input_df)[0][1]
    return float(result)

@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    prob = predict_single(customer)

    return PredictResponse(
        churn_probability = prob,
        churn = bool(prob>=0.5)
    )

if __name__ == "__main__":
    uvicorn(app, host= "localhost", port = 9696)