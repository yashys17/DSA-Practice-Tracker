import sqlite3

conn = sqlite3.connect("Backend/dsa_tracker.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        topic TEXT,
        difficulty TEXT,
        platform TEXT,
        problem_link TEXT,
        status TEXT,
        notes TEXT,
        date_solved TEXT
    )
    """
)

conn.commit()
conn.close()

print("Database Created Successfully")