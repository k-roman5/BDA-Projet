import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", location="sidebar", external_stylesheets=[
                   dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    "padding": "20px",
    "border": "2px solid #D3D3D3",
    "border-radius": "10px",
    "margin": "20px",
    "background-color": "#F8F9FA",
}


def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H1("Projet Bases de données avancées"),
        html.H3("Sujet : conception bases de données, implémentation BD, interrogation depuis un programme"),
        html.Br(),
        html.P("Louis Delignac & Karina Roman, CMI ISI M1"),
        html.Br(),
        html.Br(),
        html.P("Le projet implique la création d'une base de données à partir des données de l'INSEE. Les étapes clés incluent la modélisation de la base, l'importation des données, l'enrichissement avec la population des communes et les statistiques de mariages, le développement de requêtes spécifiques, la création de vues et de procédures stockées, l'utilisation de triggers pour les modifications et les mises à jour automatiques, l'automatisation des calculs de population pour les nouvelles données, et l'analyse des performances pour optimiser les requêtes."),
        html.Br(),
        html.P("1. Le projet est organisé autour de différentes pages, chaque page correspondant à une question spécifique :"),
        html.P("2. Requêtes : Cette page contient les requêtes développées pour répondre à diverses interrogations telles que la liste des départements d'une région donnée, la liste des communes de plus de X habitants d'un département donné, etc."),
        html.P("3. Vues : Sur cette page sont définies les vues nécessaires pour calculer la population des départements et des régions pour différentes années."),
        html.P("4. Procédure stockée : Cette page présente la procédure stockée écrite pour calculer et mettre à jour la population des départements et des régions à partir des populations des communes."),
        html.P("5. Triggers : Les triggers utilisés pour bloquer les modifications sur les tables des régions et des départements, ainsi que pour mettre à jour automatiquement la population d'un département ou d'une région lorsqu'une commune est modifiée, sont décrits dans cette section."),
        html.P("6. Suite des Triggers : Cette page traite de l'automatisation des calculs de population lorsque de nouvelles données sont ajoutées pour une nouvelle année de recensement, en veillant à ce que les calculs ne se fassent que lorsque toutes les données pertinentes sont disponibles."),
        html.P("7. Plan d'exécution avec EXPLAIN : Sur cette page, les coûts d'exécution de différentes requêtes sont analysés en utilisant la commande EXPLAIN SQL, et les différentes stratégies d'exécution sont expliquées."),
        html.P("8. Plan d'exécution et index : Cette dernière page met en lumière l'efficacité des index en analysant les performances de requêtes après la création d'index sur des attributs pertinents, tout en expliquant l'impact sur les stratégies d'exécution."),
        html.Br(),
    ])