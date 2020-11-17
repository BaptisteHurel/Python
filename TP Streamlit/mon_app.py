#run de l'app:
#streamlit run mon_app.py

#Import de librairies
import seaborn as sns
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache
def get_data():
    return pd.read_csv("https://github.com/BaptisteHurel/Python/blob/master/CSV/player_data.csv")

df = get_data()
st.write(df)


st.title("Streamlit NBA datas")
st.header("Différentes infos")
st.button("Simple Button")
st.text("Une check box")

















if st.checkbox("Show DataSet"):
    number = st.number_input("Number of Rows to View")
    st.dataframe(df.head(int(number)))


if st.button("Columns Names"):
    st.write(df.columns.tolist())
