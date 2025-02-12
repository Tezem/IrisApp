import streamlit as st
import pandas as pd
import os

# Définir le chemin correct
file_path = os.path.join(os.path.dirname(__file__), "data", "iris.csv")

# Vérifier si le fichier existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Fichier introuvable : {file_path}")

# Charger les données
df = pd.read_csv(file_path)
print(df.head())
st.write("Hello world !")
