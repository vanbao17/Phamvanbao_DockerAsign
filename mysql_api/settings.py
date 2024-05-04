import mysql.connector
class MySqlDB():
    DB_CONFIG = {
        'host': 'mysql',
        'user': "root",
        'password': "psw123",
        'database': 'BooksWaka'
    }
    
    def connect(self):
        cnx = mysql.connector.connect(**self.DB_CONFIG)
        return cnx