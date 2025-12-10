# 📊 Sales Data Analysis Project

## 📌 Overview
This project performs a simple yet effective analysis of sales data using Python and pandas.  
It includes data cleaning, descriptive analysis, and generation of key business metrics.

### 🎯 Project Objectives
- Load and explore a sales dataset  
- Clean data by handling missing values and removing duplicates  
- Calculate key metrics:  
  - Total Revenue  
  - Best-Selling Product  
  - Average Sales Per Order  
- Generate a clear and clean formatted report  

---

## 📂 Project Structure

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


---

## 🛠️ Technologies Used
- **Python**
- **Pandas**

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
pip install pandas

### 2️⃣ Place your dataset
Make sure `sales_data.csv` is inside the project folder.

### 3️⃣ Run the analysis script
python sales_analysis.py
You will see:
- Total Revenue  
- Best-Selling Product  
- Average Sales  
in the terminal output.

---

## 📊 Features & Analysis Steps

### ✔️ Step 1: Load Data
Reads the CSV file using pandas.

### ✔️ Step 2: Clean Data
- Missing values are replaced with 0  
- Duplicate rows are removed  

### ✔️ Step 3: Analyze Sales
- Calculates total revenue  
- Identifies the best-selling product  
- Computes average sales per order  

### ✔️ Step 4: Final Report
A structured report is generated and can be found in `analysis_report.md`.

---

## 📄 Sample Output

----------- SALES REPORT -----------
Total Revenue: ₹12,50,000.00
Best Selling Product: Product A
Average Sales Per Order: ₹780.50

---

## 📝 Documentation Files
- **sales_analysis.py** → Main Python script  
- **analysis_report.md** → Final sales analysis report  
- **requirements.txt** → Dependencies  
- **README.md** → Project explanation  

---

## 👤 Author
**Vanshika Rupera**  
Data Analyst | Python | Machine Learning | Visualization  

---

