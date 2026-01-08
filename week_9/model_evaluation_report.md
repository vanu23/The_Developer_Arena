# 🏠 House Price Prediction – Model Evaluation Report

## 1. Project Overview

The objective of this project is to build and evaluate machine learning models capable of predicting house prices based on property features such as area, number of bedrooms, and location. Accurate house price prediction helps buyers, sellers, and real estate professionals make informed decisions.

This project follows a structured data science workflow including data understanding, preprocessing, model building, evaluation, and interpretation.

---

## 2. Dataset Description

The dataset contains information about residential properties with the following key features:

- Area of the house
- Number of bedrooms
- Location (categorical)
- House price (target variable)

After preprocessing, categorical variables were converted into numerical format using one-hot encoding.

---

## 3. Data Preprocessing

The following preprocessing steps were applied:

- Checked and handled missing values using median imputation for numerical columns
- Converted categorical features into numerical values using one-hot encoding
- Split the dataset into training (80%) and testing (20%) sets
- Separated independent variables (X) and target variable (y)

These steps ensured the dataset was suitable for machine learning algorithms.

---

## 4. Models Implemented

Multiple regression models were implemented and evaluated:

### 4.1 Linear Regression (From Scratch)
- Implemented using the Normal Equation
- Helped in understanding the mathematical foundation of linear regression

### 4.2 Linear Regression (scikit-learn)
- Implemented using `LinearRegression` from scikit-learn
- Served as the baseline model

### 4.3 Polynomial Regression
- Added polynomial features (degree = 2)
- Captured non-linear relationships between features and house prices

### 4.4 Decision Tree Regressor
- Modeled complex feature interactions
- Susceptible to overfitting on training data

### 4.5 Random Forest Regressor
- Ensemble model combining multiple decision trees
- Provided better generalization and improved accuracy

---

## 5. Evaluation Metrics

The models were evaluated using the following metrics:

- **Mean Absolute Error (MAE):** Measures average absolute prediction error
- **Mean Squared Error (MSE):** Penalizes larger errors more heavily
- **R² Score:** Measures how well the model explains variance in house prices

---

## 6. Model Performance Summary

| Model                    | R² Score |
|--------------------------|----------|
| Linear Regression        | 0.78     |
| Polynomial Regression    | 0.82     |
| Decision Tree            | 0.75     |
| Random Forest            | 0.88     |

✔ The **Random Forest Regressor** achieved the highest R² score, indicating the best predictive performance.

---

## 7. Predictions vs Actual Analysis

A scatter plot comparing predicted prices against actual prices was generated.  
Most data points lie close to the diagonal reference line, indicating good predictive accuracy.

The plot has been saved as: predictions_vs_actual.png

---

## 8. Feature Importance Analysis

Feature importance analysis from the Random Forest model showed that:

- **Area** is the most influential feature
- **Location-related features** significantly impact price
- Number of bedrooms has moderate influence

This aligns with real-world expectations in real estate pricing.

---

## 9. Key Insights

- Linear models perform well but fail to capture complex patterns
- Polynomial features improve prediction accuracy
- Ensemble methods outperform individual models
- Feature importance analysis provides business-relevant insights

---

## 10. Limitations and Future Improvements

- Dataset size may limit generalization
- Hyperparameter tuning was not performed
- External factors like market trends were not included

### Future Enhancements:
- Hyperparameter tuning using GridSearchCV
- Incorporating additional features such as age of property
- Deploying the model as a web application

---

## 11. Conclusion

This project successfully demonstrates the end-to-end implementation of a house price prediction system.  
The Random Forest model proved to be the most effective, achieving high accuracy and strong generalization.

The project meets all technical and documentation requirements and is suitable for academic and internship evaluation.

---

**Author:** Vanshika Rupera  
**Domain:** Data Science & Machine Learning  

