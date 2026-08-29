-- starter.sql
-- Database setup for StudentDetails assignment

DROP VIEW IF EXISTS StudentDetails;

DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Department;

-- Department table
CREATE TABLE Department (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
);

-- Student table
CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

-- Course table
CREATE TABLE Course (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT NOT NULL
);

-- Enrollment table
CREATE TABLE Enrollment (
    EnrollmentID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- Sample Departments
INSERT INTO Department VALUES
(1, 'Computer Science'),
(2, 'Information Technology'),
(3, 'Commerce');

-- Sample Students
INSERT INTO Student VALUES
(101, 'Arun', 1),
(102, 'Priya', 2),
(103, 'Kavin', 1),
(104, 'Divya', 3);

-- Sample Courses
INSERT INTO Course VALUES
(201, 'Database Management Systems'),
(202, 'Python Programming'),
(203, 'Web Development'),
(204, 'Computer Networks');

-- Sample Enrollments
INSERT INTO Enrollment VALUES
(1, 101, 201),
(2, 101, 202),
(3, 102, 203),
(4, 103, 201),
(5, 104, 204);
