import os

import psycopg2
from psycopg2 import Error


class PostgreSQLConnection:
    def __init__(self, host, username, password, database):
        self.connection = psycopg2.connect(host=host,
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
                result = self.cursor.fetchone()[0]
            else:
                self.connection.commit()
        except Error as e:
            print(f"Erro ocorreu: {e}")
        
        return result

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()


def executar(sql, val=None):
    db = PostgreSQLConnection(
        host=os.getenv('HOST'),
        username=os.getenv('USER'),
        password=os.getenv('PASS'),
        database=os.getenv('DATABASE')
    )

    resultado = db.execute(sql, val)

    db.close()
    return resultado
