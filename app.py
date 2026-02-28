import streamlit as st
import pandas as pd
import plotly.express as px
import json
import base64

# -----------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(page_title="PhonePe Transaction Analyzer", layout="wide")

# -----------------------------
# LOAD LOGO AS BASE64
# -----------------------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("phnoepay.png")

# -----------------------------
# CUSTOM LIGHT THEME + WATERMARK
# -----------------------------
st.markdown(f"""
<style>

/* Full app background */
.stApp {{
    background-color: #f5f0ff;
}}

/* Watermark Logo */
.stApp::before {{
    content: "";
    background: url("data:image/png;base64,{img_base64}");
    background-repeat: no-repeat;
    background-position: center;
    background-size: 35%;
    opacity: 0.08;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background-color: #ffffff;
}}

/* KPI Cards */
div[data-testid="metric-container"] {{
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
#st.title("📊 State Wise Transaction Analyzer")

st.title("📊 State Wise Transaction Analyzer")

# Load Data
df = pd.read_csv("aggregated_transactions.csv")

# -----------------------------
# CLEAN STATE NAMES (IMPORTANT)
# -----------------------------

# Convert slug format to proper title case
df["State"] = df["State"].str.replace("-", " ")
df["State"] = df["State"].str.title()

# Handle special cases manually
df["State"] = df["State"].replace({
    "Andaman & Nicobar Islands": "Andaman And Nicobar",
    "Dadra & Nagar Haveli & Daman & Diu": "Dadra And Nagar Haveli And Daman And Diu",
    "Jammu & Kashmir": "Jammu And Kashmir",
    "Delhi": "Delhi",
    "Odisha": "Odisha"
})

# Sidebar Filters
st.sidebar.header("Filter Options")

state = st.sidebar.selectbox("Select State", sorted(df["State"].unique()))
year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))
quarter = st.sidebar.selectbox("Select Quarter", sorted(df["Quarter"].unique()))

# Filter Data
filtered_df = df[
    (df["State"] == state) &
    (df["Year"] == year) &
    (df["Quarter"] == quarter)
]

# KPI Section
total_amount = filtered_df["Transaction_amount"].sum()
total_count = filtered_df["Transaction_count"].sum()

col1, col2 = st.columns(2)

col1.metric("Total Transaction Amount", f"₹ {total_amount:,.0f}")
col2.metric("Total Transaction Count", f"{total_count:,.0f}")

# -----------------------------
# BAR CHART
# -----------------------------

st.subheader("Transaction Type Distribution")

fig_bar = px.bar(
    filtered_df,
    x="Transaction_type",
    y="Transaction_amount",
    color="Transaction_type"
)

st.plotly_chart(fig_bar, use_container_width=True)

# -----------------------------
# LINE CHART
# -----------------------------

st.subheader("Quarterly Transaction Trend")

trend_df = df[
    (df["State"] == state) &
    (df["Year"] == year)
]

fig_line = px.line(
    trend_df,
    x="Quarter",
    y="Transaction_amount",
    markers=True
)

st.plotly_chart(fig_line, use_container_width=True)

# -----------------------------
# INDIA MAP
# -----------------------------

# -----------------------------
# INDIA MAP (Filtered)
# -----------------------------

st.subheader("State Wise Transaction Map")

with open("india_state.geojson") as f:
    geojson = json.load(f)

# Use filtered data instead of full data
map_df = df.groupby("State", as_index=False)["Transaction_amount"].sum()

# Add highlight column
map_df["Highlight"] = map_df["State"].apply(
    lambda x: "Selected State" if x == state else "Other States"
)

fig_map = px.choropleth(
    map_df,
    geojson=geojson,
    featureidkey="properties.NAME_1",
    locations="State",
    color="Highlight",  # color based on highlight
    color_discrete_map={
        "Selected State": "red",
        "Other States": "lightgrey"
    }
)

fig_map.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig_map, use_container_width=True)