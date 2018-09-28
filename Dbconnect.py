import psycopg2
import psycopg2.extras as extras


class Databaseconnection(object):

    def __init__(self):

        try:
            connection_credit ="""
            dbname = 'postgres' user='postgres' password='xxlii'
            host = 'localhost' port = '5432'
            """
            self.connection = psycopg2.connect(connection_credit)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("\ndatabase connected\n")
        except Exception as e:
            print(e)
            print("\ndatabase connect failed\n")



