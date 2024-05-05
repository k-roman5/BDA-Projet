# MINI PROJET DE Bases de données avancées - MASTER 1

## Sujet : conception bases de données, implémentation BD, interrogation depuis un programme

Bienvenue sur notre mini projet de Bases de données avancées de Master 1. 

Le projet comprend la conception et l'implémentation d'une base de données relationnelle à partir de données de l'INSEE, ainsi que l'interrogation de cette base depuis un programme. Des tâches supplémentaires incluent la création de vues, de procédures stockées et de triggers, ainsi que l'analyse du plan d'exécution des requêtes et l'utilisation des index pour optimiser les performances.

___

## Base de données :

Pour la gestion de la base de données, nous utilisons [PostgreSQL](https://www.postgresql.org) comme système de gestion de base de données relationnelle. Pour interagir avec la base de données, nous utilisons [PgAdmin 4](https://www.pgadmin.org), une interface web open source qui offre un ensemble complet d'outils pour la gestion et le développement de bases de données PostgreSQL.

___

## Python : 

[__Python (13.12.3)__](https://www.python.org) est un langage de programmation polyvalent réputé pour sa lisibilité et sa facilité d'utilisation. Avec sa vaste bibliothèque standard et sa prise en charge de plusieurs paradigmes de programmation, il offre une grande flexibilité aux développeurs.

___

## Extensions : 

- __Pandas (2.2.2)__ est une bibliothèque de manipulation et d'analyse de données pour Python. Elle simplifie le traitement des données structurées en offrant des structures de données telles que les séries (Series) et les cadres de données (DataFrame). Pandas est largement employé pour le nettoyage, l'exploration et l'analyse des données.

- __Dash (2.17.0)__ est un framework Python puissant pour le développement d'applications web. Il est parfait pour la création de tableaux de bord interactifs et orientés données. Avec Dash, vous pouvez construire des applications web en utilisant uniquement Python, ce qui élimine le besoin de connaissances en HTML, CSS ou JavaScript.

- __Dash_bootstrap_components (1.6.0)__ est une bibliothèque de création qui permet de concevoir des graphiques interactifs et facilement partageables. Elle peut être utilisée en ligne et hors ligne, et prend en charge une vaste gamme de types de graphiques. (Dash crée des visualisations interactives pour ses applications web avec Plotly.)

- __Psycopg2-binary (2.9.9)__ est un adaptateur de base de données PostgreSQL pour Python. Il permet aux applications Python de se connecter à une base de données PostgreSQL, d'exécuter des requêtes SQL et d'interagir avec la base de données de manière transparente. Il s'agit d'une version binaire pré-compilée de la bibliothèque `psycopg2`, ce qui signifie qu'elle est prête à l'emploi sans nécessiter de compilation supplémentaire. Cela facilite l'installation et l'utilisation de cette bibliothèque, en particulier dans des environnements où la compilation de code source n'est pas possible ou souhaitable. `psycopg2-binary` est largement utilisé dans le monde Python pour interagir avec des bases de données PostgreSQL.

___

## Version de chaque extension utilisée pour le projet : 
```bash
Python Version: 3.12.3
Pandas Version: 2.2.2
Dash Version: 2.17.0
Dash_bootstrap_components Version : 1.6.0
Psycopg2-binary Version : 2.9.9
```
___

## Installation : 

Pour obtenir la liste complète des extensions utilisées dans ce projet, veuillez exécuter la commande suivante (notez que les versions peuvent différer de celles utilisées pour développer ce projet) :

```bash 
pip install -r requirements.txt
```
___

## Données : 

Les données utilisées pour le projet proviennent du site de l'INSEE et comprennent des informations sur [les régions, les départements et les communes françaises](https://www.insee.fr/fr/information/6800675). Ainis nous diposons des données concernant [le recensement de la population par commune](https://www.insee.fr/fr/statistiques/7632565) et les données sur [le nombre de mariages par departement](https://www.insee.fr/fr/statistiques/6790710).

___

## Lancement de l'app : 

Une fois que toutes les extensions sont installées, vous pouvez démarrer l'application directement en utilisant le code suivant :

```bash 
python app.py
```
___

## Contributeurs  : 

| [<img src="https://avatars.githubusercontent.com/u/102798850?v=4" width="50" height="50" alt=""/>](https://github.com/LouisDelignac) | [<img src="https://avatars.githubusercontent.com/u/102798439?v=4" width="50" height="50" alt=""/>](https://github.com/k-roman5) |       |
| :----------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------: | :---: |
|                                          [Louis Delignac](https://github.com/LouisDelignac)                                          |                                           [Karina Roman](https://github.com/k-roman5)                                           |