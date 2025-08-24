import db

def choice(option, db_manager):
    match option:
        case 1:
            title = input('Game title: ')
            rating = input('Game rating: ')
            status = input('Game status: ')
            new_game = db.Game(title, rating, status)
            db_manager.insert_game(new_game)
        case 2:
            db_manager.show_all()
        case 5:
            return False
    return True


def main():
    db_manager = db.DatabaseManager()
    while True:
        user_choice = db.menu()
        should_continue = choice(user_choice, db_manager)
        if not should_continue:
            break


if __name__ == "__main__":
    main()



