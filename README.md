# CarValueScope (CVS): Comprehensive Vehicle Assessment & Revenue Estimation System

Cette application est conçue pour prédire les prix des voitures en fonction de leurs caractéristiques. L'application utilise un modèle de régression pour prédire le prix en fonction de différentes caractéristiques telles que la marque, le modèle, le type de carburant, la taille du moteur, la puissance, etc.

## Installation
#
Clonez le dépôt GitHub :
```bash
git clone https://github.com/your_username/voiture-prix-prediction.git
```
Naviguez vers le répertoire du projet :

```bash
cd voiture-prix-prediction
```

Installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```
## Exécution
#
Pour exécuter l'application, exécutez la commande suivante dans le terminal :

```bash
streamlit run app.py
```
L'application sera accessible à l'adresse http://localhost:8501.

## Modèle
#
Le modèle utilisé pour la prédiction est un RandomForestRegressor entraîné sur un ensemble de données contenant des informations sur les voitures et leurs prix. Les données ont été nettoyées et prétraitées avant d'être utilisées pour l'entraînement. Le modèle a été optimisé en utilisant une recherche sur grille (GridSearchCV) pour trouver les meilleurs hyperparamètres.

Le modèle entraîné est stocké dans le fichier :
```bash 
data/best_model.pkl. 
```

## Application
L'application utilise Streamlit pour créer une interface utilisateur simple permettant de saisir les caractéristiques des voitures et d'afficher la prédiction du prix. L'utilisateur peut saisir les valeurs pour les différentes caractéristiques, et l'application utilisera le modèle entraîné pour prédire le prix de la voiture en fonction de ces caractéristiques.

## Remarque
L'ensemble de données et le modèle utilisés dans cette application sont basés sur des informations antérieures à septembre 2021. Les prédictions peuvent ne pas être exactes pour les modèles de voitures récents ou les prix actuels du marché.
