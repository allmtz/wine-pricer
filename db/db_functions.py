import sqlite3
from sqlite3 import Error, Connection
import os

# Define a relative path to the db
pathToTestDB = "./test.db"


def createConnection(path=pathToTestDB):
    cx = None
    try:
        cx = sqlite3.connect(path)
        print('Connected to database')
    except Error:
        print(f'The error {Error} occured')

    return cx


def executeQuery(connection: Connection, query: str, params=[]):
    try:
        cu = connection.execute(query, params)
        connection.commit()
        print('Query successful')
        return cu
    except sqlite3.Error as err:
        print(
            f'The error {err.sqlite_errorname}({err.sqlite_errorcode}) occured. Query: {query} Params: {params}')


def createTable(connection: Connection):
    createTable = f'''CREATE TABLE IF NOT EXISTS wines(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price TEXT,
                            restaurant TEXT,
                            varietal TEXT DEFAULT '',
                            vintage INTEGER DEFAULT -1,
                            added DATE DEFAULT (date()),
                            modified DATE DEFAULT (date()),
                            UNIQUE(name,restaurant)
                        );
                    '''
    executeQuery(connection, createTable, [])


def iterateOverParsedFiles(connection: Connection):
    folder_path = './menus/parsed'

    # TODO Reduce nesting

    # Iterate over the parsed menus
    for filename in os.listdir(folder_path):
        filePath = f'{folder_path}/{filename}'

        if os.path.isfile(filePath):
            # remove the '.txt' extension and replace seperators with spaces
            restaurant = filename[:-4].replace('-', ' ')

            lines = open(filePath).read().splitlines()

            for line in lines:
                name, sep,  price = line.partition('$')

                name = name.strip()
                price = price.strip()

                if name != '' and price != '':
                    # Create record
                    insertIntoTable = f'''INSERT INTO wines(name, price, restaurant)
                                            VALUES (?, ?, ?)
                                            ON CONFLICT(name,restaurant) DO NOTHING
                                            ;
                                        '''

                    # print(name, price, restaurant) # Useful for determining which queries failed
                    executeQuery(connection, insertIntoTable,
                                 [name, price, restaurant])


def findSubstring(connection: Connection, substr: str) -> dict:
    findWines = f'SELECT name, price, restaurant FROM wines WHERE name LIKE "%{substr}%" ORDER BY restaurant;'
    return executeQuery(connection, findWines, [])


def initializeDatabase(path):
    con = createConnection(path)
    createTable(con)
    iterateOverParsedFiles(con)
    con.close()


def main():
    initializeDatabase(pathToTestDB)


# uncommenting main() breaks docker compose watch
# main()
