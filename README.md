# Big-Mart-Retail-Analytics
Interactive Big Mart Retail Analytics Dashboard using Python, Pandas, Plotly and Streamlit.
# 🛒 Big Mart Retail Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)

An interactive Retail Analytics Dashboard developed using **Python, Pandas, Plotly, and Streamlit** to explore product categories, pricing patterns, outlet distribution, and product visibility using the Big Mart cleaned dataset.

---

## 📌 Project Overview

This project focuses on analyzing Big Mart retail data through an interactive dashboard. It helps users explore product and outlet-level patterns, compare pricing across categories, and generate useful business insights using dynamic filters and visualizations.

---

## 🚀 Key Features

- Interactive dashboard with KPI metrics
- Product category analysis
- Outlet type and location analysis
- Fat content distribution
- Product visibility vs. MRP analysis
- Product pricing distribution
- Top 10 products by MRP
- Dynamic sidebar filters
- Business insights based on filtered data
- Product search and data exploration
- Download filtered dataset as CSV

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| Pandas     | Data manipulation and analysis |
| NumPy      | Numerical computations |
| Plotly     | Interactive visualizations |
| Streamlit  | Web dashboard framework |

---

## 📂 Project Structure

```text
Big-Mart-Retail-Analytics/
│
├── app.py
├── Big_Mart_Cleaned.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Information

| Attribute      | Details                  |
|----------------|--------------------------|
| Dataset        | Big Mart Cleaned Dataset |
| Total Records  | 5,681                    |
| Total Columns  | 11                       |
| Format         | CSV                      |

The dataset includes product identifiers, item weight, fat content, visibility, product type, MRP, outlet identifiers, establishment year, outlet size, location type, and outlet type.

---

## 📈 Dashboard KPIs

- Total Records
- Unique Products
- Total Outlets
- Average MRP
- Product Categories
- Average Visibility
- Average Weight
- Median MRP

---

## 💡 Business Analysis

The dashboard provides insights into:

- Product category distribution
- Average product pricing
- Outlet type distribution
- Outlet location patterns
- Fat content distribution
- Product visibility and pricing relationships
- Highest-priced products

> **Note:** The dataset does not contain an `Item_Outlet_Sales` column. Therefore, this dashboard focuses on product pricing, distribution, and outlet profiles rather than actual sales revenue.

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR-USERNAME/Big-Mart-Retail-Analytics.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd Big-Mart-Retail-Analytics
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment

This dashboard can be deployed using **Streamlit Community Cloud**:

1. Push the project to a GitHub repository.
2. Connect the repository on [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Select `app.py` as the main application file.
4. Click **Deploy**.

---

## 👨‍💻 Developed By

**Shubham Maity**
B.Tech | Artificial Intelligence & Machine Learning

**Project:** Big Mart Retail Analytics Dashboard
Developed as part of the Business Analytics Internship at **Sysslan IT Solutions**.
