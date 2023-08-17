import sqlite3
from sqlite3 import Error, Connection
import os


# TODO  move the empty string check and quotation mark removal into txtParsers.py

def createConnection(path='./db/test.db'):
    cx = None
    try:
        cx = sqlite3.connect(path)
        print('Connected to database')
    except Error:
        print(f'The error {Error} occured')

    return cx


def executeQuery(connection: Connection, query: str):
    try:
        cu = connection.execute(query)
        connection.commit()
        print('Query successful')
        return cu
    except Error:
        print(f'The error {Error} occured')


def createTable(connection: Connection, tableName: str):
    # 'tableName' must be a valid sqlite table name
    createTable = f'''CREATE TABLE {tableName}(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price TEXT
                        ) 
                    '''
    executeQuery(connection, createTable)


def iterateOverParsedFiles(connection: Connection):
    folder_path = './menus/parsed'

    # TODO Reduce nesting. store filepaths in an array and iterate over that?

    # Iterate over the parsed menus
    for filename in os.listdir(folder_path):
        filePath = f'{folder_path}/{filename}'

        if os.path.isfile(filePath):
            # Assuming all files end in '.txt'
            restaurant = filename[:-4].replace('-', '')
            createTable(connection, restaurant)

            txt = open(filePath).read()

            # Remove all quotation marks
            lines = txt.replace('\'', '').replace('"', '').splitlines()

            for line in lines:
                name, sep,  price = line.partition('$')

                name = name.strip()
                price = price.strip()

                if name != '' and price != '':
                    insertIntoTable = f'INSERT INTO {restaurant}(name,price) VALUES ("{name}", "{price}");'
                    executeQuery(connection, insertIntoTable)


def searchAllTables(connection: Connection, substr: str) -> dict:
    res = {}

    # Query the sqlite_master table to get all table names
    getTableNames = f'SELECT name FROM sqlite_master WHERE type="table";'

    # 'tables' is a list of tuples
    tables = executeQuery(connection, getTableNames).fetchall()

    for table in tables:
        tableName = table[0]
        findWine = f'SELECT name, price FROM {tableName} WHERE name LIKE "%{substr}%";'

        res[tableName] = executeQuery(connection, findWine).fetchall()

    return res


# Uncomment to create tables and records for each file
# iterateOverParsedFiles(createConnection())
