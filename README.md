# 🛫 Airline Loyalty Program Analysis & ML Modeling
Comprehensive analytics and machine learning project leveraging **Northern Lights Air (NLA)** customer loyalty data, performed as part of the Maven Analytics Data Playground challenge.
---
## 📦 Dataset Overview
- **Source:** Maven Analytics
- **Scope:** Customer loyalty program data from a fictitious Canadian airline (Northern Lights Air or NLA). In an effort to improve program enrollment, NLA ran a promotion between Feb - Apr 2018. Files Included:
1. **Customer Flight Activity:**  Information regarding enrolled customers’ activity such as total flights, points obtained and similar.
2. **Customer Loyalty History:** Information about customer demographic, with lifetime value, enrollment and cancellation dates (if churned).
3. **Calendar:** Comprehensive date table from program start to Dec 2018.
---
## 🚀 Project Workflow
### 1. ***Exploratory Data Analysis & Preparation***
**Tool:** Jupyter Notebook (`Initial Analysis.ipynb`)  
- Cleaned datasets: handled missing values, irregular numbers, and inconsistencies.
- Explored trends, distributions, and key correlations for feature engineering.
---
### 2. ***Power BI Reporting***
**Tool:** Power BI (`Session_1.pbix`)  
- 3-page report exploring:
  - **Promotion Impact**
  - **Member Activity**
  - **Customer Demographics**
- Visuals include:
  - Flight frequency, enrollments & cancellations, customer demographic distribution
  - Year-over-Year KPIs (enrollments, cancellation rates, member duration and more)
- Created custom **DAX measures**, slicers, and used additional functionality in Power BI resulting in comprehensive analysis of the dataset.

#### **PowerBI Reports:**
Promotion Impact  
![Report1](https://github.com/PranavP4tel/Airline-Loyalty-Program/blob/main/images/Promotion%20Impact.png)

Member Activity  
![Report2](https://github.com/PranavP4tel/Airline-Loyalty-Program/blob/main/images/Member%20Activity.png)

Member Loyalty  
![Report3](https://github.com/PranavP4tel/Airline-Loyalty-Program/blob/main/images/Member%20Loyalty.png)

---
### 3. ***Machine Learning Modeling***
**Tool:** Jupyter Notebook (`ML Application.ipynb`)  
- Selected appropriate features and applied transformations such as scaling and encoding on the featres for customer churn prediction.
- **Algorithms Evaluated:** Logistic Regression, SVM, **Random Forest Classifier** and others.
- **Outcome:** Best model — **Random Forest Classifier** with **95% accuracy** for customer churn prediction
---
### 4. ***Time Series Analysis***
**Tool:** Prophet Model & Decomposition (`ML Application.ipynb`)  
- Utilized the Prophet model to forecast flight activity for the members.
- Conducted time series decomposition on the flight and enrollment frequency to inspect **trends and seasonal components.** 
---
### 5. ***Model Deployment***
- **Files:** `Churn_test.csv`, `train.py`, `predict.py`, `marketing.py`, `Dockerfile`
- **Tech Stack:** **FastAPI**, **Pydantic**, **scikit-learn**, **Docker**
- **Pipeline:**
  - **Churn_test.csv:** Contains the combined records from flight activity and loyalty history of members, joined via the common Loyalty Numbers.
  - **train.py:** Created 3 functions as load_data (to load the data from the csv file and conduct preprocessing), train_model (to create a Random Forest model using Pipeline & Column Transformer) and save_model (to save the model using pickle for reuse)
  - **predict.py:** Using FastAPI, created a web service to use the model in predicting customer churn. Used Pydantic validation to take the customer information from the user, and predict the churn probability using the saved model. The results were also validated using Pydantic.
  - **marketing.py:** Serves as a script to be used by the marketing team, to simply provide the customer information and obtain the churn probability using the running webservice from predict.py. Hence, this probability can assist them in making custom customer retention strategies.
  - **Dockerfile:** Containerization for cross-platform deployment.

    
**Note**: One can start the web service using the command below. Also, a test record script is placed commented in predict.py. A hard coded test record is present in marketing.py for direct use.
```
uvicorn predict:app --host localhost --port 9696 --reload
```
---
## 📑 References
- [🗂 Dataset](https://mavenanalytics.io/data-playground/airline-loyalty-program?page=2&pageSize=20)
- [▶️ Model Deployment (YouTube)](https://www.youtube.com/watch?v=jzGzw98Eikk&t=4s)
