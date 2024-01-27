from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('jobs.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/jobs', methods=['GET'])
def get_jobs():
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs').fetchall()
    return jsonify([dict(job) for job in jobs])


if __name__ == '__main__':
    app.run(debug=True)
