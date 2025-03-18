import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Vulnerability: SQL Injection
def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # ❌ Unsafe SQL query
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerability: Command Injection
@app.route("/execute", methods=["GET"])
def execute():
    cmd = request.args.get("cmd")
    os.system(cmd)  # ❌ Direct command execution
    return "Executed"

if __name__ == "__main__":
    app.run(debug=True)
