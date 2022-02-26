import sqlite3
from random import randint


def createTableVisitors():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS visitors (
                                    number INTEGER PRIMARY KEY,
                                    name_visitor TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    address TEXT NOT NULL  
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


def selectTableVisitors():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM visitors;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for record in records:
            print("Номер телефона:", record[0])
            print("Имя:", record[1])
            print("Фамилия:", record[2])
            print("Адресс:", record[3])

            print()
        cursor.close()



    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectTableVisitors1():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM visitors;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def insertManyDataVisitors(records):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        insert_data_query = '''INSERT INTO visitors(number, name_visitor , surname, address)
                               VALUES (?, ?, ?, ?);'''
        cursor.executemany(insert_data_query, records)
        sqlite_connection.commit()
        print("Посетителей успешно добавлено:", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectNameVisitor(name):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM visitors WHERE name_visitor = ?"
        cursor.execute(sqlite_select_query, (name,))
        records = cursor.fetchall()
        for record in records:
            print("Number:", record[0])
            print("Name:", record[1])
            print("Surname:", record[2])
            print("Address:", record[3])
            print()
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectAddressVisitor(address):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM visitors WHERE address = ?"
        cursor.execute(sqlite_select_query, (address,))
        records = cursor.fetchall()
        for record in records:
            print("Number:", record[0])
            print("Name:", record[1])
            print("Surname:", record[2])
            print("Address:", record[3])
            print()
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectSurnameVisitor(surname):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM visitors WHERE surname = ?"
        cursor.execute(sqlite_select_query, (surname,))
        records = cursor.fetchall()
        for record in records:
            print("Number:", record[0])
            print("Name:", record[1])
            print("Surname:", record[2])
            print("Address:", record[3])

            print()
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectVisitor(name, surname):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()


        sqlite_select_query = "SELECT * FROM visitors WHERE name_visitor = ? AND surname = ?;"
        cursor.execute(sqlite_select_query, (name, surname))
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")


def selectNumberVisitor(number):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT * FROM visitors WHERE number = ?"
        cursor.execute(sqlite_select_query, (number,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def inputDataVisitors():
    data = []
    while True:
        data_tuple = (randint(1000000, 9999999), input("Добавьте имя посетителя: "),
                      input("Добавьте фамилию посетителя: "), input("Добавьте адресс: ")
                      )
        data.append(data_tuple)
        if input("Хотите ввести ещё? (Да/Нет) ").capitalize() == "Нет":
            return data


def updateRecordVisitors(name, surname, address, number):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_update_query = "UPDATE visitors SET name=?, surname=?, address=? WHERE number=?"
        cursor.execute(sqlite_update_query, (name, surname, address, number))
        sqlite_connection.commit()

        cursor.close()
        print("Посетитель с номером телофна", number, "успешно изменен.")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def deleteVisitors(number):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM visitors WHERE number=?"
        cursor.execute(sqlite_delete_query, (number,))
        sqlite_connection.commit()

        cursor.close()
        print("Посетитель с телофоном", number, "успешно удален.")
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def deleteTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        create_table_query = '''DROP TABLE visitors
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