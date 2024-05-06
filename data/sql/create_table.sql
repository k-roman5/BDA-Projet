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