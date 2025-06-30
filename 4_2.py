place = int(input("Введите номер места (1-54): "))

if place < 1 or place > 54:
    print("Неверный номер места")
else:
    if place % 2 == 0:
        seat_type = "верхнее"
    else:
        seat_type = "нижнее"
    
    if place > 36:
        location = "боковое"
    else:
        location = "в купе"
    
    print(f"Место {place}: {seat_type}, {location}")