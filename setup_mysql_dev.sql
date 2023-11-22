---Script that prepares the database server for my airbnb project
--This query creates the db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--This query creates the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--This query grants all privileges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
--This query grants select privileges to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
--This query flushes the qrants
FLUSH PRIVILEGES;