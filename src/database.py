import psycopg2
import time
from pprint import pprint

class DatabaseConnection():
    def __init__(self):
        try:
            self.connection = psycopg2.connect()
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database.")

    def createTable(self):
        create_table_command = "CREATE TABLE Faces(name VARCHAR, time NUMERIC, id SERIAL UNIQUE)"
        self.cursor.execute(create_table_command)

    def insert_new_record(self, name):
        insert_command = "INSERT INTO \"Faces\" (name,time) VALUES ('{}','{}')".format(name,time.time())
        pprint(insert_command)
        self.cursor.execute(insert_command)

    def query_all(self):
        self.cursor.execute("SELECT * FROM Faces")
        people = self.cursor.fetchall()
        for entry in people:
            pprint("{0}".format(entry))

    def update_record(self, name, time):
        update_command = "UPDATE \"Faces\" SET time={0} WHERE name='{1}'".format(time, name)
        self.cursor.execute(update_command)


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.createTable()