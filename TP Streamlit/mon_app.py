#run de l'app:
#streamlit run mon_app.py

#Import de librairies
import seaborn as sns
from pathlib import Path
import pandas as pd
import streamlit as st
#import plotly.express as px


@st.cache
def get_data():
   bikes_data_path = Path() / 'Seasons_Stats.csv'
   data = pd.read_csv(bikes_data_path)

df = get_data()
st.write(df)

st.title("Streamlit NBA datas")
st.header("Différentes infos")

if st.checkbox("Afficher Dataset"):
    nbligne = st.number_input("Nombre de ligne à afficher", step=1)
    st.dataframe(df.head(int(nbligne)))
    print (df)
    
if st.button("Nom de colonnes"):
    st.write(df.columns.tolist())
    st.table(df.dtypes)
