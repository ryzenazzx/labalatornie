color1 = input("Введите первый цвет (красный, синий, желтый): ").lower()
color2 = input("Введите второй цвет (красный, синий, желтый): ").lower()

if color1 not in ["красный", "синий", "желтый"] or color2 not in ["красный", "синий", "желтый"]:
    print("Ошибка: введены не основные цвета")
else:
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        print("Фиолетовый")
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        print("Оранжевый")
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        print("Зеленый")
    else:
        print("Ошибка: одинаковые цвета")