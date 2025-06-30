def divide_100():
    try:
        num = float(input("Введите число: "))
        result = 100 / num
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")

divide_100()