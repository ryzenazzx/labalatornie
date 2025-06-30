def is_divisible_by_3(number):
    return number % 3 == 0

num = int(input("Введите число: "))
if is_divisible_by_3(num):
    print("Число делится на 3")
else:
    print("Число не делится на 3")