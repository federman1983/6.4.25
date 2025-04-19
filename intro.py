import sqlite3

class Table:
    dbname = "mydb.db"
    @staticmethod
    def get_connection():
        connection = sqlite3.connect(Table.dbname)
        return connection
    # @staticmethod
    # def create_table_cities():
    #     with Table.get_connection() as connection:


        


print("Hello")
Table.get_connection()