-- creating a database
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
SHOW DATABASES;


USE Tech4Girls_DB;

CREATE TABLE IF NOT EXISTS Users( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

SHOW TABLES;


INSERT INTO Users (username, email, created_at)
VALUES ('ama','ama@example.com','2024-11-01 10:30:00'),
('Abena','abena@example.com','2024-11-02 12:00:00'),
('adjoa','adjoa@example.com','2024-11-03 14:15:00');

SELECT * FROM Users;

