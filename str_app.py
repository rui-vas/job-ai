import streamlit as st
import pandas as pd
import requests

# Fetch jobs from API
response = requests.get('http://127.0.0.1:5000/jobs')
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Display data in Streamlit
st.title('Job Dashboard')
st.dataframe(df)
