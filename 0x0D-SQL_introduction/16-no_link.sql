-- lists all records of a table except rows without a name value

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
