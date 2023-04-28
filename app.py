import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Charger le modèle entraîné
model = pickle.load(open('data/best_model.pkl', 'rb'))

st.title("Mon application de prédiction des prix des voitures")

# Créez des champs pour recueillir les données d'entrée
input_feature_1 = st.number_input("Caractéristique 1", value=0)
input_feature_2 = st.number_input("Caractéristique 2", value=0)
# Ajoutez d'autres champs pour les autres caractéristiques

# Mettez les caractéristiques d'entrée dans un DataFrame
input_data = pd.DataFrame({
    "feature_1": [input_feature_1],
    "feature_2": [input_feature_2],
    # Ajoutez d'autres caractéristiques ici
})

# Lorsque l'utilisateur clique sur le bouton, effectuez une prédiction
if st.button("Prédire le prix"):
    prediction = model.predict(input_data)
    st.write(f"Le prix prédit est : {prediction[0]:.2f}")
