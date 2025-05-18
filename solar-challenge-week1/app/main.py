import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    benin = pd.read_csv('src/data/benin_clean.csv')
    sierra = pd.read_csv('src/data/sierraleone_clean.csv')
    togo = pd.read_csv('src/data/togo_clean.csv')
    benin['country'] = 'Benin'
    sierra['country'] = 'Sierra Leone'
    togo['country'] = 'Togo'
    return pd.concat([benin, sierra, togo])

df = load_data()

# Sidebar filters
st.sidebar.header('Filters')
selected_countries = st.sidebar.multiselect(
    'Select countries',
    ['Benin', 'Sierra Leone', 'Togo'],
    default=['Benin', 'Sierra Leone', 'Togo']
)

selected_metric = st.sidebar.selectbox(
    'Select metric',
    ['GHI', 'DNI', 'DHI', 'Tamb']
)

# Filter data
filtered_df = df[df['country'].isin(selected_countries)]

# Main content
st.title('Solar Potential Comparison Dashboard')

# Boxplot
st.header(f'{selected_metric} Distribution')
fig, ax = plt.subplots(figsize=(10,6))
sns.boxplot(data=filtered_df, x='country', y=selected_metric, ax=ax)
st.pyplot(fig)

# Summary table
st.header('Summary Statistics')
st.dataframe(
    filtered_df.groupby('country')[selected_metric].describe()
)

# Top regions
st.header('Top Measurements')
top_n = st.slider('Number of top measurements to show', 5, 50, 10)
st.dataframe(
    filtered_df.nlargest(top_n, selected_metric)[['country', selected_metric, 'Timestamp']]
)