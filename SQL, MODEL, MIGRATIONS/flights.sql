CREATE TABLE flights (
    id INTERGER PRIMARY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTERGER NOT NULL
);

-- ####################################################################
-- # Basic INSERT statement
-- # See https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-insert for complete syntax.
-- ####################################################################
INSERT INTO table-name (column-name)
    VALUES (expression)