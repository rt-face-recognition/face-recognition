import psycopg2
import time
from pprint import pprint

# class DatabaseConnection():
#     def __init__(self):
try:
    conn = psycopg2.connect()
    conn.autocommit = True
    cur = conn.cursor()
except:
    pprint("Cannot connect to database.")

def createTable():
    create_table_command = "CREATE TABLE Faces(name VARCHAR, time NUMERIC, id SERIAL UNIQUE)"
    cur.execute(create_table_command)

def insert_new_record(name):
    insert_command = "INSERT INTO \"Faces\" (name,time) VALUES ('{}','{}')".format(name,time.time())
    pprint(insert_command)
    cur.execute(insert_command)

def query_all():
    cur.execute("SELECT * FROM Faces")
    people = cur.fetchall()
    for entry in people:
        pprint("{0}".format(entry))

def update_record(name, time):
    update_command = "UPDATE \"Faces\" SET time={0} WHERE name='{1}'".format(time, name)
    cur.execute(update_command)


# if __name__ == "__main__":
#     database_connection = DatabaseConnection()
#     database_connection.createTable()