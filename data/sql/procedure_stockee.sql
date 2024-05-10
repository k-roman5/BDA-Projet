CREATE TABLE population_dep_annee (
    code_dep VARCHAR(10),
    annee INT NOT NULL,
    population INT NOT NULL,
    CONSTRAINT pk_population_dep_annee PRIMARY KEY (code_dep, annee),
    CONSTRAINT fk_population_dep_annee FOREIGN KEY (code_dep) REFERENCES departements(code_dep)
);

CREATE TABLE population_reg_annee (
    code_reg VARCHAR(10),
    annee INT NOT NULL,
    population INT NOT NULL,
    CONSTRAINT pk_population_reg_annee PRIMARY KEY (code_reg, annee),
    CONSTRAINT fk_population_reg_annee FOREIGN KEY (code_reg) REFERENCES regions(code_reg)
);

CREATE PROCEDURE population_dep_reg_annee()
LANGUAGE SQL
AS $$
    INSERT INTO population_dep_annee (code_dep, annee, population)
    SELECT d.code_dep, p.annee_debut, SUM(p.valeur_stat)
    FROM departements d
    JOIN communes c ON d.code_dep = c.code_dep
    JOIN populations p ON c.code_com = p.code_com
    WHERE p.type_stat = 'population'
    GROUP BY d.code_dep, p.annee_debut;

    INSERT INTO population_reg_annee (code_reg, annee, population)
    SELECT r.code_reg, p.annee_debut, SUM(p.valeur_stat)
    FROM regions r
    JOIN departements d ON r.code_reg = d.code_reg
    JOIN communes c ON d.code_dep = c.code_dep
    JOIN populations p ON c.code_com = p.code_com
    WHERE p.type_stat = 'population'
    GROUP BY r.code_reg, p.annee_debut;
$$;

CALL population_dep_reg_annee()