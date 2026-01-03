import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("ecommerce_sales_data.csv")

print(df.head())
df.head()
df.shape
df.columns
df.info()


df.isnull().sum()
df.dropna(inplace=True)      # OR
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)
# Convert date column
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

# Ensure numeric columns are numeric
numeric_cols = [
    'Quantity',
    'Price',
    'Discount',
    'CustomerAge',
    'CustomerLoyaltyScore'
]

df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
df['TotalAmount'] = df['Quantity'] * df['Price'] * (1 - df['Discount'])
df['Month'] = df['TransactionDate'].dt.month
df['Year'] = df['TransactionDate'].dt.year
print(df.head())
df.info()
df.describe()
#Total Revenue
total_revenue = df['TotalAmount'].sum()
print("Total Revenue:", total_revenue)
#Average Order Value
avg_order_value = df['TotalAmount'].mean()
print("Average Order Value:", avg_order_value)

#Top Product Categories by Revenue
category_revenue = (
    df.groupby('ProductCategory')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
)

print(category_revenue)


#Most Sold Products (by Quantity)
top_products = (
    df.groupby('ProductID')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

#Monthly sales trend
monthly_sales = (
    df.groupby('Month')['TotalAmount']
    .sum()
)

print(monthly_sales)
#Top Customers by Spending
top_customers = (
    df.groupby('CustomerID')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)
#Payment method analysis
payment_analysis = (
    df['PaymentMethod']
    .value_counts()
)

print(payment_analysis)

#Customer Demographics Analysis
#By gender
gender_revenue = (
    df.groupby('CustomerGender')['TotalAmount']
    .sum()
)

print(gender_revenue)
#By income group
income_revenue = (
    df.groupby('CustomerIncomeGroup')['TotalAmount']
    .sum()
)

print(income_revenue)


#Numpy based analysis
import numpy as np

sales = df['TotalAmount'].values

print("Min Sale:", np.min(sales))
print("Max Sale:", np.max(sales))
print("Mean Sale:", np.mean(sales))
print("Median Sale:", np.median(sales))
print("75th Percentile:", np.percentile(sales, 75))
