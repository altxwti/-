import random
while True:

    com = ["камень", "ножницы", "бумага"]
    print("Введите: 1 = камень, 2 = ножницы, 3 = бумага")
    a = str(input())
    c = random.choice(com)

    if a == "1":
        a = "камень"
    elif a == "2":
        a = "ножницы"
    elif a == "3":
        a = "бумага"

    print(f"Вы выбрали: {a}", "Комп: {c}")

    if a == c:
        print("ничья")
    elif a == "камень":
        if c == "ножницы":
            print("Победа")
        elif c == "бумага":
            print("Проигрыш")
    elif a == "ножницы":
        if c == "бумага":
            print("Победа")
        else:
            print("Проигрыш")
    elif a == "бумага":
        if c == "камень":
            print("Победа")
        else:
            print("Проигрыш")

