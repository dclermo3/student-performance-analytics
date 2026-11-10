import pandas as pd
import sqlite3

# Load student dataset
students = pd.read_csv("data/student-mat.csv", sep=";")

# Connect to SQLite database
connection = sqlite3.connect("database/students.db")

# Store student records in a SQL table
students.to_sql(
    "students",
    connection,
    if_exists="replace",
    index=False
)

print("Student database created successfully!")

# Check how many students were imported
query = "SELECT COUNT(*) FROM students"

result = pd.read_sql_query(query, connection)

print("Total Students in Database:")
print(result)

# SQL Query 1: Average final grade

query1 = """
SELECT ROUND(AVG(G3), 2) AS average_grade
FROM students
"""

print("\nAverage Final Grade:")
print(pd.read_sql_query(query1, connection))


# SQL Query 2: Students who passed and failed

query2 = """
SELECT
    CASE
        WHEN G3 >= 10 THEN 'Passed'
        ELSE 'Failed'
    END AS result,
    COUNT(*) AS total_students
FROM students
GROUP BY result
"""

print("\nStudent Pass/Fail Results:")
print(pd.read_sql_query(query2, connection))


# SQL Query 3: Average grades by study time

query3 = """
SELECT
    studytime,
    COUNT(*) AS total_students,
    ROUND(AVG(G3), 2) AS average_grade
FROM students
GROUP BY studytime
ORDER BY studytime
"""

print("\nAverage Grades by Study Time:")
print(pd.read_sql_query(query3, connection))
connection.close()
