import sqlite3
import sys
import os

DB_FILE = "assignment.db"
STARTER_FILE = "starter.sql"
SOLUTION_FILE = "solution.sql"


def fail(message):
    print("❌ FAIL:", message)
    sys.exit(1)


def success(message):
    print("✅ PASS:", message)


# Check required files
if not os.path.exists(STARTER_FILE):
    fail("starter.sql not found")

if not os.path.exists(SOLUTION_FILE):
    fail("solution.sql not found")


# Create database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Load starter database
with open(STARTER_FILE, "r", encoding="utf-8") as file:
    starter_sql = file.read()

try:
    cursor.executescript(starter_sql)
except Exception as e:
    fail(f"Error in starter.sql: {e}")


# Load student solution
with open(SOLUTION_FILE, "r", encoding="utf-8") as file:
    solution_sql = file.read().strip()

if not solution_sql:
    fail("solution.sql is empty")


try:
    cursor.executescript(solution_sql)
except Exception as e:
    fail(f"Student SQL contains an error: {e}")


# -------------------------------------------------
# TEST 1: View exists
# -------------------------------------------------

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'view'
      AND name = 'StudentDetails'
""")

view = cursor.fetchone()

if view is None:
    fail("StudentDetails view was not created")

success("StudentDetails view exists")


# -------------------------------------------------
# TEST 2: Check columns
# -------------------------------------------------

cursor.execute("PRAGMA table_info(StudentDetails)")
columns = [row[1] for row in cursor.fetchall()]

expected_columns = [
    "StudentName",
    "CourseName",
    "DepartmentName"
]

if columns != expected_columns:
    fail(
        f"Incorrect columns. Expected {expected_columns}, "
        f"but found {columns}"
    )

success("View contains the correct columns")


# -------------------------------------------------
# TEST 3: Check number of rows
# -------------------------------------------------

cursor.execute("SELECT COUNT(*) FROM StudentDetails")
row_count = cursor.fetchone()[0]

expected_count = 5

if row_count != expected_count:
    fail(
        f"Incorrect number of rows. "
        f"Expected {expected_count}, found {row_count}"
    )

success("Correct number of rows returned")


# -------------------------------------------------
# TEST 4: Check expected records
# -------------------------------------------------

cursor.execute("""
    SELECT StudentName, CourseName, DepartmentName
    FROM StudentDetails
    ORDER BY StudentName, CourseName
""")

actual_rows = cursor.fetchall()

expected_rows = [
    ("Arun", "Database Management Systems", "Computer Science"),
    ("Arun", "Python Programming", "Computer Science"),
    ("Divya", "Computer Networks", "Commerce"),
    ("Kavin", "Database Management Systems", "Computer Science"),
    ("Priya", "Web Development", "Information Technology")
]

if actual_rows != expected_rows:
    print("Expected:")
    for row in expected_rows:
        print(row)

    print("\nActual:")
    for row in actual_rows:
        print(row)

    fail("StudentDetails does not return the expected data")

success("Correct Student, Course and Department data")


# -------------------------------------------------
# TEST 5: Check duplicate records
# -------------------------------------------------

cursor.execute("""
    SELECT StudentName, CourseName, DepartmentName, COUNT(*)
    FROM StudentDetails
    GROUP BY StudentName, CourseName, DepartmentName
    HAVING COUNT(*) > 1
""")

duplicates = cursor.fetchall()

if duplicates:
    fail("Duplicate records found in StudentDetails")

success("No duplicate records found")


# -------------------------------------------------
# TEST 6: Check that the view is actually a VIEW
# -------------------------------------------------

cursor.execute("""
    SELECT type
    FROM sqlite_master
    WHERE name = 'StudentDetails'
""")

object_type = cursor.fetchone()

if object_type is None or object_type[0] != "view":
    fail("StudentDetails must be a VIEW, not a table")

success("StudentDetails is a VIEW")


conn.close()

print("\n🎉 ALL TEST CASES PASSED!")
print("StudentDetails assignment completed successfully.")
