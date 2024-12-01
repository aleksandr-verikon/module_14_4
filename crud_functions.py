import sqlite3


def initiate_db(db_name='products.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    """

    cursor.execute(create_table_query)

    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product1", "Описание1", "100"))
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product2", "Описание2", "200"))
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product3", "Описание3", "300"))
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product4", "Описание4", "400"))

    connection.commit()
    connection.close()


initiate_db()


def get_all_products(db_name='products.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    select_query = "SELECT * FROM Products;"
    cursor.execute(select_query)

    products = cursor.fetchall()
    connection.close()
    return products

