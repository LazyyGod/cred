import sqlite3
from sqlite3 import Error

#СКьюЛь часть
PATH = "main.db"

CREATE_DATABASE_QUERY = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  surname TEXT NOT NULL,
  class TEXT NOT NULL,
  login TEXT NOT NULL,
  password TEXT NOT NULL,
  balance INTEGER NOT NULL
);
"""

DROP_DATABASE_QUERY = """
DROP TABLE users;
"""

def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn

def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully -", query.replace("\n", " "))
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(conn, query):
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

conn = create_connection(PATH)
while True:
    com = input(">>> ")
    res = execute_read_query(conn, com)
    if res != None:
        print(res)
