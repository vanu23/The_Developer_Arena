# ===============================
# Interactive Sales Dashboard
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -------------------------------
# Styling
# -------------------------------
sns.set(style="whitegrid", palette="Set2")
plt.rcParams["figure.figsize"] = (10, 6)

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("D:\Developer Arena\week_6\sales_data.csv")

# -------------------------------
# Data Cleaning
# -------------------------------
df.drop_duplicates(inplace=True)

if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -------------------------------
# Seaborn Visualizations
# -------------------------------

# 1. Sales Trend
plt.figure()
sns.lineplot(data=df, x="Date", y="Total_Sales")
plt.title("Total Sales Trend Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.show()

# 2. Product-wise Sales
plt.figure()
sns.barplot(data=df, x="Product", y="Total_Sales", estimator=np.sum)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# 3. Box Plot (Sales Distribution)
plt.figure()
sns.boxplot(data=df, x="Product", y="Total_Sales")
plt.title("Total Sales Distribution by Product")
plt.xticks(rotation=45)
plt.show()

# 4. Violin Plot
plt.figure()
sns.violinplot(data=df, x="Product", y="Total_Sales")
plt.title("Total Sales Density by Product")
plt.xticks(rotation=45)
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(10, 6))
numeric_cols = df.select_dtypes(include="number")
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Plotly Interactive Visuals
# -------------------------------

# Interactive Sales Trend
fig1 = px.line(
    df,
    x="Date",
    y="Total_Sales",
    color="Product",
    title="Interactive Total Sales Trend by Product"
)
fig1.show()

# Product Performance
fig2 = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    title="Product-wise Total Sales Performance"
)
fig2.show()

# -------------------------------
# Combined Interactive Dashboard
# -------------------------------
fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Total Sales Trend",
        "Total Sales by Product",
        "Sales Distribution",
        "Total Sales vs Quantity"
    )
)

# Sales Trend
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Total_Sales"],
        mode="lines",
        name="Total Sales"
    ),
    row=1,
    col=1
)

# Product Sales
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()
fig.add_trace(
    go.Bar(
        x=product_sales["Product"],
        y=product_sales["Total_Sales"],
        name="Product Sales"
    ),
    row=1,
    col=2
)

# Sales Distribution
fig.add_trace(
    go.Box(
        y=df["Total_Sales"],
        name="Sales Distribution"
    ),
    row=2,
    col=1
)

# Sales vs Quantity
if "Quantity" in df.columns:
    fig.add_trace(
        go.Scatter(
            x=df["Quantity"],
            y=df["Total_Sales"],
            mode="markers",
            name="Quantity vs Total Sales"
        ),
        row=2,
        col=2
    )

fig.update_layout(
    height=800,
    title="Interactive Sales Dashboard",
    showlegend=True
)

fig.show()

# -------------------------------
# Insights Summary
# -------------------------------
print("""
KEY INSIGHTS:
1. Total sales show clear trends over time.
2. Certain products consistently generate higher revenue.
3. Sales distribution varies significantly across products.
4. Quantity sold has a strong influence on total sales.
5. Interactive dashboards improve exploratory analysis.
""")
