CREATE TABLE regions (
    reg int constraint cle_reg PRIMARY KEY,
    libelle varchar(30)
);

CREATE TABLE departements (
    dep varchar(10) constraint cle_dep PRIMARY KEY,
    reg int constraint cle_reg_departements references regions(reg),
    libelle varchar(30)
);

CREATE TABLE communes (
    com varchar(10) constraint cle_com PRIMARY KEY,
    dep varchar(10) constraint cle_dep_communes references departements(dep),
    libelle varchar(50)
);

CREATE TABLE cheflieureg (
    reg int constraint cle_reg_cheflieureg references regions(reg),
    com varchar(10) constraint cle_com_cheflieureg references communes(com)
);

CREATE TABLE cheflieudep (
    dep varchar(10) constraint cle_dep_cheflieudep references departements(dep),
    com varchar(10) constraint cle_com_cheflieudep references communes(com)
);