-- prints the full description of the table 
-- not allowed to use the DESCRIBE or EXPLAIN statements

SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
