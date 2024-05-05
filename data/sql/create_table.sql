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