
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Big Mart Retail Analytics",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------
# CUSTOM STYLING
# --------------------------------

st.markdown("""
<style>
.main-title {
    font-size: 34px;
    font-weight: bold;
}
.subtitle {
    color: gray;
    font-size: 16px;
}
div[data-testid="stMetric"] {
    background-color: #F5F7FA;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# LOAD DATASET
# --------------------------------

@st.cache_data
def load_data():
    file_path = Path(__file__).parent / "Big_Mart_Cleaned.csv"
    data = pd.read_csv(file_path)
    return data

df = load_data()

# --------------------------------
# HEADER
# --------------------------------

st.markdown(
    '<p class="main-title">🛒 Big Mart Retail Analytics Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Business Analytics Internship | Sysslan IT Solutions</p>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------
# SIDEBAR FILTERS
# --------------------------------

st.sidebar.title("Dashboard Filters")

categories = st.sidebar.multiselect(
    "Product Category",
    sorted(df["Item_Type"].dropna().unique()),
    default=sorted(df["Item_Type"].dropna().unique())
)

outlets = st.sidebar.multiselect(
    "Outlet",
    sorted(df["Outlet_Identifier"].dropna().unique()),
    default=sorted(df["Outlet_Identifier"].dropna().unique())
)

outlet_types = st.sidebar.multiselect(
    "Outlet Type",
    sorted(df["Outlet_Type"].dropna().unique()),
    default=sorted(df["Outlet_Type"].dropna().unique())
)

fat_types = st.sidebar.multiselect(
    "Fat Content",
    sorted(df["Item_Fat_Content"].dropna().unique()),
    default=sorted(df["Item_Fat_Content"].dropna().unique())
)

min_mrp = float(df["Item_MRP"].min())
max_mrp = float(df["Item_MRP"].max())

mrp_range = st.sidebar.slider(
    "MRP Range",
    min_value=min_mrp,
    max_value=max_mrp,
    value=(min_mrp, max_mrp)
)

# --------------------------------
# APPLY FILTERS
# --------------------------------

filtered_df = df[
    df["Item_Type"].isin(categories) &
    df["Outlet_Identifier"].isin(outlets) &
    df["Outlet_Type"].isin(outlet_types) &
    df["Item_Fat_Content"].isin(fat_types) &
    df["Item_MRP"].between(mrp_range[0], mrp_range[1])
].copy()

if filtered_df.empty:
    st.warning("No data found. Please change your filters.")
    st.stop()

# --------------------------------
# KPI SECTION
# --------------------------------

st.subheader("📊 Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Records",
    f"{len(filtered_df):,}"
)

c2.metric(
    "Unique Products",
    f"{filtered_df['Item_Identifier'].nunique():,}"
)

c3.metric(
    "Total Outlets",
    f"{filtered_df['Outlet_Identifier'].nunique():,}"
)

c4.metric(
    "Average MRP",
    f"₹{filtered_df['Item_MRP'].mean():,.2f}"
)

c5, c6, c7, c8 = st.columns(4)

c5.metric(
    "Categories",
    filtered_df["Item_Type"].nunique()
)

c6.metric(
    "Average Visibility",
    f"{filtered_df['Item_Visibility'].mean():.4f}"
)

c7.metric(
    "Average Weight",
    f"{filtered_df['Item_Weight'].mean():.2f}"
)

c8.metric(
    "Median MRP",
    f"₹{filtered_df['Item_MRP'].median():,.2f}"
)

st.divider()

# --------------------------------
# CATEGORY ANALYSIS
# --------------------------------

st.subheader("📦 Product Category Analysis")

category_data = (
    filtered_df.groupby("Item_Type")
    .agg(
        Product_Records=("Item_Identifier", "count"),
        Average_MRP=("Item_MRP", "mean")
    )
    .reset_index()
)

col1, col2 = st.columns(2)

with col1:

    fig1 = px.bar(
        category_data.sort_values(
            "Product_Records", ascending=False
        ),
        x="Item_Type",
        y="Product_Records",
        color="Product_Records",
        title="Product Distribution by Category"
    )

    fig1.update_layout(
        template="plotly_white",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    fig2 = px.bar(
        category_data.sort_values(
            "Average_MRP", ascending=False
        ),
        x="Item_Type",
        y="Average_MRP",
        color="Average_MRP",
        title="Average MRP by Category"
    )

    fig2.update_layout(
        template="plotly_white",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------
# OUTLET ANALYSIS
# --------------------------------

st.subheader("🏬 Outlet Analysis")

col3, col4 = st.columns(2)

outlet_data = (
    filtered_df.groupby("Outlet_Type")
    .agg(
        Product_Records=("Item_Identifier", "count"),
        Average_MRP=("Item_MRP", "mean")
    )
    .reset_index()
)

with col3:

    fig3 = px.bar(
        outlet_data,
        x="Outlet_Type",
        y="Product_Records",
        color="Outlet_Type",
        title="Product Records by Outlet Type"
    )

    fig3.update_layout(template="plotly_white")

    st.plotly_chart(fig3, use_container_width=True)

with col4:

    location_data = (
        filtered_df["Outlet_Location_Type"]
        .value_counts()
        .reset_index()
    )

    location_data.columns = ["Location", "Count"]

    fig4 = px.pie(
        location_data,
        names="Location",
        values="Count",
        hole=0.4,
        title="Location Distribution"
    )

    st.plotly_chart(fig4, use_container_width=True)

# --------------------------------
# FAT CONTENT ANALYSIS
# --------------------------------

st.subheader("🥗 Fat Content Distribution")

fat_data = (
    filtered_df["Item_Fat_Content"]
    .value_counts()
    .reset_index()
)

fat_data.columns = ["Fat_Content", "Count"]

fig5 = px.pie(
    fat_data,
    names="Fat_Content",
    values="Count",
    hole=0.4,
    title="Low Fat vs Regular"
)

st.plotly_chart(fig5, use_container_width=True)

# --------------------------------
# VISIBILITY ANALYSIS
# --------------------------------

st.subheader("👁️ Product Visibility Analysis")

fig6 = px.scatter(
    filtered_df,
    x="Item_Visibility",
    y="Item_MRP",
    color="Item_Type",
    hover_data=[
        "Item_Identifier",
        "Outlet_Identifier"
    ],
    title="Item Visibility vs MRP"
)

fig6.update_layout(template="plotly_white")

st.plotly_chart(fig6, use_container_width=True)

# --------------------------------
# MRP DISTRIBUTION
# --------------------------------

st.subheader("💰 Product Pricing Distribution")

fig7 = px.histogram(
    filtered_df,
    x="Item_MRP",
    nbins=35,
    title="MRP Distribution"
)

st.plotly_chart(fig7, use_container_width=True)

# --------------------------------
# TOP PRODUCTS
# --------------------------------

st.subheader("🏆 Top 10 Products by MRP")

top_products = (
    filtered_df.sort_values(
        "Item_MRP", ascending=False
    )
    [[
        "Item_Identifier",
        "Item_Type",
        "Item_MRP",
        "Outlet_Identifier"
    ]]
    .head(10)
)

st.dataframe(
    top_products,
    use_container_width=True,
    hide_index=True
)

# --------------------------------
# BUSINESS INSIGHTS
# --------------------------------

st.subheader("💡 Business Insights")

top_category = (
    filtered_df["Item_Type"].value_counts().idxmax()
)

highest_mrp_category = (
    category_data.sort_values(
        "Average_MRP", ascending=False
    ).iloc[0]["Item_Type"]
)

top_outlet_type = (
    filtered_df["Outlet_Type"].value_counts().idxmax()
)

st.markdown(f"""
- **Most represented category:** {top_category}
- **Highest average MRP category:** {highest_mrp_category}
- **Most represented outlet type:** {top_outlet_type}
- **Average MRP:** ₹{filtered_df['Item_MRP'].mean():.2f}
""")

st.info(
    "This dataset does not contain Item_Outlet_Sales. "
    "Therefore, the dashboard presents product pricing, "
    "distribution and outlet profiles, not actual sales revenue."
)

# --------------------------------
# PRODUCT SEARCH
# --------------------------------

st.subheader("🔎 Product Explorer")

search = st.text_input(
    "Search Product Identifier"
)

if search:

    search_df = filtered_df[
        filtered_df["Item_Identifier"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

else:

    search_df = filtered_df

st.dataframe(
    search_df,
    use_container_width=True,
    hide_index=True
)

# --------------------------------
# DOWNLOAD DATA
# --------------------------------

st.subheader("📥 Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV",
    data=csv,
    file_name="filtered_big_mart_data.csv",
    mime="text/csv"
)

st.divider()

st.caption(
    "Developed using Python, Pandas, Plotly and Streamlit | Sysslan IT Solutions"
)
