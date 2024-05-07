CREATE TABLE regions (
    code_reg VARCHAR(10) CONSTRAINT cle_reg PRIMARY KEY,
    nom VARCHAR(30)
);

CREATE TABLE departements (
    code_dep VARCHAR(10) CONSTRAINT cle_dep PRIMARY KEY,
    code_reg VARCHAR(10) CONSTRAINT cle_reg_departements REFERENCES regions(code_reg),
    nom VARCHAR(30)
);

CREATE TABLE communes (
    code_com VARCHAR(10) CONSTRAINT cle_com PRIMARY KEY,
    code_dep VARCHAR(10) CONSTRAINT cle_dep_communes REFERENCES departements(code_dep),
    nom VARCHAR(50)
);

CREATE TABLE cheflieureg (
    code_reg VARCHAR(10) CONSTRAINT cle_reg_cheflieureg REFERENCES regions(code_reg),
    code_com VARCHAR(10) CONSTRAINT cle_com_cheflieureg REFERENCES communes(code_com)
);

CREATE TABLE cheflieudep (
    code_dep VARCHAR(10) CONSTRAINT cle_dep_cheflieudep REFERENCES departements(code_dep),
    code_com VARCHAR(10) CONSTRAINT cle_com_cheflieudep REFERENCES communes(code_com)
);

-- Tables pour les données de population

CREATE TABLE populations (
    code_com VARCHAR(10) NOT NULL,
    annee_debut INT NOT NULL,
    annee_fin INT NOT NULL,
    type_stat VARCHAR(20) NOT NULL,
    valeur_stat FLOAT,
    CONSTRAINT pk_populations PRIMARY KEY (code_com, annee_debut, annee_fin, type_stat),
    CONSTRAINT fk_populations_communes FOREIGN KEY (code_com) REFERENCES communes(code_com)
);

--


-- Tables pour les données de mariage

CREATE TABLE GroupeAgeEpoux (
    id INT CONSTRAINT cle_id_groupe_age_epoux PRIMARY KEY,
    typmar3 VARCHAR(10),
    code_dep VARCHAR(10) CONSTRAINT cle_dep_mariage_age REFERENCES departements(code_dep),
    groupeage VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries CHECK (nbmaries >= 0)
);

CREATE TABLE EtatMatrimonialAnterieur (
    id INT CONSTRAINT cle_id_etat_matrimonial PRIMARY KEY,
    typmar VARCHAR(10),
    code_dep VARCHAR(10) CONSTRAINT cle_dep_etat_matrimonial REFERENCES departements(code_dep),
    sexe VARCHAR(1),
    etat VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_etat_matrimonial CHECK (nbmaries >= 0)
);

CREATE TABLE GroupeAgePremierMariage (
    id INT CONSTRAINT cle_id_groupe_age_premier_mariage PRIMARY KEY,
    typmar3 VARCHAR(10),
    code_dep VARCHAR(10) CONSTRAINT cle_dep_premier_mariage_age REFERENCES departements(code_dep),
    groupeage VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_premier_mariage CHECK (nbmaries >= 0)
);

CREATE TABLE NationaliteEpoux (
    id INT CONSTRAINT cle_id_nationalite_pays_naissance PRIMARY KEY,
    typmar2 VARCHAR(10),
    dep_dom VARCHAR(10) CONSTRAINT cle_dep_nationalite_naissance REFERENCES departements(code_dep),
    nationalite VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_nationalite CHECK (nbmar >= 0)
);

CREATE TABLE PaysNaissanceEpoux (
    id INT CONSTRAINT cle_id_pays_naissance PRIMARY KEY,
    typmar2 VARCHAR(10),
    dep_dom VARCHAR(10) CONSTRAINT cle_dep_pays_naissance REFERENCES departements(code_dep),
    pays_naissance VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_pays_naissance CHECK (nbmar >= 0)
);

CREATE TABLE RepartitionMensuelleMariages (
    id INT CONSTRAINT cle_id_repartition_mensuelle PRIMARY KEY,
    typmar VARCHAR(10),
    code_dep VARCHAR(10) CONSTRAINT cle_dep_repartition_mensuelle REFERENCES departements(code_dep),
    mois VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_repartition_mensuelle CHECK (nbmar >= 0)
);

--