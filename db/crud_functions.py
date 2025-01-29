import sqlite3


def initiate_db():
    conn = sqlite3.connect('./db/Products.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('DELETE FROM Products')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Витамины №{i}', f'Описание витаминов №{i}', i * 150))
    conn.commit()
    conn.close()
    conn = sqlite3.connect('./db/Users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('./db/Products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def add_user(username, email, age):
    conn = sqlite3.connect('./db/Users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, 1000)', (username, email, age))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('./db/Users.db')
    cursor = conn.cursor()
    check_name = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    try:
        if check_name.fetchone()[1] == username:
            return True
    except TypeError:
        return False
    finally:
        conn.close()
