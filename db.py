import sqlite3
from curses.ascii import isdigit
from os.path import isdir

class DatabaseManager:
    def __init__(self, db_name='game_backlog.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS games
            (
                id INTEGER PRIMARY KEY,
                title TEXT,
                rating REAL,
                status TEXT DEFAULT 'Want to play'
            )
            """)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def insert_game(self, game):
        query = """
            INSERT INTO games (title, rating, status) VALUES (?, ?, ?)
        """
        values = (game.title, game.rating, game.status)
        self.cursor.execute(query, values)
        self.conn.commit()

    def show_all(self):
        query = "SELECT * FROM games"
        self.cursor.execute(query)
        items = self.cursor.fetchall()
        for game in items:
            print(game)


# Games
class Game:
    def __init__(self, title, rating, status):
        self.title = title
        self.rating = rating
        self.status = status

def menu():
    print('=-'*20)
    print('1- Add new game')
    print('2- Show BackLog')
    print('3- Search for game')
    print('4- Delete game from BackLog')
    print('5- Exit')
    print('=-'*20)
    while True:
        option = input('Select an option: ')
        if option.isdigit():
            int_option = int(option)

            if 1 <= int_option <= 5:
                return int_option
            else:
                print('Please enter a valid option.')
        else:
            print('Invalid input. Please enter a number')

