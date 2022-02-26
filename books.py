import sqlite3


def createTableBooks():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMARY KEY,
                                    name_book TEXT NOT NULL,
                                    author_book TEXT NOT NULL,
                                    volumes_book INTEGER NOT NULL  
                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectTableBooks():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite")

        sqlite_select_query = "SELECT * FROM books;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for record in records:
            print("ID:", record[0])
            print("Название книги:", record[1])
            print("Автор:", record[2])
            print("Количество томов:", record[3])
            print()
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def insertManyDataBooks(records):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        insert_data_query = '''INSERT INTO books(id, name, author, volumes)
                               VALUES (?, ?, ?, ?);'''
        cursor.executemany(insert_data_query, records)
        sqlite_connection.commit()
        print("Записей успешно добавлено:", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def selectNameBook(name):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite")

        sqlite_select_query = "SELECT * FROM books WHERE name = ?"
        cursor.execute(sqlite_select_query, (name,))
        records = cursor.fetchall()
        for record in records:
            print("ID:", record[0])
            print("Название книги:", record[1])
            print("Автор:", record[2])
            print("Количество томов:", record[3])
            print()
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectAuthorBook(author):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * FROM books WHERE author = ?"""
        cursor.execute(sqlite_select_query, (author,))
        records = cursor.fetchall()
        for record in records:
            print("ID:", record[0])
            print("Название книги:", record[1])
            print("Автор:", record[2])
            print("Количество томов:", record[3])
            print()

            cursor.close()

    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectVolumesBook(volumes):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM books WHERE volumes = ?"
        cursor.execute(sqlite_select_query, (volumes,))
        records = cursor.fetchall()
        for record in records:
            print("ID:", record[0])
            print("Название книги:", record[1])
            print("Автор:", record[2])
            print("Количество томов:", record[3])
            print()
        cursor.close()

    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def inputDataBooks():
    data = []
    i = 1
    while True:
        data_tuple = (lastID() + i, input("Добавьте название книги: "), input("Добавьте автора книги: "),
                      int(input("Добавьте количество томов: ")))
        data.append(data_tuple)
        if input("Хотите ввести ещё? (Да/Нет) ").capitalize() == "Нет":
            return data
        i += 1


def lastID():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT MAX(id) FROM books;"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchone()
        cursor.close()
        return record[0]
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


# def selectBooks(visitor: tuple) -> list:
#     try:
#         sqlite_connection = sqlite3.connect("sqlite_pyth.db")
#         cursor = sqlite_connection.cursor()
#
#         sqlite_select_query = '''SELECT name_visitor, surname, name FROM visitors JOIN books
#                                     ON visitors.id_book = books.id
#
#                                     '''
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         cursor.close()
#         return records
#     except sqlite3.Error as error:
#         print("При работе с базой данных возникла ошибка:", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()