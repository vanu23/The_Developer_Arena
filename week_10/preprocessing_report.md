# Customer Churn Prediction – Preprocessing Report

## 1. Project Overview
The objective of this project is to preprocess customer data and build a robust preprocessing pipeline to support customer churn prediction. The preprocessing phase focuses on cleaning data, handling categorical variables, scaling numerical features, detecting outliers, and preparing the dataset for machine learning models.

---

## 2. Dataset Description
The dataset contains 500 customer records with the following columns:

| Column Name | Data Type | Description |
|------------|----------|-------------|
| CustomerID | Object | Unique customer identifier |
| Tenure | Integer | Number of months the customer has stayed |
| MonthlyCharges | Integer | Monthly billing amount |
| TotalCharges | Integer | Total amount charged |
| Contract | Object | Contract type |
| PaymentMethod | Object | Payment method used |
| PaperlessBilling | Object | Whether paperless billing is enabled |
| SeniorCitizen | Integer | Indicates if customer is a senior citizen |
| Churn | Integer | Target variable (1 = churn, 0 = no churn) |

---

## 3. Missing Value Handling
- No missing values were found in the dataset.
- All numerical columns were verified to be of correct data types.

---

## 4. Categorical Encoding
Three encoding techniques were used:

### 4.1 Label Encoding
- Applied to `PaperlessBilling`
- Converted binary categorical values into numeric format

### 4.2 One-Hot Encoding
- Applied to:
  - `Contract`
  - `PaymentMethod`
- Prevents ordinal assumptions between categories

### 4.3 Frequency Encoding
- Applied to `Tenure`
- Encodes values based on their occurrence frequency

---

## 5. Feature Scaling
Two scaling techniques were applied for comparison:

### 5.1 Min-Max Scaling
- Scales numerical values between 0 and 1

### 5.2 Standard Scaling
- Centers data around mean = 0 and standard deviation = 1

Applied to:
- `Tenure`
- `MonthlyCharges`
- `TotalCharges`

---

## 6. Outlier Detection & Treatment

### 6.1 IQR Method
- Used to detect extreme values in `MonthlyCharges`
- Outliers beyond 1.5 × IQR were removed

### 6.2 Z-Score Method
- Applied to `MonthlyCharges`
- Rows with absolute Z-score > 3 were removed

---

## 7. Preprocessing Pipeline
A complete preprocessing pipeline was created using:
- `ColumnTransformer`
- `Pipeline`
- `StandardScaler`

This ensures consistent preprocessing during training and inference.

---

## 8. Conclusion
The preprocessing steps transformed raw customer data into a clean, structured, and machine-learning-ready dataset. The pipeline approach improves reproducibility, scalability, and deployment readiness.

---
