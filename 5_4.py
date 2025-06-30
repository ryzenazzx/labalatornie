import random

correct = 0
mistakes = 0

while mistakes < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = input(f"{a} + {b} = ")
    
    if answer.isdigit() and int(answer) == a + b:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct}")