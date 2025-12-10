import pandas as pd

# -----------------------------------------
# STEP 1: Load the Dataset
# -----------------------------------------
# Replace 'sales_data.csv' with your file name if needed
df = pd.read_csv('sales_data.csv')

# -----------------------------------------
# STEP 2: Clean the Data
# -----------------------------------------
# Fill missing values with 0
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# -----------------------------------------
# STEP 3: Perform Analysis
# -----------------------------------------

# Total revenue calculation
total_revenue = df['Total_Sales'].sum()

# Best-selling product (product with highest total sales)
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# Average sales value per order
average_sales = df['Total_Sales'].mean()

# -----------------------------------------
# STEP 4: Display Final Output (Report)
# -----------------------------------------

print("----------- SALES REPORT -----------")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Average Sales Per Order: ₹{average_sales:,.2f}")
print("-------------------------------------")
