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
empattement = st.number_input("Empattement", min_value=0, value=100, step=1)
taille_moteur = st.number_input("Taille du moteur", min_value=0, value=1000, step=10)
poids_vide = st.number_input("Poids à vide", min_value=0, value=2000, step=10)
consommation_ville = st.number_input("Consommation en ville", min_value=0, value=20, step=1)
consommation_autoroute = st.number_input("Consommation sur autoroute", min_value=0, value=20, step=1)
puissance = st.number_input("Puissance", min_value=0, value=100, step=1)
trmin_max = st.number_input("Tours/minute max", min_value=0, value=5000, step=100)
nombre_cylindres = st.number_input("Nombre de cylindres", min_value=1, value=4, step=1)
alesage = st.number_input("Alésage", min_value=0.0, value=3.0, step=0.1)
course = st.number_input("Course", min_value=0.0, value=3.0, step=0.1)
taux_compression = st.number_input("Taux de compression", min_value=0.0, value=10.0, step=0.1)
nombre_portes = st.number_input('Nombre de portes', min_value=1, max_value=5, value=4, step=1)
type_carburant = st.selectbox('Type de carburant', ['essence', 'diesel', 'électrique', 'hybride'])
emplacement_moteur = st.selectbox('Emplacement du moteur', ['avant', 'arrière'])
systeme_carburant = st.selectbox('Système de carburant', ['Injection de carburant multipoint', '2 barils simple corps', 'Injection de carburant mécanique', '1 baril simple corps', 'Injection de carburant monopoint simplifiée', '4 barils simple corps', 'Injection directe indirecte', 'Injection de carburant monopoint'])
aspiration = st.selectbox('Aspiration', ['standard', 'turbocharged'])
roues_motrices = st.selectbox('Roues motrices', ['traction arrière', 'traction avant', 'quatre roues motrices'])
type_moteur = st.selectbox('Type de moteur', ['Double arbre à cames en tête', 'Arbre à cames en tête avec soupapes en V', 'Arbre à cames en tête', 'En ligne', 'Moteur rotatif', 'Arbre à cames en tête avec soupapes en F', 'Double arbre à cames en tête avec soupapes en V'])
# ... Ajoutez d'autres champs pour les caractéristiques numériques

marque_dict, modele_dict = create_dictionaries()

marques = list(marque_dict.values())
marque = st.selectbox("Marque", options=marques)

modeles = list(modele_dict.values())
modele = st.selectbox("Modèle", options=modeles)

type_carrosseries = ['décapotable', 'à hayon', 'berline', 'break', 'coupé']# Remplacez par les vrais types de carrosserie
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
    'empattement': [empattement],
    'taille_moteur': [taille_moteur],
    'poids_vide': [poids_vide],
    'consommation_ville': [consommation_ville],
    'consommation_autoroute': [consommation_autoroute],
    'puissance': [puissance],
    'trmin_max': [trmin_max],
    'nombre_cylindres': [nombre_cylindres],
    'alesage': [alesage],
    'course': [course],
    'taux_compression': [taux_compression],
    'nombre_portes': [nombre_portes],
    'type_carburant': [type_carburant],
    'emplacement_moteur': [emplacement_moteur],
    'systeme_carburant': [systeme_carburant],
    'aspiration': [aspiration],
    'roues_motrices': [roues_motrices],
    'type_moteur': [type_moteur],
})

# Lorsque l'utilisateur clique sur le bouton, effectuez une prédiction
if st.button("Prédire le prix"):
    prediction = model.predict(input_data)
    st.write(f"Le prix prédit est : {prediction[0]:.2f}")