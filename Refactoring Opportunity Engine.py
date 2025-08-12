
import streamlit as st
import pandas as pd

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

# Display bar chart for Effort scores
st.subheader("Effort Scores")
effort_chart_data = pd.DataFrame({'Anti-Pattern': df['Anti-Pattern'], 'Effort': df['Effort']})
effort_chart_data.set_index('Anti-Pattern', inplace=True)
st.bar_chart(effort_chart_data)

# Display bar chart for Impact scores
st.subheader("Impact Scores")
impact_chart_data = pd.DataFrame({'Anti-Pattern': df['Anti-Pattern'], 'Impact': df['Impact']})
impact_chart_data.set_index('Anti-Pattern', inplace=True)
st.bar_chart(impact_chart_data)
