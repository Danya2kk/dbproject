import sqlite3


def createTableBooklist():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS booklist (
                                    id INTEGER PRIMARY KEY,
                                    book_id INTEGER NOT NULL,
                                    visitor_number INTEGER NOT NULL); '''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def lastID():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT MAX(id) FROM booklist;"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchone()
        cursor.close()
        if record[0] == None:
            return 0
        return record[0]
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def addBook(visitor: int, book: int) -> None:
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        insert_query = '''INSERT INTO booklist (id, book_id, visitor_number)
                           VALUES (?, ?, ?);'''

        cursor.execute(insert_query, (lastID() + 1, book, visitor),)
        sqlite_connection.commit()
        cursor.close()
        print("Добавлена книга для человека с номером", visitor, end=".\n")

    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite")

        sqlite_select_query = "SELECT * FROM booklist;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def deleteTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        create_table_query = '''DROP TABLE booklist
                                '''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица удалена успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectBooks(visitor: tuple) -> list:
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = '''SELECT number, name_visitor, surname, name, author
                                FROM booklist JOIN visitors ON visitors.number = booklist.visitor_number
                                                JOIN books ON books.id = booklist.book_id
                                                WHERE visitor_number = ?;
                                '''
        cursor.execute(sqlite_select_query, (visitor[0],))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()