import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import PowerTransformer, MinMaxScaler, OrdinalEncoder

from sklearn.ensemble import RandomForestClassifier
import pickle

def load_data(): 
    df_test = pd.read_csv("Churn_test.csv")
    #Converting the date columns into the appropriate date data type.
    df_test['Enrollment Date'] = pd.to_datetime(df_test['Enrollment Date'])
    df_test['Cancellation Date'] = pd.to_datetime(df_test['Cancellation Date'])

    #Tenure calculation and churn column creation
    df_test['tenure months'] = (df_test['Cancellation Date'] - df_test['Enrollment Date']).dt.days/30.44
    df_test['tenure months'] = df_test['tenure months'].fillna((pd.Timestamp('2019-01-01')-df_test['Enrollment Date']).dt.days/30.44)
    df_test['churn'] = df_test['Cancellation Date'].isnull().astype(int)
    df_test = df_test[['Postal Code', 'Gender', 'Education', 'Salary',
        'Marital Status', 'Loyalty Card', 'Enrollment Type','Total Flights', 'Distance', 'Points Accumulated', 'Points Redeemed',
        'Dollar Cost Points Redeemed', 'tenure months', 'CLV','churn']]

    df_test.columns = ["Postal_Code","Gender","Education","Salary","Marital_Status","Loyalty_Card",
  "Enrollment_Type", "Total_Flights",  "Distance", "Points_Accumulated", "Points_Redeemed",
  "Dollar_Cost_Points_Redeemed",  "tenure_months", "CLV","churn"]
    
    return df_test    

def train_model(df_test):
    # Features
    numerical = [
        'Total_Flights', 'Distance', 'Points_Accumulated', 'Points_Redeemed',
        'Dollar_Cost_Points_Redeemed', 'tenure_months', 'Salary', 'CLV'
    ]
    categorical = [
        'Postal_Code', 'Gender', 'Education', 'Marital_Status', 'Loyalty_Card', 'Enrollment_Type'
    ]
    
    features = categorical + numerical

    # Splitting data
    ytrain = df_test['churn'].values
    xtrain = df_test[features]

    # Define pipeline
    pipeline = make_pipeline(
        ColumnTransformer(
            transformers=[
                # Numerical transformation using YeoJohnson and then scaling
                ('num', make_pipeline(PowerTransformer(method='yeo-johnson'), MinMaxScaler()), numerical),
                ('cat', OrdinalEncoder(), categorical) #Encoding the categorical columns
            ],
            remainder='passthrough' #Other columns will pass through this transformer untouched
        ),
        RandomForestClassifier(n_estimators=100, max_depth=20)
    )

    pipeline.fit(xtrain, ytrain)
    return pipeline

def save_model(pipeline, output_file):
    with open(output_file, 'wb') as f_out:
        pickle.dump(pipeline, f_out)
    print("Model saved!")

if __name__ == "__main__":
    df = load_data()
    pipeline = train_model(df)
    save_model(pipeline, "pipeline_model.bin")