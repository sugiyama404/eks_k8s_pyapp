from flask import Flask, redirect, url_for
from flask_cors import CORS
import mysql.connector
import json
import re
from collections import OrderedDict
import os
import random


app = Flask(__name__)
CORS(app)

flag = True


def conn_db():
    hostname = os.environ.get('HOST')
    db_name = os.environ.get('DBNAME')
    username = os.environ.get('USERNAME')
    passwd = os.environ.get('PASSWORD')

    conn = mysql.connector.connect(
        host=hostname,
        user=username,
        password=passwd,
        database=db_name
    )
    return conn


def create_table():
    try:
        conn = conn_db()
        cursor = conn.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS todos(id INT PRIMARY KEY AUTO_INCREMENT, content TEXT DEFAULT NULL);'
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    except (mysql.connector.errors.ProgrammingError) as e:
        print(e)


def insert_data():
    name = ['James', 'James', 'Ronald', 'Mary', 'Mary', 'Michelle']
    try:
        conn = conn_db()
        cursor = conn.cursor()
        sql = "INSERT INTO todos (content) VALUES (%s);"
        cursor.execute(sql, (random.choice(name),))
        conn.commit()
        cursor.close()
        conn.close()
    except (mysql.connector.errors.ProgrammingError) as e:
        print(e)


@app.route('/')
def hello():
    create_table()
    insert_data()
    try:
        conn = conn_db()
        cursor = conn.cursor()
        sql = 'SELECT * FROM todos'
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
    except (mysql.connector.errors.ProgrammingError) as e:
        print(e)

    data = []
    for row in rows:
        data.append(OrderedDict(id=row[0], content=row[1]))
    j = json.dumps(data, indent=2, ensure_ascii=False)
    j = re.sub(r'"(\w+?)":', r'\1:', j)
    return j


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
