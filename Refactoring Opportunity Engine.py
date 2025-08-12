
import streamlit as st
import pandas as pd
import plotly.express as px

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

# Create a scatter plot for effort vs impact
fig_scatter = px.scatter(df, x='Effort', y='Impact', text='Anti-Pattern',
                         color='Recommendation', size=[10]*len(df),
                         labels={'Effort': 'Effort Score', 'Impact': 'Impact Score'},
                         title='Effort vs Impact of Recommendations')

# Show the scatter plot
st.plotly_chart(fig_scatter)

# Create a bar chart for impact scores
fig_bar = px.bar(df, x='Anti-Pattern', y='Impact', color='Effort',
                 labels={'Impact': 'Impact Score', 'Effort': 'Effort Score'},
                 title='Impact of Anti-Patterns')

# Show the bar chart
st.plotly_chart(fig_bar)
