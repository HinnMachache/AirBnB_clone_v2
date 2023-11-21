-- Script that prepares the test database server for my airbnb project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- If the databse doesn't exist create one
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'Cable@123';

-- Use the database
USE hbnb_test_db;

-- Grant all the priviledge on the database to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT priviliges on performance_schema to the test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Create Database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

SET PASSWORD FOR 'hbnb_test'@'localhost' = 'Cable@123';

USE hbnb_test_db;

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
