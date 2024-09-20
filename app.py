import pandas as pd
import streamlit as st

# Ajouter le logo du Paris FC
st.image("https://parisfc.fr/wp-content/uploads/bis-images/48453/Logo-Paris-FC1-1400x700-f50_50.jpg", width=300)

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

    # Ajouter "Toutes les options" à chaque sélection
    st.markdown("<h3 style='color: #003366;'>🎯 Sélectionnez vos critères (ou laissez 'Toutes les options') :</h3>", unsafe_allow_html=True)
    
    intensity_options = ["Toutes les options"] + list(exercises_df['Intensité de travail'].unique())
    intensity = st.selectbox("💪 Sélectionnez l'intensité", options=intensity_options)

    theme_options = ["Toutes les options"] + list(exercises_df['Thème de l\'exercice'].unique())
    theme = st.selectbox("🎯 Sélectionnez le thème", options=theme_options)

    surface_options = ["Toutes les options"] + list(exercises_df['Surface de terrain'].unique())
    surface = st.selectbox("🏟️ Sélectionnez la surface de terrain", options=surface_options)

    ballons = st.slider("⚽ Nombre de ballons", min_value=int(exercises_df['Nombre de ballons'].min()), max_value=int(exercises_df['Nombre de ballons'].max()), value=int(exercises_df['Nombre de ballons'].min()))
    
    equipes = st.slider("👥 Nombre d'équipes", min_value=int(exercises_df['Nombre d\'équipes'].min()), max_value=int(exercises_df['Nombre d\'équipes'].max()), value=int(exercises_df['Nombre d\'équipes'].min()))

    mode_marques_options = ["Toutes les options"] + list(exercises_df['Mode de marques'].unique())
    mode_marques = st.selectbox("🥅 Sélectionnez le mode de marques", options=mode_marques_options)

    # Appliquer les filtres uniquement si l'utilisateur ne choisit pas "Toutes les options"
    filtered_df = exercises_df.copy()
    
    if intensity != "Toutes les options":
        filtered_df = filtered_df[filtered_df['Intensité de travail'] == intensity]
    
    if theme != "Toutes les options":
        filtered_df = filtered_df[filtered_df['Thème de l\'exercice'] == theme]
    
    if surface != "Toutes les options":
        filtered_df = filtered_df[filtered_df['Surface de terrain'] == surface]

    if mode_marques != "Toutes les options":
        filtered_df = filtered_df[filtered_df['Mode de marques'] == mode_marques]
    
    # Appliquer les filtres pour les sliders (Nombre de ballons et Nombre d'équipes)
    filtered_df = filtered_df[
        (filtered_df['Nombre de ballons'] >= ballons) &
        (filtered_df['Nombre d\'équipes'] >= equipes)
    ]

    # Afficher les résultats
    st.markdown(f"<h4 style='color: #003366;'>Exercices trouvés : {len(filtered_df)}</h4>", unsafe_allow_html=True)
    st.dataframe(filtered_df)

else:
    st.markdown("<h4 style='color: #FF0000;'>Veuillez téléverser un fichier Excel pour voir les exercices.</h4>", unsafe_allow_html=True)
