import pandas as pd
import streamlit as st

# Ajouter le logo du Paris FC
st.image("data:image/jpeg;base64,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", width=150)

# Titre de l'application avec la couleur du Paris FC (bleu foncé)
st.markdown("<h1 style='text-align: center; color: #003366;'>Cahier d'exercices du Paris FC</h1>", unsafe_allow_html=True)

# Description avec fond blanc et texte bleu foncé
st.markdown("""
<div style="background-color: #FFFFFF; padding: 10px; border-radius: 5px">
    <h2 style="color: #003366;">Bienvenue dans l'application d'exercices du Paris FC.</h2>
    <p>Utilisez les filtres pour rechercher des exercices en fonction de l'intensité, du thème ou du nombre de joueuses.</p>
</div>
""", unsafe_allow_html=True)

# Charger le fichier Excel via un téléverseur
uploaded_file = st.file_uploader("Téléchargez le fichier Excel des exercices", type=["xlsx"])

if uploaded_file is not None:
    # Lire le fichier Excel
    exercises_df = pd.read_excel(uploaded_file)

    # Créer des filtres interactifs uniquement si un fichier est téléversé
    st.markdown("<h3 style='color: #003366;'>🎯 Sélectionnez vos critères :</h3>", unsafe_allow_html=True)
    
    intensity = st.selectbox("💪 Sélectionnez l'intensité", options=exercises_df['Intensité de travail'].unique())
    theme = st.selectbox("🎯 Sélectionnez le thème", options=exercises_df['Thème de l\'exercice'].unique())
    min_players = st.slider("👥 Nombre minimum de joueuses", min_value=int(exercises_df['Nombre de joueuses'].min()), max_value=int(exercises_df['Nombre de joueuses'].max()), value=int(exercises_df['Nombre de joueuses'].min()))
    surface = st.selectbox("🏟️ Sélectionnez la surface de terrain", options=exercises_df['Surface de terrain'].unique())
    ballons = st.slider("⚽ Nombre de ballons", min_value=int(exercises_df['Nombre de ballons'].min()), max_value=int(exercises_df['Nombre de ballons'].max()), value=int(exercises_df['Nombre de ballons'].min()))
    equipes = st.slider("👥 Nombre d'équipes", min_value=int(exercises_df['Nombre d\'équipes'].min()), max_value=int(exercises_df['Nombre d\'équipes'].max()), value=int(exercises_df['Nombre d\'équipes'].min()))
    mode_marques = st.selectbox("🥅 Sélectionnez le mode de marques", options=exercises_df['Mode de marques'].unique())

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
    st.markdown(f"<h4 style='color: #003366;'>Exercices trouvés : {len(filtered_df)}</h4>", unsafe_allow_html=True)
    st.dataframe(filtered_df)
else:
    st.markdown("<h4 style='color: #FF0000;'>Veuillez téléverser un fichier Excel pour voir les exercices.</h4>", unsafe_allow_html=True)


