import streamlit as st
import pandas as pd
import numpy as np
import pickle

#charger le .csv 

df = pd.read_csv('data/cars_cleaned.csv')

# Charger le modèle entraîné
model = pickle.load(open('data/best_model.pkl', 'rb'))

st.title("Mon application de prédiction des prix des voitures")

# Créer des dictionnaires pour les valeurs de catégorie

def create_dictionaries():
    marque_dict = {
        i: marque for i, marque in enumerate([
            'alfa-romeo', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar',
            'mazda', 'buick', 'mercury', 'mitsubishi', 'nissan', 'peugeot', 'plymouth',
            'porsche', 'renault', 'saab', 'subaru', 'toyota', 'volkswagen', 'volvo'
        ])
    }

    modele_dict = {
        i: modele for i, modele in enumerate([
            'giulia', 'stelvio', 'Quadrifoglio', '100 ls', '100ls', 'fox', '5000', '4000',
            '5000s (diesel)', '320i', 'x1', 'x3', 'z4', 'x4', 'x5', 'impala', 'monte carlo',
            'vega 2300', 'rampage', 'challenger se', 'd200', 'monaco (sw)', 'colt hardtop',
            'colt (sw)', 'coronet custom', 'dart custom', 'coronet custom (sw)', 'civic',
            'civic cvcc', 'accord cvcc', 'accord lx', 'civic 1500 gl', 'accord',
            'civic 1300', 'prelude', 'civic (auto)', 'MU-X', 'D-Max ', 'D-Max V-Cross',
            'xj', 'xf', 'xk', 'rx3', 'glc deluxe', 'rx2 coupe', 'rx-4', '626', 'glc',
            'rx-7 gs', 'glc 4', 'glc custom l', 'glc custom', 'electra 225 custom',
            'century luxus (sw)', 'century', 'skyhawk', 'opel isuzu deluxe', 'skylark',
            'century special', 'regal sport coupe (turbo)', 'cougar', 'mirage', 'lancer',
            'outlander', 'g4', 'mirage g4', 'montero', 'pajero', 'versa', 'gt-r', 'rogue',
            'latio', 'titan', 'leaf', 'juke', 'note', 'clipper', 'nv200', 'dayz', 'fuga',
            'otti', 'teana', 'kicks', '504', '304', '504 (sw)', '604sl', '505s turbo diesel',
            'fury iii', 'cricket', 'satellite custom (sw)', 'fury gran sedan', 'valiant',
            'duster', 'macan', 'panamera', 'cayenne', 'boxter', '12tl', '5 gtl', '99e',
            '99le', '99gle', None, 'dl', 'brz', 'baja', 'r1', 'r2', 'trezia', 'tribeca',
            'corona mark ii', 'corona', 'corolla 1200', 'corona hardtop',
            'corolla 1600 (sw)', 'carina', 'mark ii', 'corolla', 'corolla liftback',
            'celica gt liftback', 'starlet', 'tercel', 'cressida', 'corolla tercel', 'camry',
            'corolla 1.6', 'gti', 'rabbit', 'scirocco', 'dasher', 'rabbit custom',
            'passat', 'dasher (diesel)', 'rabbit custom diesel', 'rabbit l', 'golf',
            'jetta', 'scirocco 16v', 'vanagon', 'model 111', 'type 3', '1600', '411 (sw)',
            'super beetle', 'dasher (diesel)', 's-12', 'audi 5000', 'audi 4000',
            'audi 5000s (diesel)', '320i', 'x1', 'x3', 'z4', 'x4', 'x5', 'x6', 'x7',
            '240 dl', '145e (sw)', '144ea', '244dl', '245', '264gl', 'diesel', '246'
        ])
    }

    return marque_dict, modele_dict


# Créez des champs pour recueillir les données d'entrée
longueur_voiture = st.number_input("Longueur voiture", value=150)
hauteur_voiture = st.number_input("Hauteur voiture", value=60)
largeur_voiture = st.number_input("Largeur voiture", value=50)
# ... Ajoutez d'autres champs pour les caractéristiques numériques

marque_dict, modele_dict = create_dictionaries()

marques = list(marque_dict.values())
marque = st.selectbox("Marque", options=marques)

modeles = list(modele_dict.values())
modele = st.selectbox("Modèle", options=modeles)

type_carrosseries = ['carrosserie1', 'carrosserie2', 'carrosserie3']  # Remplacez par les vrais types de carrosserie
type_carrosserie = st.selectbox("Type carrosserie", options=type_carrosseries)

# ... Ajoutez d'autres champs pour les caractéristiques catégorielles

# Mettez les caractéristiques d'entrée dans un DataFrame
input_data = pd.DataFrame({
    "longueur_voiture": [longueur_voiture],
    "hauteur_voiture": [hauteur_voiture],
    "largeur_voiture": [largeur_voiture],
    "marque": [marque],
    "modele": [modele],
    "type_carrosserie": [type_carrosserie],
    # ... Ajoutez d'autres caractéristiques ici
})

# Lorsque l'utilisateur clique sur le bouton, effectuez une prédiction
if st.button("Prédire le prix"):
    prediction = model.predict(input_data)
    st.write(f"Le prix prédit est : {prediction[0]:.2f}")