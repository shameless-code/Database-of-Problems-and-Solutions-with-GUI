#!/usr/bin/python3

# Native Python imports
import sqlite3


class SQLiteConnection:
    """Makes sure that database's connection has been closed after use"""

    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


class Database:
    """Allows to create and modify one-table database"""

    def __init__(self, database_file):
        self.database_file = database_file
        self.Q_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS problems(' \
                              'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,' \
                              'name TEXT NOT NULL UNIQUE,' \
                              'problem TEXT NOT NULL,' \
                              'solution TEXT NOT NULL' \
                              ');'
        self.Q_ADD              = 'INSERT INTO problems(name, problem, solution) VALUES (?, ?, ?);'
        self.Q_UPDATE           = 'UPDATE problems SET problem = ?, solution = ?' \
                                  ' WHERE name = ? LIMIT 1;'
        self.Q_DELETE           = 'DELETE FROM problems WHERE name = ? LIMIT 1;'
        self.Q_SELECT_NAMES     = 'SELECT name FROM problems;'
        self.Q_SELECT_CONTENT   = 'SELECT * FROM problems WHERE name = ?;'
        self.Q_SELECT_TABLE     = 'SELECT * FROM problems;'
        self.Q_CHECK_CONTENT    = 'SELECT id, name, problem, solution FROM problems LIMIT 1;'

    def check_file(self):
        """Check if file provided as database fulfill requirements for the program"""

        with SQLiteConnection(self.database_file) as db_connection:
            select_cursor = db_connection.cursor()
            return select_cursor.execute(self.Q_CHECK_CONTENT).fetchall()

    def create_table(self):
        """Creates table which is the core of whole database"""

        with SQLiteConnection(self.database_file) as db_connection:
            db_connection.execute(self.Q_CREATE_TABLE)
            db_connection.commit()

    def add(self, name, problem, solution):
        """Adds a row of data"""

        name = str(name).strip()  # Prevents white symbols in names
        with SQLiteConnection(self.database_file) as db_connection:
            db_connection.execute(self.Q_ADD, (name, problem, solution,))
            db_connection.commit()

    def update(self, problem, solution, name_update):
        """Updates with provided data the row with provided name"""

        name_update = str(name_update).strip()  # Prevents white symbols in names
        with SQLiteConnection(self.database_file) as db_connection:
            db_connection.execute(self.Q_UPDATE, (problem, solution, name_update,))
            db_connection.commit()

    def delete(self, name_delete):
        """Deletes the row with provided name"""

        with SQLiteConnection(self.database_file) as db_connection:
            db_connection.execute(self.Q_DELETE, (name_delete,))
            db_connection.commit()

    def select_names(self):
        """Returns all names for each row of data"""

        with SQLiteConnection(self.database_file) as db_connection:
            select_cursor = db_connection.cursor()
            for content in select_cursor.execute(self.Q_SELECT_NAMES).fetchall():
                yield content['name']

    def select_content(self, select_where):
        """Returns a row with provided name"""

        with SQLiteConnection(self.database_file) as db_connection:
            select_cursor = db_connection.cursor()
            return select_cursor.execute(self.Q_SELECT_CONTENT, (select_where,)).fetchall()

    def select_table(self):
        """Returns a whole table"""

        with SQLiteConnection(self.database_file) as db_connection:
            select_cursor = db_connection.cursor()
            return select_cursor.execute(self.Q_SELECT_TABLE).fetchall()

    def insert_dummy_data(self):
        """Fills database with dummy data to allows testing"""

        self.create_table()
        self.add('Name content','Problem content','Solution content',)
        self.add('Hello!','This is Problem','And that is Solution',)
