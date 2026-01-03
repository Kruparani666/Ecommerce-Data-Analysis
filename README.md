**E-commerce Data Analysis using NumPy & Pandas**
Overview:
This project performs an end-to-end E-commerce data analysis using Python, NumPy, and Pandas.
The objective is to analyze transaction data to uncover sales trends, customer behavior, and business insights, and to provide data-driven recommendations that can help improve business performance.

The analysis focuses on revenue, products, customers, payment methods, and customer demographics.
**Dataset Description**
The dataset is sourced from Kaggle and contains E-commerce transaction-level data.

**Columns in the Dataset**
TransactionID – Unique identifier for each transaction
CustomerID – Unique identifier for each customer
ProductID – Unique identifier for each product
ProductCategory – Category of the product
Quantity – Number of units purchased
Price – Price per unit
Discount – Discount applied on the transaction
TransactionDate – Date of purchase
PaymentMethod – Mode of payment
CustomerLocation – Location of the customer
CustomerAge – Age of the customer
CustomerGender – Gender of the customer
CustomerIncomeGroup – Income group of the customer
CustomerLoyaltyScore – Loyalty score assigned to the customer

**Tools & Technologies Used**
Python
NumPy
Pandas
Matplotlib
Kaggle Dataset
Git & GitHub

**Data Loading**
_1) Loaded the dataset using Pandas
2) Handled file encoding issues during import_
**pd.read_csv("data.csv", encoding="latin1")**

**Data Cleaning & Preprocessing**
_Checked and handled missing values
Removed duplicate records
Converted columns to appropriate data types
Converted transaction date to datetime format_

**Feature Engineering**
_Created new features to enhance analysis:
_TotalAmount = Quantity × Price × (1 − Discount)_
Extracted Month and Year from TransactionDate
These features helped in revenue and time-based analysis._

**Exploratory Data Analysis (EDA)**
_Performed descriptive analysis to understand:
Overall revenue
Average order value
Distribution of sales
Customer purchasing behavior_

**NumPy-Based Statistical Analysis**
_Used NumPy for numerical analysis:
Mean, median, minimum, and maximum sales
Percentile calculations
Sales distribution insights_

**Key Insights**
_A small number of product categories generate a major share of revenue
Customers with higher loyalty scores contribute significantly more revenue
Sales show noticeable trends across different months
Digital and card payments are the most preferred payment methods
Higher income groups have higher average order values_

**Author**
_Puttabanthi Kruparani
AIML Student | Data Science Enthusiast
Skills: Python, NumPy, Pandas, Machine Learning, Data Analysis_

**How to Run the Project**
_pip install numpy pandas matplotlib
python numpy_pandas.py_

**Acknowledgement**
The dataset used in this project is sourced from Kaggle and is used strictly for educational and learning purposes.
