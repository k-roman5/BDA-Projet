import dash
import dash_bootstrap_components as dbc
from dash import html
from view.fonctions import lire_contenu_fichier_sql

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Plan d'exécution (EXPLAIN)"),
        html.Br(),
        html.P("Le plan d'exécution (EXPLAIN) est une fonctionnalité des systèmes de gestion de bases de données (SGBD) qui permet d'analyser la façon dont une requête SQL sera exécutée par le moteur de la base de données. En fournissant des détails sur les étapes prises par le SGBD pour récupérer et manipuler les données, le plan d'exécution aide les développeurs à comprendre et à optimiser les performances de leurs requêtes. Il indique les opérations effectuées, telles que les analyses séquentielles ou les recherches par index, ainsi que les coûts associés à chaque opération, ce qui permet d'identifier les points d'optimisation potentiels."),
        html.Br(),
        html.H4("Table avec la population totale pour chaque département de la région 'Nouvelle-Aquitaine'."),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre(lire_contenu_fichier_sql('data/sql/plan_execution.sql'), className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '500px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.H4("Résultat"),
        html.Img(src="static/img/plan_execution.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
        html.Br(),
        html.H4("Explication"),
        html.Br(),
        html.P("L'analyse du plan d'exécution de cette requête SQL révèle en détail comment la base de données traite la demande. Chaque étape du plan est cruciale pour comprendre le processus global :"),
        html.P("Au départ, une boucle imbriquée est mise en place. Chaque ligne de la table des communes est associée à une ou plusieurs lignes de la table des populations, conformément aux conditions de jointure spécifiées. Ce premier pas produit un ensemble de lignes résultantes."),
        html.P("Ensuite, intervient une opération de jointure de hachage entre les tables des communes et des départements. Elle recherche la correspondance des codes de département entre ces deux tables et utilise une fonction de hachage pour accélérer ce processus."),
        html.P("Dans une troisième étape, une autre boucle imbriquée entre les tables des départements et des régions est initiée. Elle vise à récupérer les régions liées aux départements sélectionnés précédemment. La correspondance des codes de région entre les deux tables est vérifiée à cette étape."),
        html.P("Enfin, une opération d'accès à l'index est effectuée pour rechercher les données dans la table des populations. Cette recherche est basée sur le code de commune et le type de statistique, facilitée par l'index primaire de la table."),
        html.P("Cette approche globale permet d'extraire efficacement les données de population pour toutes les communes de la région 'Nouvelle-Aquitaine'. Les opérations de jointure et d'accès à l'index sont des éléments clés pour filtrer les données de manière précise et obtenir les résultats attendus."),
        html.Br(),
    ])
