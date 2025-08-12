import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data representing SQL anti-patterns in Snowflake
data = [
    {"Anti-Pattern": "SELECT *", "Description": "Fetches all columns, increasing compute and storage costs.", "Severity": "High", "Frequency": 45},
    {"Anti-Pattern": "JOIN Explosion", "Description": "Poor join logic leads to massive intermediate datasets.", "Severity": "High", "Frequency": 30},
    {"Anti-Pattern": "COUNT(*) in Outer Joins", "Description": "Misleading counts due to NULLs.", "Severity": "Medium", "Frequency": 25},
    {"Anti-Pattern": "Scalar Subqueries in SELECT", "Description": "Reduces readability and performance.", "Severity": "Medium", "Frequency": 20},
    {"Anti-Pattern": "Filtering on Non-Preserved Side of OUTER JOIN", "Description": "Converts OUTER JOIN to INNER JOIN unintentionally.", "Severity": "Medium", "Frequency": 15},
    {"Anti-Pattern": "Using Cursors Instead of Set-Based Operations", "Description": "Inefficient and slow.", "Severity": "High", "Frequency": 10},
    {"Anti-Pattern": "Hardcoding Values", "Description": "Reduces flexibility and increases risk.", "Severity": "Low", "Frequency": 35},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.set_page_config(page_title="Snowflake SQL Anti-Patterns Dashboard", layout="wide")

st.title("❄️ Snowflake SQL Anti-Patterns Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
severity_filter = st.sidebar.multiselect("Select Severity Level", options=df["Severity"].unique(), default=df["Severity"].unique())

# Filter data based on selection
filtered_df = df[df["Severity"].isin(severity_filter)]

# Display table of anti-patterns
st.subheader("📋 Anti-Patterns Table")
st.dataframe(filtered_df, use_container_width=True)

# Bar chart: Frequency of anti-patterns
st.subheader("📊 Frequency of Anti-Patterns")
fig_freq = px.bar(filtered_df, x="Anti-Pattern", y="Frequency", color="Severity", title="Frequency by Anti-Pattern")
st.plotly_chart(fig_freq, use_container_width=True)

# Pie chart: Distribution by severity
st.subheader("🧮 Severity Distribution")
severity_counts = filtered_df["Severity"].value_counts().reset_index()
severity_counts.columns = ["Severity", "Count"]
fig_severity = px.pie(severity_counts, names="Severity", values="Count", title="Severity Distribution")
st.plotly_chart(fig_severity, use_container_width=True)

