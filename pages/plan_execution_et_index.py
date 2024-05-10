import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Plan d'exécution et index"),
        html.Br(),
        html.H4("Analyse de l'effet de l'index primaire sur la table avec la région la moins peuplée"),
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("SELECT r.nom AS region, SUM(p.valeur_stat) AS population_totale \nFROM communes c \nJOIN departements d ON c.code_dep = d.code_dep \nJOIN regions r ON d.code_reg = r.code_reg \nJOIN populations p ON c.code_com = p.code_com \nWHERE p.type_stat = 'population' GROUP BY r.nom ORDER BY population_totale ASC LIMIT 1;", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_1.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.P("La présence d'index sur les colonnes utilisées pour les jointures aurait permis d'accélérer ces opérations. Par exemple, un index sur les colonnes 'code_dep' de la table 'communes' et 'code_dep' de la table 'departements' aurait rendu les jointures hash join plus efficaces, réduisant ainsi le temps d'exécution global de la requête."),
        html.P("Ainsi l'ajout d'un index sur la colonne 'type_stat' de la table 'populations' aurait facilité l'accès aux données pertinentes, en particulier lors de l'application du filtre sur cette colonne. Cela aurait réduit le temps nécessaire pour filtrer les données lors du scan séquentiel parallèle de la table 'populations', améliorant ainsi les performances globales de la requête."),
        html.P("L'utilisation d'index sur les colonnes impliquées dans les opérations de tri et d'agrégation aurait également contribué à réduire le coût global de ces opérations. Par exemple, un index sur la colonne 'nom' de la table 'regions' aurait accéléré l'opération de tri final, ce qui aurait permis de réduire le temps nécessaire pour obtenir les résultats triés."),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H4("Analyse de l'effet de l'index primaire sur la table des communes qui ont une population supérieure à 10000 habitants en 2020"),
                html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("EXPLAIN SELECT nom \nFROM communes \nWHERE code_com \nIN \n(SELECT code_com FROM populations \nWHERE annee_debut = 2020 AND type_stat = 'population' AND valeur_stat > 100000);", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_2.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
        html.P("Les index offrent une voie d'accès rapide aux données stockées dans une table. Dans ce contexte, l'index sur la colonne 'code_com' de la table 'communes' permet à la base de données d'atteindre rapidement les enregistrements correspondants. Au lieu de parcourir linéairement chaque ligne de la table 'communes' pour trouver les correspondances avec les valeurs de 'code_com', la base de données peut recourir à cet index pour localiser directement les enregistrements associés, réduisant considérablement le temps d'accès aux données."),
        html.P("L'optimisation des jointures constitue un autre avantage significatif des index. En utilisant un index sur la colonne 'code_com', la base de données peut rationaliser le processus de jointure entre les tables 'communes' et 'populations'. Plutôt que de passer en revue toutes les lignes de la table 'communes' pour vérifier leur correspondance avec les résultats de la sous-requête, la base de données exploite l'index pour effectuer une recherche ciblée et rapide des lignes pertinentes, améliorant ainsi les performances de la jointure."),
        html.P("En outre, l'utilisation d'index contribue à réduire le coût global de traitement de la requête. Dans l'explication du plan de requête fourni, l'index scan sur la table 'communes' se révèle être une opération moins onéreuse en termes de ressources par rapport à un scan séquentiel complet. Cette optimisation se traduit par des temps d'exécution réduits et une utilisation plus efficace des ressources du système, ce qui favorise des performances globales améliorées."),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H4("Analyse de l'effet de l'index sur une requête spécifique avant la création de l'index"),
                html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("EXPLAIN SELECT * FROM populations p \nJOIN communes c ON p.code_com = c.code_com \nWHERE p.valeur_stat < 5000;", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_3.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
                html.Br(),
        html.Br(),
        html.Br(),
        html.H4("Analyse de l'effet de l'index sur une requête spécifique avant la création de l'index après la création d'un index sur l'attribut population"),
                html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("CREATE INDEX idx_population ON populations (valeur_stat); \n\nEXPLAIN SELECT * FROM populations p \nJOIN communes c ON p.code_com = c.code_com \nWHERE p.valeur_stat < 5000;", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_4.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
        html.H4("Conclusion")
    ])