
DROP VIEW IF EXISTS StudentDetails;
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Department;

CREATE TABLE Department (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName VARCHAR(50) NOT NULL
);

CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    StudentName VARCHAR(50) NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID)
        REFERENCES Department(DepartmentID)
);

CREATE TABLE Course (
    CourseID INTEGER PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL
);

CREATE TABLE Enrollment (
    EnrollmentID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (StudentID)
        REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID)
        REFERENCES Course(CourseID)
);

INSERT INTO Department VALUES
(101, 'Computer Science'),
(102, 'Information Technology'),
(103, 'Commerce');

INSERT INTO Student VALUES
(1, 'Arun', 101),
(2, 'Divya', 103),
(3, 'Kavin', 101),
(4, 'Priya', 102);

INSERT INTO Course VALUES
(201, 'Database Management Systems'),
(202, 'Python Programming'),
(203, 'Computer Networks'),
(204, 'Web Development');

INSERT INTO Enrollment VALUES
(1, 1, 201),
(2, 1, 202),
(3, 2, 203),
(4, 3, 201),
(5, 4, 204);

CREATE VIEW StudentDetails AS
SELECT
    Student.StudentName,
    Course.CourseName,
    Department.DepartmentName
FROM Student
INNER JOIN Enrollment
    ON Student.StudentID = Enrollment.StudentID
INNER JOIN Course
    ON Enrollment.CourseID = Course.CourseID
INNER JOIN Department
    ON Student.DepartmentID = Department.
