-- creating a database named Tech4Girls_DB
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
SHOW DATABASES;

-- Use the Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create a table Users
CREATE TABLE IF NOT EXISTS Users( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

SHOW TABLES;

-- Insert sample data into the Users table
INSERT INTO Users (username, email, created_at)
VALUES ('ama','ama@example.com','2024-11-01 10:30:00'),
('Abena','abena@example.com','2024-11-02 12:00:00'),
('adjoa','adjoa@example.com','2024-11-03 14:15:00');

SELECT * FROM Users
  


