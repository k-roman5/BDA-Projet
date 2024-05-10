EXPLAIN SELECT d.nom AS departement, SUM(p.valeur_stat) AS population_totale 
FROM communes c 
JOIN departements d ON c.code_dep = d.code_dep 
JOIN regions r ON d.code_reg = r.code_reg 
JOIN populations p ON c.code_com = p.code_com 
WHERE r.nom = 'Nouvelle-Aquitaine' AND p.type_stat = 'population' 
GROUP BY d.nom ORDER BY population_totale DESC LIMIT 1;