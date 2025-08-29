import pickle
import pandas as pd
import requests

url = "http://localhost:9696/predict"

customer = {
  "Postal_Code": "M2Z 4K1",
  "Gender": "Female",
  "Education": "Bachelor",
  "Marital_Status": "Married",
  "Loyalty_Card": "Star",
  "Enrollment_Type": "Standard",
  "Total_Flights": 37,
  "Distance": 54525,
  "Points_Accumulated": 54525.0,
  "Points_Redeemed": 1418,
  "Dollar_Cost_Points_Redeemed": 256,
  "tenure_months": 34.98685939553219,
  "Salary": 83236.0,
  "CLV": 3839.14
}


response = requests.post(url, json = customer)
churn = response.json()

print("Probability of Churning: ",churn['churn_probability'])
if churn['churn']>=0.5:
    print("Customer will churn")
else:
    print("Customer won't churn")