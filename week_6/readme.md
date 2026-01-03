# 📊 Interactive Sales Dashboard

## 📌 Project Overview
The Interactive Sales Dashboard project focuses on analyzing and visualizing sales data using
both static and interactive visualizations. The dashboard helps understand **sales trends,
category-wise performance, product contribution, and quantity impact on sales**.

The project uses **Seaborn** for statistical analysis and **Plotly** for interactive dashboard
elements, making it suitable for business reporting and decision-making.

---

## 🎯 Project Objectives
- Analyze sales trends over time
- Compare performance across product categories
- Identify high-performing products
- Understand sales distribution and variability
- Build an interactive dashboard for exploratory analysis

---

## 🗂️ Dataset Description
The dataset contains transactional sales data with the following key columns:

| Column Name   | Description |
|--------------|------------|
| Order_Date   | Date of the sales transaction |
| Category     | Product category |
| Product      | Product name |
| Sales        | Total sales amount |
| Quantity     | Number of units sold |

> ⚠️ Note: The dataset does **not** include a Profit column. All analysis is strictly based on available data.

---

## 🛠️ Tools & Technologies
- **Python**
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Statistical visualizations
- **Plotly** – Interactive charts and dashboards
- **Jupyter Notebook**

---

## 📁 Project Structure
Interactive-Sales-Dashboard/
│
├── dashboard.ipynb # Main analysis and dashboard notebook
├── dashboard.py # Python script version
├── requirements.txt # Project dependencies
├── visualizations/ # Saved charts and screenshots
├── dashboard_demo.gif # Dashboard interaction demo
└── README.md # Project documentation


---

## ⚙️ Setup Instructions
1. Clone the repository
2. Install required libraries: pip install -r requirements.txt
3. Open Jupyter Notebook: jupyter notebook dashboard.ipynb or run: python dashboard.py


---

## 📊 Visualizations Included

### Static Visualizations (Seaborn)
- Line chart – Sales trend over time
- Bar chart – Category-wise sales
- Box plot – Sales distribution by category
- Violin plot – Sales density and variability
- Histogram – Sales frequency distribution
- Correlation heatmap – Relationship between numeric features

### Interactive Visualizations (Plotly)
- Interactive sales trend with hover effects
- Category-wise sales comparison
- Product performance analysis
- Sales vs Quantity scatter plot
- Multi-panel interactive dashboard

---

## 📈 Dashboard Insights
- Sales show clear trends over time with periodic fluctuations
- Certain categories consistently outperform others
- Sales distribution varies significantly across categories
- Quantity sold has a strong influence on total sales
- A small number of products contribute a large share of revenue

---

## 🧪 Testing & Validation
- Missing values checked and handled
- Duplicate records removed
- Date column converted to datetime format
- Visual outputs validated for accuracy
- Interactive elements tested for responsiveness

---

## 🧠 Business Use Case
This dashboard can be used by:
- Sales teams to monitor performance
- Managers to identify top categories and products
- Analysts for exploratory sales analysis
- Stakeholders for data-driven decision making

---

## 👩‍💻 Author
**Vanshika Rupera**  
Data Analyst | Python | Data Visualization | Machine Learning



