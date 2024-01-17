-- create a MySQL server
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev set to hbnb_dev_pwd
-- hbnb_dev has all privileges on the hbnb_dev_db (only this database)
-- hbnb_dev has SELECT privilege on performance_schema (only this database)

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER
        IF NOT EXISTS 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
	ON `hbnb_dev_db`.*
	TO 'hbnb_dev'@'localhost';

GRANT SELECT
	ON `performance_schema`.*
	TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
