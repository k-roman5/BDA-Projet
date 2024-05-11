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
    code_reg VARCHAR(10) CONSTRAINT pk_cle_reg_cheflieureg REFERENCES regions(code_reg) PRIMARY KEY,
    code_com VARCHAR(10) CONSTRAINT cle_com_cheflieureg REFERENCES communes(code_com)
);

CREATE TABLE cheflieudep (
    code_dep VARCHAR(10) CONSTRAINT pk_cle_dep_cheflieudep REFERENCES departements(code_dep) PRIMARY KEY,
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


-- Tables pour les données de mariage

CREATE TABLE groupeageepoux (
    typmar3 VARCHAR(10),
    dep_mar VARCHAR(10) CONSTRAINT cle_dep_mar_groupeageepoux REFERENCES departements(code_dep),
    groupeage VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_groupeageepoux CHECK (nbmaries >= 0),
    CONSTRAINT pk_groupeageepoux PRIMARY KEY (typmar3, dep_mar, groupeage)
);

CREATE TABLE etatmatrimonialanterieur (
    typmar VARCHAR(10),
    dep_mar VARCHAR(10) CONSTRAINT cle_dep_mar_etatmatrimonialanterieur REFERENCES departements(code_dep),
    sexe VARCHAR(1),
    etat VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_etatmatrimonialanterieur CHECK (nbmaries >= 0),
    CONSTRAINT pk_etatmatrimonialanterieur PRIMARY KEY (typmar, dep_mar, sexe, etat)
);

CREATE TABLE groupeagepremiermariage (
    typmar3 VARCHAR(10),
    dep_mar VARCHAR(10) CONSTRAINT cle_dep_mar_groupeagepremiermariage REFERENCES departements(code_dep),
    groupeage VARCHAR(10),
    nbmaries INT CONSTRAINT non_neg_nbmaries_groupeagepremiermariage CHECK (nbmaries >= 0),
    CONSTRAINT pk_groupeagepremiermariage PRIMARY KEY (typmar3, dep_mar, groupeage)
);

CREATE TABLE nationaliteepoux (
    typmar2 VARCHAR(10),
    dep_domi VARCHAR(10) CONSTRAINT cle_dep_dom_nationaliteepoux REFERENCES departements(code_dep),
    nationalite VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_nationaliteepoux CHECK (nbmar >= 0),
    CONSTRAINT pk_nationaliteepoux PRIMARY KEY (typmar2, dep_domi, nationalite)
);

CREATE TABLE paysnaissanceepoux (
    typmar2 VARCHAR(10),
    dep_domi VARCHAR(10) CONSTRAINT cle_dep_dom_paysnaissanceepoux REFERENCES departements(code_dep),
    pays_naissance VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_paysnaissanceepoux CHECK (nbmar >= 0),
    CONSTRAINT pk_paysnaissanceepoux PRIMARY KEY (typmar2, dep_domi, pays_naissance)
);

CREATE TABLE repartitionmensuellemariages (
    typmar VARCHAR(10),
    dep_mar VARCHAR(10) CONSTRAINT cle_dep_repartitionmensuellemariages REFERENCES departements(code_dep),
    mois VARCHAR(10),
    nbmar INT CONSTRAINT non_neg_nbmar_repartitionmensuellemariages CHECK (nbmar >= 0),
    CONSTRAINT pk_repartitionmensuellemariages PRIMARY KEY (typmar, dep_mar, mois)
);

--