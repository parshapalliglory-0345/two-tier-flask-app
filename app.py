from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector

app = Flask(__name__)

# MySQL config from environment
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
MYSQL_DB = os.getenv("MYSQL_DB", "devops")

def get_db_connection():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages")
    messages = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return render_template("index.html", messages=messages)

@app.route("/add", methods=["POST"])
def add_message():
    message = request.form.get("message")
    if message:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for("index"))

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)