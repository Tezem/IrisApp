import streamlit as st
import pandas as pd
# Charger le fichier CSV
file_path = "iris.csv"  # Assurez-vous que le fichier est dans le bon dossier
df = pd.read_csv(file_path)

# Afficher les 5 premières lignes
print(df.head())

# Informations générales sur les données
print(df.info())

# Statistiques descriptives
print(df.describe())

# Vérification des valeurs manquantes
print(df.isnull().sum())
st.write("Hello world !")
