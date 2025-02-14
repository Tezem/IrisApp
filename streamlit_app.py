import streamlit as st
from sklearn.model_selection import train_test_split

st.write("Hello world !")

# Séparer les caractéristiques et la cible
X = df.drop('species', axis=1)
y = df['species']
