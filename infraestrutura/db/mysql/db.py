import os

import mysql.connector


class MySQLConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )

    def execute(self, query, params=None):
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        result = cursor.fetchall()
        cursor.close()

        return result

    def close(self):
        if self.connection:
            self.connection.close()


def executar(sql, val = {}):
    
    db = MySQLConnection(
        host = os.getenv('HOST'),
        username = os.getenv('USER'),
        password = os.getenv('PASS'),
        database = os.getenv('DATABASE')
    )

    resultado = db.execute(sql, val)
    db.close()
    return resultado
