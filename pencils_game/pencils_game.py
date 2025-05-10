import random


def get_pencils_count():
    """Функция для ввода количества карандашей с проверкой"""
    while True:
        pencils = input("How many pencils would you like to use:\n")
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils)
        if pencils <= 0:
            print("The number of pencils should be positive")
            continue
        return pencils


def get_first_player():
    """Функция для выбора первого игрока"""
    players = ["John", "Jack"]
    while True:
        first_player = input(f"Who will be the first ({', '.join(players)}):\n")
        if first_player not in players:
            print(f"Choose between {players[0]} and {players[1]}")
            continue
        return first_player


def get_human_move(pencils_left):
    """Функция для хода игрока-человека"""
    while True:
        move = input()
        if not move.isdigit():
            print("Possible values: '1', '2' or '3'")
            continue
        move = int(move)
        if move not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
            continue
        if move > pencils_left:
            print("Too many pencils were taken")
            continue
        return move


def bot_move(pencils_left):
    """Функция для хода бота с выигрышной стратегией"""
    if pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1
    elif pencils_left == 1:
        return 1
    else:
        return random.randint(1, min(3, pencils_left))


def main():
    """Основная функция игры"""
    # Получаем начальные параметры
    pencils = get_pencils_count()
    first_player = get_first_player()

    # Инициализация игры
    current_player = first_player
    remaining_pencils = pencils

    # Начальное состояние
    print("|" * remaining_pencils)
    print(f"{current_player} is going first!")

    # Основной игровой цикл
    while remaining_pencils > 0:
        print(f"{current_player}'s turn!")

        # Обработка хода
        if current_player == "Jack":
            move = bot_move(remaining_pencils)
            print(move)
        else:
            move = get_human_move(remaining_pencils)

        # Обновление состояния
        remaining_pencils -= move

        # Проверка окончания игры
        if remaining_pencils <= 0:
            print(f"{current_player} won!")
            break

        # Отображение текущего состояния
        print("|" * remaining_pencils)

        # Смена игрока
        current_player = "Jack" if current_player == "John" else "John"


if __name__ == "__main__":
    main()