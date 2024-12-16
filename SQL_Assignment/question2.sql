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
VALUES
--('ama','ama@example.com','2024-11-01 10:30:00'),
--('Abena','abena@example.com','2024-11-02 12:00:00'),
--('adjoa','adjoa@example.com','2024-11-03 14:15:00');

--SELECT * FROM Users



-- question2.sql

-- Use the Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create a Posts table
CREATE TABLE IF NOT EXISTS Posts (
 id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT,
 title VARCHAR(255) NOT NULL,
  content TEXT,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES Users(id)
  );
 
SHOW TABLES;

-- Insert sample data to establish a one-to-many relationship between Users and Posts
INSERT INTO Posts (user_id, title, content)
VALUES
  (1, 'My First Post', 'This is my first post on this platform.'),
  (1, 'My Second Post', 'This is my second post on this platform.'),
  (2, 'Hello World', 'This is my first post on this platform.'),
  (3, 'Tech4Girls', 'This is a post about Tech4Girls.');

-- Retrieve data from both tables to verify the relationship
SELECT Users.username, Posts.title, Posts.content
FROM Users
JOIN Posts
 ON id user_id = Posts.user_id 


