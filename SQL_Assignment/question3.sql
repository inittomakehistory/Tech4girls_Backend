-- question3.sql

-- Use the Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create a Courses table
CREATE TABLE IF NOT EXISTS Courses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  course_name VARCHAR(100) NOT NULL
);

SHOW DATABASES;

-- Create an intermediate table User_Courses
CREATE TABLE IF NOT EXISTS User_Courses (
  user_id INT NOT NULL, 
  course_id INT NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES Users(id),
  FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- Insert sample data into the Courses table
INSERT INTO Courses (course_name)
VALUES
  ('Introduction to Python'),
  ('Object Oriented'),
  ('Programming'),
  ('Software Engineer');

-- Insert sample data into the User_Courses table
INSERT INTO User_Courses (user_id, course_id)
VALUES
  (1, 2),
  (2, 1),
  (2, 3),
  
  SELECT * FROM User_Courses;
