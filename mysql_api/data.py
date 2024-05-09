import unicodedata
import sys
import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)
from settings import MySqlDB

# def connect_db():
#     return mysql.connector.connect(
#             host= 'localhost',
#             user= 'root',
#             password= 'Phamvanbao_0123',
#             database= 'books'
#     )
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    output = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    output = output.replace('đ', 'd').replace('Đ', 'D')
    return output
def save_to_db(data):
    try:
        db = MySqlDB()
        cnx = db.connect()
        cursor = cnx.cursor()
        if len(data) != 0:
            for post in data:
                try:
                    cursor.execute("INSERT INTO books (id_book, title, author, thumb, content_type, liked, price) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                   (post['id'], remove_accents(post['title']), remove_accents(post['authors'][0]['name']), post['thumb'], post['content_type'], post['liked'], post['price']))
                except Exception as e:
                    print("Error inserting data:", e)
                    print("Data:", post)
        else:
            print("No data to insert")
        cnx.commit()
    except Exception as e:
        print("Database connection or SQL error:", e)
    finally:
        cursor.close()
        cnx.close()

def get_books():
    db = MySqlDB()
    cnx = db.connect()
    cursor = cnx.cursor()
    try:
        cursor.execute("select * from books")
        records = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        return records
    except:
        print("loi khi lay du lieu")
def search_books(key_word):
    db = MySqlDB()
    cnx = db.connect()
    cursor = cnx.cursor()
    print("select * from books where title like '"+key_word+"%'")
    if(len(key_word)!=0):
        try:
            cursor.execute("select * from books where title like '"+key_word+"%'")
            records = cursor.fetchall()
            cnx.commit()
            cursor.close()
            cnx.close()
            return records
        except:
            print("loi khi lay du lieu")

    