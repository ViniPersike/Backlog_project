import sqlite3

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
        values = (game.title.title(), game.rating, game.status.title())
        self.cursor.execute(query, values)
        self.conn.commit()
        print('Game added successfully.')

    def show_all(self):
        query = "SELECT * FROM games ORDER BY title"
        self.cursor.execute(query)
        items = self.cursor.fetchall()
        for index, game in enumerate(items):
            print(f'{index}- {game[1]:<30} | Rating: {game[2]:<6} | Status: {game[3]:<10}')

    def delete_game(self, game_title):
        game_query = "SELECT id, title FROM games WHERE title = (?) ORDER BY title LIMIT 1"
        self.cursor.execute(game_query, (game_title.title(),))
        game = self.cursor.fetchone()
        if game:
            game_id, title = game
            delete_query = "DELETE FROM games WHERE id = (?)"
            while True:
                opt = input('Are you sure? [y/n] ')
                should_continue = self.confirm_operation(opt.lower())
                if should_continue == True:
                    print('Invalid option.')
                    continue
                else:
                    if opt == 'y':
                        self.cursor.execute(delete_query, (game_id,))
                        self.conn.commit()
                        print(f'{title.capitalize()} was deleted successfully.')
                        break
                    else:
                        print('Operation cancelled.')
                        break
        else:
            print(f'No games found.')

    def search_games(self, game_title):
        query = "SELECT * FROM games WHERE title LIKE (?)"
        self.cursor.execute(query, (game_title+'%',))
        game_list = self.cursor.fetchall()
        if game_list:
            for index, game in enumerate(game_list):
                print(f'{index}- {game[1]:<30} | Rating: {game[2]:<6} | Status: {game[3]:<10}')
        else:
            print('No games found.')

    def confirm_operation(self, option):
        if option not in ['y','n']:
            return True
        else:
            return option


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
