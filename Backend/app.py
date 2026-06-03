from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home Route
@app.route("/")
def home():
    return "Welcome to DSA Practice Tracker"


# Test Database Connection
@app.route("/testdb")
def testdb():
    conn = sqlite3.connect("Backend/dsa_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    conn.close()

    return jsonify({
        "tables": str(tables)
    })


# Register User
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    conn = sqlite3.connect("Backend/dsa_tracker.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "User Registered Successfully"
    })


# Get All Users
@app.route("/users")
def get_users():

    conn = sqlite3.connect("Backend/dsa_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    users = []

    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    conn.close()

    return jsonify(users)


# Add DSA Problem
@app.route("/add-problem", methods=["POST"])
def add_problem():

    data = request.get_json()

    conn = sqlite3.connect("Backend/dsa_tracker.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO problems
        (title, topic, difficulty, platform)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["title"],
            data["topic"],
            data["difficulty"],
            data["platform"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Problem Added Successfully"
    })


# Get All Problems
@app.route("/problems")
def get_problems():

    conn = sqlite3.connect("Backend/dsa_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()

    problems = []

    for row in rows:
        problems.append({
            "id": row[0],
            "title": row[1],
            "topic": row[2],
            "difficulty": row[3],
            "platform": row[4]
        })

    conn.close()

    return jsonify(problems)


# Dashboard Statistics
@app.route("/stats")
def stats():

    conn = sqlite3.connect("Backend/dsa_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM problems")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM problems WHERE difficulty='Easy'")
    easy = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM problems WHERE difficulty='Medium'")
    medium = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM problems WHERE difficulty='Hard'")
    hard = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total_problems": total,
        "easy": easy,
        "medium": medium,
        "hard": hard
    })


if __name__ == "__main__":
    app.run(debug=True)