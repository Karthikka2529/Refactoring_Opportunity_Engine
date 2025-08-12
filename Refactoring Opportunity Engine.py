
import streamlit as st
import pandas as pd
import seaborn as sns

# Set the title of the Streamlit app
st.title("SQL Anti-Pattern Detection Dashboard")

# Sample data for anti-patterns and recommendations
data = {
    'Anti-Pattern': ['SELECT *', 'Nested Views', 'Redundant Joins'],
    'Recommendation': ['Use explicit column names', 'Flatten views', 'Optimize joins'],
    'Effort': [2, 4, 3],  # Scale: 1 (Low) to 5 (High)
    'Impact': [5, 4, 3]   # Scale: 1 (Low) to 5 (High)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the data table
st.subheader("Detected Anti-Patterns and Recommendations")
st.dataframe(df)

# Scatter plot: Effort vs Impact
st.subheader("Effort vs Impact of Recommendations")
scatter_plot = sns.scatterplot(data=df, x='Effort', y='Impact', hue='Recommendation', s=100)
for i in range(len(df)):
    scatter_plot.text(df['Effort'][i]+0.05, df['Impact'][i], df['Anti-Pattern'][i], fontsize=9)
st.pyplot(scatter_plot.figure)

# Bar chart: Impact of Anti-Patterns
st.subheader("Impact of Anti-Patterns")
bar_plot = sns.barplot(data=df, x='Anti-Pattern', y='Impact', hue='Effort')
st.pyplot(bar_plot.figure)
