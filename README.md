📊 E-commerce Data Analysis using NumPy & Pandas
📌 Project Overview

This project performs an end-to-end E-commerce data analysis using Python, NumPy, and Pandas.
The objective is to analyze transaction data to uncover sales trends, customer behavior, and business insights, and to provide data-driven recommendations that can help improve business performance.

The analysis focuses on revenue, products, customers, payment methods, and customer demographics.

📂 Dataset Description

The dataset is sourced from Kaggle and contains E-commerce transaction-level data.

Columns in the Dataset

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

🛠️ Tools & Technologies Used

Python

NumPy

Pandas

Matplotlib

Kaggle Dataset

Git & GitHub

📌 Project Workflow
1️⃣ Data Loading

Loaded the dataset using Pandas

Handled file encoding issues during import

pd.read_csv("data.csv", encoding="latin1")

2️⃣ Data Cleaning & Preprocessing

Checked and handled missing values

Removed duplicate records

Converted columns to appropriate data types

Converted transaction date to datetime format

3️⃣ Feature Engineering

Created new features to enhance analysis:

TotalAmount = Quantity × Price × (1 − Discount)

Extracted Month and Year from TransactionDate

These features helped in revenue and time-based analysis.

4️⃣ Exploratory Data Analysis (EDA)

Performed descriptive analysis to understand:

Overall revenue

Average order value

Distribution of sales

Customer purchasing behavior

5️⃣ Business Analysis

Key analyses performed include:

Category-wise revenue analysis

Top-selling products by quantity

Top customers by total spending

Monthly sales trends

Payment method usage analysis

Customer demographics analysis

Gender-wise revenue

Income-group-wise spending

Loyalty score vs spending

6️⃣ NumPy-Based Statistical Analysis

Used NumPy for numerical analysis:

Mean, median, minimum, and maximum sales

Percentile calculations

Sales distribution insights

📈 Key Insights

A small number of product categories generate a major share of revenue

Customers with higher loyalty scores contribute significantly more revenue

Sales show noticeable trends across different months

Digital and card payments are the most preferred payment methods

Higher income groups have higher average order values

💡 Business Recommendations

Introduce loyalty-based rewards for high-value customers

Increase promotions during high-sales months

Focus inventory and marketing on top-performing categories

Personalize offers based on customer demographics

Optimize payment options based on customer preference

📁 Project Structure
Ecommerce-Data-Analysis/
│
├── data.csv
├── numpy_pandas.py   (or analysis.ipynb)
├── README.md

🎯 Learning Outcomes

Hands-on experience with NumPy and Pandas

Real-world data cleaning and preprocessing

Feature engineering for business analysis

Practical use of groupby and aggregations

Converting data analysis into actionable insights

Writing professional GitHub documentation

🚀 Future Enhancements

Add advanced visualizations using Seaborn

Perform customer segmentation analysis

Build an interactive dashboard using Streamlit or Power BI

Apply machine learning models for sales prediction

👩‍💻 Author

Puttabanthi Kruparani
AIML Student | Data Science Enthusiast
Skills: Python, NumPy, Pandas, Machine Learning, Data Analysis

▶️ How to Run the Project
pip install numpy pandas matplotlib
python numpy_pandas.py

⭐ Acknowledgement

The dataset used in this project is sourced from Kaggle and is used strictly for educational and learning purposes.
