import os

import mysql.connector
from mysql.connector import Error


class MySQLConnection:
    def __init__(self, host, username, password, database):
        self.connection = mysql.connector.connect(host=host,
                                                  database=database,
                                                  user=username,
                                                  password=password)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        result = []
        try:
            self.cursor.execute(query, params)
            if 'SELECT' in query.upper():
                result = self.cursor.fetchall()
            if 'INSERT' in query.upper():
                self.connection.commit()
                result = self.cursor.lastrowid
            else:
                self.connection.commit()
        except Error as e:
            print(f"Erro ocorreu: {e}")
        
        # ==== todo remover depois ====
        print("-"* 50)
        print(query)
        print("-"* 50)
        print(params)
        print("-"* 50)
        print(result)
        print("-"* 50)
        # =============================

        return result

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

def executar(sql, val = None):
    
    db = MySQLConnection(
        host = os.getenv('HOST'),
        username = os.getenv('USER'),
        password = os.getenv('PASS'),
        database = os.getenv('DATABASE')
    )

    resultado = db.execute(sql, val)

    db.close()
    return resultado
