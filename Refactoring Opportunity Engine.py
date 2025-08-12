
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x='Effort', y='Impact', hue='Recommendation', s=100, ax=ax1)
for i in range(len(df)):
    ax1.text(df['Effort'][i]+0.05, df['Impact'][i], df['Anti-Pattern'][i], fontsize=9)
ax1.set_xlabel('Effort Score')
ax1.set_ylabel('Impact Score')
st.pyplot(fig1)

# Bar chart: Impact of Anti-Patterns
st.subheader("Impact of Anti-Patterns")
fig2, ax2 = plt.subplots()
sns.barplot(data=df, x='Anti-Pattern', y='Impact', hue='Effort', ax=ax2)
ax2.set_ylabel('Impact Score')
st.pyplot(fig2)
