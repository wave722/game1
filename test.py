
import random

# Инициализация глобальных переменных
inventory = []
levels = {
    1: "Ключ для двери",
    2: "Монстр",
    3: "Загадка",
    4: "Выход из замка Монстра"
}
monster_defeated = False
completed_tasks = set()
keys_found = set()
monster_required_item = "Меч"
total_keys = 3

# Функция для отображения инвентаря
def show_inventory():
    print("Ваш рюкзак:", inventory if inventory else "пуст.")

# Функция для получения ключей
def collect_keys():
    global keys_found
    print("Вы ищете ключи в комнате...")
    keys = {f"ключ{num}" for num in range(1, total_keys + 1)}
    
    while keys:
        action = input("Что вы хотите сделать? (взять, проверить проверить рюкзак): ").lower()
        if action == "взять":
            key = random.choice(list(keys))
            keys.remove(key)
            keys_found.add(key)
            inventory.append(key)
            print(f"Вы нашли {key}. Осталось ключей: {len(keys)}.")
        elif action == "проверить рюкзак":
            show_inventory()
        else:
            print("Неверная команда, попробуйте снова.")
    print("Вы собрали все ключи")

# Функция для нахождения меч
def find_sword():
    print("Вы ищете мечь, чтобы победить Монстра.")
    if "меч" not in inventory:
        print("Вы нашли меч!")
        inventory.append("меч")

# Функция для уровня 1
def level_one():
    print("Вы находитесь в комнате где спрятаны ключи. Найдите ключи. На ключах будет код для выхода из замка.")
    collect_keys()

    while True:
        action = input("Что хотите сделать? (убежать, Рюкзак): ").lower()
        if action == "убежать" and keys_found:
            print("Вы убежали с ключами.")
            completed_tasks.add(levels[1])
            break
        elif action == "рюкзак":
            show_inventory()
        else:
            print("Неверная команда, попробуйте снова.")

# Функция для уровня 2
def level_two():
    global monster_defeated
    print("Вы вошли в темный коридор и встретили Монстра!")
    find_sword()

    while True:
        action = input("Что вы хотите сделать? (победить, убежать, рюкзак): ").lower()
        if action == "победить":
            if "меч" in inventory:
                print("Вы победили Монстра с помощью меча!")
                monster_defeated = True
                completed_tasks.add(levels[2])
                break
            else:
                print("Для победы над Монстра вам нужен меч!")
                continue
        elif action == "убежать":
            print("Вы убежали от Монстра, но все еще находитесь в замке.")
        elif action == "рюкзак":
            show_inventory()
        else:
            print("Неверная команда, попробуйте снова.")

# Функция для уровня 3
def level_three():
    print("Вы оказались в комнату, где вам загадали зададку. Отгадайте загадку.")
    puzzle_answer = "душ"

    while True:
        answer = input("То висячий, то стоячий, то холодный, то горячий").lower()
        if answer == puzzle_answer:
            print("Вы угадали!")
            completed_tasks.add(levels[3])
            break
        else:
            print("Неправильный ответ. Попробуйте еще раз.")

# Функция для уровня 4
def level_four():
    print("Вы находитесь у выхода из замка, но дверь закрыта.")
    secret_code = "гейсенин"  # Код для выхода

    while True:
        code = input("Введите код для выхода: ")
        if code == secret_code:
            print("Вы успешно выбрались из замка! Поздравляем!")
            completed_tasks.add(levels[4])
            break
        else:
            print("Неверный код. Попробуйте ещё раз.")

# Главная функция игры
def game():
    print("Добро пожаловать в замок Монстра!")
    level_one()
    if levels[1] in completed_tasks:
        print("Вы прошли уровень 1.")
    level_two()
    if monster_defeated:
        print("Вы прошли уровень 2.")
    level_three()
    if levels[3] in completed_tasks:
        print("Вы прошли уровень 3.")
    level_four()
    if levels[4] in completed_tasks:
        print("Вы завершили игру. Поздравляем!")

# Начало игры
if __name__ == "__main__":
    game()