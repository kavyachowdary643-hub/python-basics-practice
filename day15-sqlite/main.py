import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    branch TEXT
)
""")
cursor.execute(
    "INSERT INTO students (name, age, branch) VALUES (?, ?, ?)",
    ("Kavya", 20, "IT")
)

conn.commit()
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("Student Records:\n")

for student in students:
    print(student)

conn.close()