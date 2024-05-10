CREATE OR REPLACE FUNCTION no_modif_regions()
RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'La table REGIONS est non modifiable';
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prevent_modif_regions
BEFORE INSERT OR UPDATE OR DELETE ON regions
FOR EACH STATEMENT
EXECUTE FUNCTION no_modif_regions();


CREATE OR REPLACE FUNCTION no_modif_departements()
RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'La table DEPARTEMENTS est non modifiable';
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prevent_modif_departements
BEFORE INSERT OR UPDATE OR DELETE ON departements
FOR EACH STATEMENT
EXECUTE FUNCTION no_modif_departements();


CREATE OR REPLACE FUNCTION update_population_dep_reg()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
        UPDATE population_dep_annee
        SET population = (SELECT SUM(p.valeur_stat)
                          FROM populations p
                          WHERE p.code_com = NEW.code_com
                            AND p.annee_debut = NEW.annee_debut)
        WHERE code_dep = NEW.code_dep
          AND annee = NEW.annee_debut;

        UPDATE population_reg_annee
        SET population = (SELECT SUM(p.valeur_stat)
                          FROM populations p
                          JOIN departements d ON p.code_com = NEW.code_com
                          WHERE d.code_reg = NEW.code_reg
                            AND p.annee_debut = NEW.annee_debut)
        WHERE code_reg = NEW.code_reg
          AND annee = NEW.annee_debut;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE population_dep_annee
        SET population = (SELECT SUM(p.valeur_stat)
                          FROM populations p
                          WHERE p.code_com = OLD.code_com
                            AND p.annee_debut = OLD.annee_debut)
        WHERE code_dep = OLD.code_dep
          AND annee = OLD.annee_debut;

        UPDATE population_reg_annee
        SET population = (SELECT SUM(p.valeur_stat)
                          FROM populations p
                          JOIN departements d ON p.code_com = OLD.code_com
                          WHERE d.code_reg = OLD.code_reg
                            AND p.annee_debut = OLD.annee_debut)
        WHERE code_reg = OLD.code_reg
          AND annee = OLD.annee_debut;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_population_trigger
AFTER INSERT OR UPDATE OR DELETE ON populations
FOR EACH ROW
EXECUTE FUNCTION update_population_dep_reg();