## INTRODUCTION TO DATABASES AND SQL

## Project Overview

This project focuses on database concepts and SQL commands. It consists of three questions that test understanding of database design and SQL scripting.
1. Understand database concepts and SQL commands.
2. Learn to design and create databases.
3. Practice SQL scripting and data manipulation.

## PROJECT STRUCTURE 
- question1.sql: Creates a database and a Users table.
- question2.sql: Creates a Posts table and establishes a one-to-many relationship with Users.
- question3.sql: Creates a Courses table and establishes a many-to-many relationship with Users.

## CONCEPTS DEMONSTRATED 
- Creating databases and tables
- Establishing relationships between tables
- Inserting and manipulating data

## EXPLANATION OF COMMANDS USED 

question1.sql
- CREATE DATABASE Tech4Girls_DB;`: Creates a new database named Tech4Girls_DB.
- CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), email VARCHAR(100), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);`: Creates a new table named Users with the specified columns.
- INSERT INTO Users (username, email) VALUES ('ama', 'ama@example.com');`: Inserts a new row into the Users table.

question2.sql
- CREATE TABLE Posts (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, title VARCHAR(255), content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES Users(id));`: Creates a new table named Posts with the specified columns and establishes a foreign key relationship with the Users table.
- INSERT INTO Posts (user_id, title, content) VALUES (1, 'My First Post', 'This is my first post.');`: Inserts a new row into the Posts table.

question3.sql
- `CREATE TABLE Courses (id INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(100));`: Creates a new table named Courses with the specified columns.
- `CREATE TABLE User_Courses (user_id INT, course_id INT, FOREIGN KEY (user_id) REFERENCES Users(id), FOREIGN KEY (course_id) REFERENCES Courses(id));`: Creates a new table named User_Courses with the specified columns and establishes foreign key relationships with the Users and Courses tables.
- `INSERT INTO User_Courses (user_id, course_id) VALUES (1, 1);`: Inserts a new row into the User_Courses table.

## AUTHOR

VICTORIA 
