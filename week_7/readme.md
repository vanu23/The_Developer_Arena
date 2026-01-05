# 📊 Statistical Business Analysis (Sales & Customer Churn)

## 🎯 Project Overview
This project performs an end-to-end statistical analysis on business data to derive actionable insights.
It combines **sales performance analysis** with **customer churn behavior analysis** using statistical
methods such as hypothesis testing, correlation analysis, confidence intervals, and regression modeling.

Datasets Used:
- `sales_data.csv` – Sales, revenue, quantity, product, and region data
- `customer_churn.csv` – Customer tenure, charges, and churn status

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels
- Jupyter Notebook

---

## 📂 Project Structure
Statistical_Business_Analysis/
│
├── statistical_analysis.ipynb
├── sales_data.csv
├── customer_churn.csv
├── hypothesis_tests_results.txt
├── requirements.txt
└── README.md
---

## 📅 Step-by-Step Methodology

### Day 1: Descriptive Statistics
- Mean, Median, Mode, Standard Deviation
- Applied on Total Sales and Churn-related numerical features

### Day 2: Data Distribution Analysis
- Histogram visualization
- Normality testing using Shapiro-Wilk test

### Day 3: Correlation Analysis
- Pearson correlation for sales drivers
- Heatmap visualization
- Numeric-only correlation for churn dataset

### Day 4: Hypothesis Testing
- Independent T-Test (East vs West sales)
- One-Way ANOVA (Product-wise sales)
- T-Test (Churn vs Monthly Charges)

### Day 5: Confidence Intervals
- 95% confidence interval for average sales
- Margin of error calculation

### Day 6: Regression Analysis
- Linear regression: Quantity → Total Sales
- Linear regression: Tenure → Monthly Charges
- R² interpretation

### Day 7: Business Insights
- Sales growth driven by quantity
- Regional sales differences
- Higher charges linked with churn risk

---

## 📊 Key Insights
- Strong positive correlation between quantity sold and total sales
- Region significantly impacts sales performance
- Churned customers tend to have higher monthly charges
- Quantity explains a large portion of revenue variability

---

## 📈 Business Recommendations
- Implement volume-based promotions
- Use region-specific sales strategies
- Reduce churn by offering pricing incentives to high-charge customers

---

## 🧪 Testing & Validation
- All hypothesis tests validated using p-values
- Numeric-only correlation applied to avoid data type errors
- Regression assumptions checked via model summary

---

## 🏁 Conclusion
This project demonstrates practical statistical analysis skills applied to real-world business data,
making it suitable for academic evaluation and data analyst interviews.
