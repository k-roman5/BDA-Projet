CREATE OR REPLACE PROCEDURE population_dep_reg_annee()
LANGUAGE SQL
AS $$
    DECLARE max_year INT;
    DECLARE current_year INT DEFAULT EXTRACT(YEAR FROM CURRENT_DATE);
    BEGIN
        SELECT MAX(annee_debut) INTO max_year FROM populations;
        
        WHILE current_year <= max_year LOOP
            INSERT INTO population_dep_annee (code_dep, annee, population)
            SELECT d.code_dep, current_year, SUM(p.valeur_stat)
            FROM departements d
            JOIN communes c ON d.code_dep = c.code_dep
            JOIN populations p ON c.code_com = p.code_com
            WHERE p.type_stat = 'population' AND p.annee_debut = current_year
            GROUP BY d.code_dep;

            INSERT INTO population_reg_annee (code_reg, annee, population)
            SELECT r.code_reg, current_year, SUM(p.valeur_stat)
            FROM regions r
            JOIN departements d ON r.code_reg = d.code_reg
            JOIN communes c ON d.code_dep = c.code_dep
            JOIN populations p ON c.code_com = p.code_com
            WHERE p.type_stat = 'population' AND p.annee_debut = current_year
            GROUP BY r.code_reg;
            
            current_year := current_year + 1;
        END LOOP;
    END;
$$;


CREATE OR REPLACE FUNCTION update_population_trigger()
RETURNS TRIGGER AS $$
BEGIN
    CALL population_dep_reg_annee();
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_population_trigger
AFTER INSERT OR UPDATE OR DELETE ON populations
FOR EACH STATEMENT
EXECUTE FUNCTION update_population_trigger();