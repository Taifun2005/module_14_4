import sqlite3
from itertools import product



def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER  NOT NULL
    );
    ''')
    connection.commit()
    connection.close()




def get_add_products(id, title, description, price, cursor=None):
    check_user = cursor.execute("SELECT * FROM Products WHERE id=?", (id,))

    if check_user.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES('{id}', '{title}', '{description}', '{price}')
''')
    connection.commit()


def get_all_products(cursor=None):
    cursor.execute("SELECT * FROM Products")
    total = cursor.fetchall()
    for prod in total:
        print(prod)

    connection.commit()
    connection.close()

get_all_products()
