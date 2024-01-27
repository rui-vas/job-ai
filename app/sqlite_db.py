import sqlite3

def connect_db():
    return sqlite3.connect('jobs.db')

def create_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE jobs
        (id INTEGER PRIMARY KEY, title TEXT, status TEXT)
    ''')

def insert_data(conn):
    c = conn.cursor()
    c.execute("INSERT INTO jobs VALUES (1, 'Software Engineer', 'open')")
    c.execute("INSERT INTO jobs VALUES (2, 'Data Scientist', 'closed')")
    c.execute("INSERT INTO jobs VALUES (3, 'Product Manager', 'open')")

def print_data(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM jobs')
    rows = c.fetchall()
    for row in rows:
        print(row)

def check_and_create_db():
    conn = connect_db()
    c = conn.cursor()

    # Check if table exists
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='jobs' ''')

    # If the count is 1, then table exists, delete it
    if c.fetchone()[0] == 1:
        c.execute(''' DROP TABLE jobs ''')

    create_table(conn)
    insert_data(conn)
    print_data(conn)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    check_and_create_db()