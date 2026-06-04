import csv
from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = "dsa_tracker.db"


@app.route("/")
def home():
    return "Welcome to DSA Practice Tracker"


@app.route("/testdb")
def testdb():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    conn.close()

    return jsonify({
        "tables": str(tables)
    })


@app.route("/columns")
def columns():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(problems)")
    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


@app.route("/upgrade")
def upgrade():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("ALTER TABLE problems ADD COLUMN problem_link TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE problems ADD COLUMN status TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE problems ADD COLUMN notes TEXT")
    except:
        pass

    try:
        cursor.execute("ALTER TABLE problems ADD COLUMN date_solved TEXT")
    except:
        pass

    conn.commit()
    conn.close()

    return "Database Upgraded Successfully"


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    conn = sqlite3.connect(DB_PATH)
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


@app.route("/users")
def get_users():

    conn = sqlite3.connect(DB_PATH)
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


@app.route("/add-problem", methods=["POST"])
def add_problem():

    data = request.get_json()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO problems
        (
            title,
            topic,
            difficulty,
            platform,
            problem_link,
            status,
            notes,
            date_solved
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data.get("title"),
            data.get("topic"),
            data.get("difficulty"),
            data.get("platform"),
            data.get("problem_link", ""),
            data.get("status", "Solved"),
            data.get("notes", ""),
            data.get("date_solved", "")
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Problem Added Successfully"
    })


@app.route("/problems")
def get_problems():

    conn = sqlite3.connect(DB_PATH)
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
            "platform": row[4],
            "problem_link": row[5] if len(row) > 5 else "",
            "status": row[6] if len(row) > 6 else "",
            "notes": row[7] if len(row) > 7 else "",
            "date_solved": row[8] if len(row) > 8 else ""
        })

    conn.close()

    return jsonify(problems)


@app.route("/stats")
def stats():

    conn = sqlite3.connect(DB_PATH)
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

@app.route("/add-links")
def add_links():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    links = [
        (1, "https://leetcode.com/problems/two-sum/"),
        (2, "https://leetcode.com/problems/binary-search/"),
        (3, "https://leetcode.com/problems/valid-parentheses/"),
        (4, "https://leetcode.com/problems/merge-sorted-array/"),
        (5, "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"),
        (6, "https://leetcode.com/problems/linked-list-cycle/"),
        (7, "https://leetcode.com/problems/3sum/"),
        (8, "https://leetcode.com/problems/group-anagrams/"),
        (9, "https://leetcode.com/problems/longest-substring-without-repeating-characters/"),
        (10, "https://leetcode.com/problems/container-with-most-water/"),
        (11, "https://leetcode.com/problems/number-of-islands/"),
        (12, "https://leetcode.com/problems/merge-intervals/"),
        (13, "https://leetcode.com/problems/n-queens/"),
        (14, "https://leetcode.com/problems/word-ladder/"),
        (15, "https://leetcode.com/problems/sudoku-solver/"),
        (16, "https://leetcode.com/problems/regular-expression-matching/"),
        (17, "https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph/"),
        (18, "https://www.geeksforgeeks.org/implementing-dijkstra-set-1-adjacency-matrix/"),
        (19, "https://www.geeksforgeeks.org/koko-eating-bananas/"),
        (20, "https://www.codingninjas.com/studio/problems/allocate-books_1090540"),
        (21, "https://www.hackerrank.com/challenges/maxsubarray/problem"),
        (22, "https://www.hackerrank.com/challenges/icecream-parlor/problem"),
        (23, "https://www.codechef.com/problems/PRIME1"),
        (24, "https://www.codechef.com/problems/TSORT")
    ]

    for problem_id, link in links:
        cursor.execute(
            "UPDATE problems SET problem_link=? WHERE id=?",
            (link, problem_id)
        )

    conn.commit()
    conn.close()

    return "Links Added Successfully"


@app.route("/solve/<int:problem_id>", methods=["PUT"])
def solve_problem(problem_id):

    from datetime import date

    today = str(date.today())

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE problems
        SET status=?,
            date_solved=?
        WHERE id=?
        """,
        (
            "Solved",
            today,
            problem_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Problem Marked Solved"
    })
@app.route("/pending/<int:problem_id>", methods=["PUT"])
def pending_problem(problem_id):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE problems
        SET status='Pending'
        WHERE id=?
        AND (status IS NULL OR status='Unsolved')
        """,
        (problem_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Problem Marked Pending"
    })

@app.route("/streak")
def streak():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT date_solved
        FROM problems
        WHERE status='Solved'
        AND date_solved IS NOT NULL
    """)

    dates = cursor.fetchall()

    conn.close()

    return jsonify({
        "streak": len(dates)
    })
@app.route("/progress")
def progress():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM problems WHERE status='Solved'"
    )
    solved = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM problems"
    )
    total = cursor.fetchone()[0]

    conn.close()

    percent = round((solved / total) * 100, 2) if total > 0 else 0

    return jsonify({
        "solved": solved,
        "total": total,
        "percent": percent
    })
@app.route("/topics")
def topics():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT topic, COUNT(*)
        FROM problems
        GROUP BY topic
    """)

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)
@app.route("/export")
def export():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()

    conn.close()

    with open("report.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Title",
            "Topic",
            "Difficulty",
            "Platform",
            "Problem Link",
            "Status",
            "Notes",
            "Date Solved"
        ])

        writer.writerows(rows)

    return jsonify({
        "message": "Report Exported Successfully"
    })
if __name__ == "__main__":
    app.run(debug=True)