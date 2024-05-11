import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Plan d'exécution et indexAnalyse de l'effet de l'index"),
        html.Br(),
        html.Br(),
        html.H4("Table avec la liste les communes avec moins de 5000 habitants"),
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
        html.P("Nous allons ajouter un index nommé 'idx_population' sur la table 'populations' de la base de données."),
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
        html.Br(),
        html.P("Nous constatons que l'EXPLAIN produit le même résultat même lorsque nous utilisons un index sur la table 'population', soit un coût total de 1023.36. Cette similarité est attribuable à la concision de la requête. Afin d'approfondir notre analyse, nous prévoyons mettre ce mécanisme à l'épreuve en utilisant une requête plus élaborée, intégrant un nombre plus important de jointures."),
        html.Br(),
        html.Br(),
        html.H4("Table des communes qui ont une population supérieure à 10000 habitants en 2020"),
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
        html.P("Création un index sur la colonne 'code_com' de la table 'communes'."),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("CREATE INDEX idx_code_com ON communes (code_com); \n\nEXPLAIN SELECT nom \nFROM communes \nWHERE code_com \nIN \n(SELECT code_com FROM populations \nWHERE annee_debut = 2020 AND type_stat = 'population' AND valeur_stat > 100000);", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_6.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
        html.P("Les index offrent une voie d'accès rapide aux données stockées dans une table. Dans ce contexte, l'index sur la colonne 'code_com' de la table 'communes' permet à la base de données d'atteindre rapidement les enregistrements correspondants. Au lieu de parcourir linéairement chaque ligne de la table 'communes' pour trouver les correspondances avec les valeurs de 'code_com', la base de données peut recourir à cet index pour localiser directement les enregistrements associés, réduisant considérablement le temps d'accès aux données."),
        html.P("L'optimisation des jointures constitue un autre avantage significatif des index. En utilisant un index sur la colonne 'code_com', la base de données peut rationaliser le processus de jointure entre les tables 'communes' et 'populations'. Plutôt que de passer en revue toutes les lignes de la table 'communes' pour vérifier leur correspondance avec les résultats de la sous-requête, la base de données exploite l'index pour effectuer une recherche ciblée et rapide des lignes pertinentes, améliorant ainsi les performances de la jointure."),
        html.P("En outre, l'utilisation d'index contribue à réduire le coût global de traitement de la requête en passant d'un coût total d'exécution 17751.93 à 8052.31. L'index scan sur la table 'communes' se révèle être une opération moins onéreuse en termes de ressources par rapport à un scan séquentiel complet. Cette optimisation se traduit par des temps d'exécution réduits et une utilisation plus efficace des ressources du système, ce qui favorise des performances globales améliorées."),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H4("Table avec la région la moins peuplée"),
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("EXPLAIN SELECT r.nom AS region, SUM(p.valeur_stat) AS population_totale \nFROM communes c \nJOIN departements d ON c.code_dep = d.code_dep \nJOIN regions r ON d.code_reg = r.code_reg \nJOIN populations p ON c.code_com = p.code_com \nWHERE p.type_stat = 'population' GROUP BY r.nom ORDER BY population_totale ASC LIMIT 1;", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_1.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
        html.P("Création un index sur la colonne 'valeur_stat' de la table 'populations'."),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre("CREATE INDEX idx_population_2 ON populations (valeur_stat); \n\nEXPLAIN SELECT r.nom AS region, SUM(p.valeur_stat) AS population_totale \nFROM communes c \nJOIN departements d ON c.code_dep = d.code_dep \nJOIN regions r ON d.code_reg = r.code_reg \nJOIN populations p ON c.code_com = p.code_com \nWHERE p.type_stat = 'population' GROUP BY r.nom ORDER BY population_totale ASC LIMIT 1;", className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Img(src="static/img/plan_exec_index_5.jpg",
                 style={'width': '40%', 'margin-top': '20px', 'margin-bottom': '20px'}),
        html.Br(),
        html.P("L'intérêt de l'index dans ces requêtes est de faciliter l'accès aux données, en particulier lors des opérations de jointure et d'agrégation."),
        html.P("Nous constatons que avec une requête est plus complexe avec plusieurs jointures et une agrégation plus importante des données, l'index sur valeur_stat dans la table populations n'est pas utilisé (la premiere requete tout en haut de la page). Le coût d'exécution de la requête est significativement plus élevé (coût total de 17569.12). Cela est dû à la nécessité pour la base de données de parcourir de grandes quantités de données pour effectuer les jointures et l'agrégation."),
        html.P("En utilisant l'index idx_population_2 soit présent, le coût d'exécution de la requête est relativement plus faible (coût total de 1238.31). L'utilisation de l'index dans ce cas peut aider à accélérer l'accès aux valeurs_statistiques dans la table populations lors de la jointure avec la table communes."),
        html.H4("Conclusion"),
        html.P("L'utilisation judicieuse des index peut jouer un rôle crucial dans l'optimisation des performances des requêtes SQL et dans l'amélioration de l'expérience utilisateur dans les applications basées sur des bases de données. Cependant, il est important de garder à l'esprit que la création excessive d'index peut également avoir un impact sur les performances, donc il est essentiel de les choisir avec soin en fonction des besoins spécifiques de votre application."),
        html.Br(),    
    ])