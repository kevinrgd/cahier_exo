import pandas as pd
import streamlit as st

# Charger le fichier Excel des exercices
file_path = "C:/Users/rigaud/OneDrive - ENS RENNES/Bureau/Paris FC/tableau_complet_exercices_paris_fc.xlsx"  # Mets ici le chemin vers ton fichier Excel
exercises_df = pd.read_excel(file_path)

# Titre de l'application
st.title("Cahier d'exercices du Paris FC")

# Description
st.write("""
Bienvenue dans l'application d'exercices du Paris FC. Utilisez les filtres pour rechercher des exercices en fonction de l'intensité, du thème ou du nombre de joueuses.
""")

# Créer des filtres interactifs
intensity = st.selectbox("Sélectionnez l'intensité", options=exercises_df['Intensité de travail'].unique())
theme = st.selectbox("Sélectionnez le thème", options=exercises_df['Thème de l\'exercice'].unique())
min_players = st.slider("Nombre minimum de joueuses", min_value=int(exercises_df['Nombre de joueuses'].min()), max_value=int(exercises_df['Nombre de joueuses'].max()), value=int(exercises_df['Nombre de joueuses'].min()))
surface = st.selectbox("Sélectionnez la surface de terrain", options=exercises_df['Surface de terrain'].unique())
ballons = st.slider("Nombre de ballons", min_value=int(exercises_df['Nombre de ballons'].min()), max_value=int(exercises_df['Nombre de ballons'].max()), value=int(exercises_df['Nombre de ballons'].min()))
equipes = st.slider("Nombre d'équipes", min_value=int(exercises_df['Nombre d\'équipes'].min()), max_value=int(exercises_df['Nombre d\'équipes'].max()), value=int(exercises_df['Nombre d\'équipes'].min()))
mode_marques = st.selectbox("Sélectionnez le mode de marques", options=exercises_df['Mode de marques'].unique())

# Filtrer le tableau en fonction des choix de l'utilisateur
filtered_df = exercises_df[
    (exercises_df['Intensité de travail'] == intensity) & 
    (exercises_df['Thème de l\'exercice'] == theme) &
    (exercises_df['Nombre de joueuses'] >= min_players) &
    (exercises_df['Surface de terrain'] == surface) &
    (exercises_df['Nombre de ballons'] >= ballons) &
    (exercises_df['Nombre d\'équipes'] >= equipes) &
    (exercises_df['Mode de marques'] == mode_marques)
]


# Afficher les résultats
st.write(f"Exercices trouvés : {len(filtered_df)}")
st.dataframe(filtered_df)

# Lancer l'application : dans ton terminal, tape la commande
# streamlit run chemin/vers/ton/script.py