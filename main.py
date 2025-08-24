import db

def choice(option, db_manager):
    match option:
        case 1:
            title = input('Game title: ')
            while True:
                rating = input('Game rating: ')
                if rating.lstrip('-').isdigit():
                    float_rating = float(rating)
                    if 0 <= float_rating <= 10:
                        break
                    else:
                        print('Invalid Rating.')
                        continue
                else:
                    print('Enter a number')
            while True:
                status = input('Game status: ')
                if status.lstrip('-').isdigit():
                    print('Invalid status.')
                    continue
                else:
                    break
            new_game = db.Game(title, rating, status)
            db_manager.insert_game(new_game)
        case 2:
            db_manager.show_all()
        case 3:
            target_title = input('Search game title: ')
            db_manager.search_games(target_title)
        case 4:
            target_title = input('What game would you like to remove: (Title) ')
            db_manager.delete_game(target_title)
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
