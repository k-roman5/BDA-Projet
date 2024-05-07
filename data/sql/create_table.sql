CREATE TABLE regions (
    reg varchar(10) CONSTRAINT cle_reg PRIMARY KEY,
    libelle varchar(30)
);

CREATE TABLE departements (
    dep varchar(10) CONSTRAINT cle_dep PRIMARY KEY,
    reg varchar(10) CONSTRAINT cle_reg_departements REFERENCES regions(reg),
    libelle varchar(30)
);

CREATE TABLE communes (
    com varchar(10) CONSTRAINT cle_com PRIMARY KEY,
    dep varchar(10) CONSTRAINT cle_dep_communes REFERENCES departements(dep),
    libelle varchar(50)
);

CREATE TABLE cheflieureg (
    reg varchar(10) CONSTRAINT cle_reg_cheflieureg REFERENCES regions(reg),
    com varchar(10) CONSTRAINT cle_com_cheflieureg REFERENCES communes(com)
);

CREATE TABLE cheflieudep (
    dep varchar(10) CONSTRAINT cle_dep_cheflieudep REFERENCES departements(dep),
    com varchar(10) CONSTRAINT cle_com_cheflieudep REFERENCES communes(com)
);

CREATE TABLE populations (
    com VARCHAR(10) CONSTRAINT cle_com_populations REFERENCES communes(com), 
    pop2020 INT CONSTRAINT non_neg_pop2020 CHECK (pop2020 >= 0),
    pop2014 INT CONSTRAINT non_neg_pop2014 CHECK (pop2014 >= 0),
    pop2009 INT CONSTRAINT non_neg_pop2009 CHECK (pop2009 >= 0),
    pop1999 INT CONSTRAINT non_neg_pop1999 CHECK (pop1999 >= 0),
    pop1990 INT CONSTRAINT non_neg_pop1990 CHECK (pop1990 >= 0),
    pop1982 INT CONSTRAINT non_neg_pop1982 CHECK (pop1982 >= 0),
    pop1975 INT CONSTRAINT non_neg_pop1975 CHECK (pop1975 >= 0),
    pop1968 INT CONSTRAINT non_neg_pop1968 CHECK (pop1968 >= 0)
);


-- Tables pour les données de mariage

CREATE TABLE GroupeAgeEpoux (
    id INT CONSTRAINT cle_id_groupe_age_epoux PRIMARY KEY,
    typmar3 VARCHAR(10),
    dep VARCHAR(10) CONSTRAINT cle_dep_mariage_age REFERENCES departements(dep),
    groupeage VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries CHECK (nbmaries >= 0)
);

CREATE TABLE EtatMatrimonialAnterieur (
    id INT CONSTRAINT cle_id_etat_matrimonial PRIMARY KEY,
    typmar VARCHAR(10),
    dep VARCHAR(10) CONSTRAINT cle_dep_etat_matrimonial REFERENCES departements(dep),
    sexe VARCHAR(1),
    etat VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_etat_matrimonial CHECK (nbmaries >= 0)
);

CREATE TABLE GroupeAgePremierMariage (
    id INT CONSTRAINT cle_id_groupe_age_premier_mariage PRIMARY KEY,
    typmar3 VARCHAR(10),
    dep VARCHAR(10) CONSTRAINT cle_dep_premier_mariage_age REFERENCES departements(dep),
    groupeage VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_premier_mariage CHECK (nbmaries >= 0)
);

CREATE TABLE NationaliteEpoux (
    id INT CONSTRAINT cle_id_nationalite_pays_naissance PRIMARY KEY,
    typmar2 VARCHAR(10),
    dep_dom VARCHAR(10) CONSTRAINT cle_dep_nationalite_naissance REFERENCES departements(dep),
    nationalite VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_nationalite CHECK (nbmar >= 0)
);

CREATE TABLE PaysNaissanceEpoux (
    id INT CONSTRAINT cle_id_pays_naissance PRIMARY KEY,
    typmar2 VARCHAR(10),
    dep_dom VARCHAR(10) CONSTRAINT cle_dep_pays_naissance REFERENCES departements(dep),
    pays_naissance VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_pays_naissance CHECK (nbmar >= 0)
);

CREATE TABLE RepartitionMensuelleMariages (
    id INT CONSTRAINT cle_id_repartition_mensuelle PRIMARY KEY,
    typmar VARCHAR(10),
    dep VARCHAR(10) CONSTRAINT cle_dep_repartition_mensuelle REFERENCES departements(dep),
    mois VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_repartition_mensuelle CHECK (nbmar >= 0)
);

--