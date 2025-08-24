# Airline Loyalty Program

Analysis and ML model developed on the Airline Loyalty Program dataset from Maven Analytics.

<br/>

## About the data
This is the customer loyalty program data from Northern Lights Air (NLA), a fictitious airline based in Canada. In an effort to improve program enrollment, NLA ran a promotion between Feb - Apr 2018. 

The dataset includes the following files with associated data:
1. Customer Flight Activity - Information regarding enrolled customers’ activity such as total flights, points obtained and similar.
2. Customer Loyalty History - Information about customer demographic, with lifetime value, enrollment and cancellation dates (if churned).
3. Calendar - Date information from the start of the program to December 2018.

<br/>

## Project Workflow

1. **Exploratory Data Analysis (EDA) & Data Preparation:**
   - Performed thorough investigation of the multiple files within the dataset, to resolve any inconsistencies such as blank rows, irregular numerical values and more.
   - Analyzed trends, distributions, and correlations among the columns within the notebook titled "Initial Analysis".

2. **Power BI Report**:
   - Created a 3 page report exploring -  Impact of promotion, member activity & member demographic information. Utilized the aggregated flight activity data created from the initial analysis.
   - Created visuals for flight frequency, cancellation and enrollments trends, customer demographic distribution with Year over Year change KPIs for enrollments, cancellations, flight frequency, active members and average duration of the membership.
   - Crafted various DAX measures, slicers and additional functionality in Power BI resulting in comprehensive analysis of the dataset.

3. **Machine Learning Modeling:**
   - Selected appropriate features and applied transformations such as scaling and encoding on the featres for customer churn prediction.
   - Evaluated various algorithms such as Logistic Regressor, SVM & Random Forest Classifier, to obtain the best model as Random Forest Classifier with 95% accuracy.

4. **Time Series Analysis:**
   - Utilized the Prophet model to forecast flight activity for the members.
   - Conducted time series decomposition on the flight and enrollment frequency to inspect trends and seasonal components. 

<br/>

## PowerBI Reports
1. Promotion Impact:
![Report 1](https://github.com/PranavP4tel/Airline-Loyalty-Program/blob/main/images/Promotion%20Impact.png)

2. Member Activity: 
![Report 2](https://github.com/PranavP4tel/Airline-Loyalty-Program/blob/main/images/Member%20Activity.png)

3. Member Loyalty:
![Report 2](https://github.com/PranavP4tel/Airline-Loyalty-Program/blob/main/images/Member%20Loyalty.png)

---
## References:
1. Dataset: https://mavenanalytics.io/data-playground/airline-loyalty-program?page=2&pageSize=20
