x = 0
y = 0
import art
import random

hp = 100
ex = 0
money = 15
equipment = [0, 0, x, y, 0]


def play():
    print("1. Магазин")
    print("2. Подземелье")
    print("3. Цветочная полянка")
    choise_loc = input("Выберите локацию: ")
    if choise_loc == "1":
        shop()
    elif choise_loc == "2":
        dungeon()


def shop():
    while True:

        # Сама игра собственно говоря!!!

        print("Вы зашли в магазин.")
        print("Пред вами открывается список товаров!")
        print("1. Лук и стрелы - 15 монет")
        print("2. Меч - 25 монет")
        print("3. Зелье лечения - 10 монет")
        print("4. Бомба - 20 монет")
        print("5. Броня - 40 монет")
        print("6. Выйти")
        magazin = [15, 25, 10, 20, 40]
        choise_mag = input("Выберите товар: ")
        if choise_mag == "1" and money >= magazin[0]:
            print("Вы купили лук и стрелы!")
            equipment[0] = 1
            money = money - 15
        elif choise_mag == "2" and money >= magazin[1]:
            print("Вы купили меч!")
            equipment[1] = 1
            money = money - 25
        elif choise_mag == "3" and money >= magazin[2]:
            print("Вы купили зелье лечения!")
            x = x + 1
            money = money - 10
        elif choise_mag == "4" and money >= magazin[3]:
            print("Вы купили бомбу!")
            y = y + 1
            money = money - 20
        elif choise_mag == "5" and money >= magazin[4]:
            print("Вы купили броню!")
            equipment[4] = 1
            money = money - 40
        elif choise_mag == "6":
            play()
            break
        else:
            print("У вас недостаточно денег!")


def dungeon():
    while True:
        print("Вы зашли в подземелье.")
        print("Табличка: Добро пожаловать в подземелье имени Лича Эрлен...")
        print("Дальше табличка стёрта...")
        print("1. Продвинуться дальше по подземелью")
        print("2. Обыск")
        print("3. Выйти")
        choise_dungeon = input("Выберете действие: ")
        if choise_dungeon == "1":
            fight()
        elif choise_dungeon == "2":
            search()
        elif choise_dungeon == "3":
            play()


def fight():
    pass


def search():
    d = 1
    global x, y
    search = ["Вы нашли: Зелье лечения!", "Вы нашли: Зелье лечения!", "Вы нашли: Зелье лечения!", "Вы нашли: Бомба!", "Вы нашли: Бомба!", "Вы нашли: Меч!"]
    searchx = random.choice(search)
    if search.index(searchx) == 0 or search.index(searchx) == 1 or search.index(searchx) == 2:
        x = x + 1
        print("Вы нашли зелье здоровья!")
        d = d - 1
    elif search.index(searchx) == 3 or search.index(searchx) == 4:
        y = y + 1
        print("Вы нашли взрывную-разрывную бомбу!")
        d = d - 1
    elif search.index(searchx) == 5:
        equipment[4] = 1
        print("Вы нашли крепкую броню!")
        d = d - 1
    elif d == 0:



def quit_dungeon():
    play()


def guide():
    print("Для того чтобы начать играть, сначала нужно выбрать локацию для игры.")
    print("В зависимости от выбранной локации, вам нужно будет сделать определённые действия.")
    print("Например: Если вы выбрали локацию Магазин, то вам нужно будет купить что-то.")
    print(
        "А если вы выберете локацию Подземелье, то вам нужно будет сражаться с монстрами посредством выбора действий. Удачи!")


def quit():
    print("Истинная концовка! Вы вышли из игры нафиг!")
    exit()


while True:
    print("\nTHE DANGEROUS DANGEOUS")
    print(art.tprint("THE DUNGEON"))
    print("1. Играть")
    print("2. Как играть")
    print("3. Выйти нафиг")
    choise = input("Выберите действие: ")
    if choise == "1":
        play()
        break
    elif choise == "2":
        guide()
    elif choise == "3":
        quit()