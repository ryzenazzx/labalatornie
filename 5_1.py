n = int(input("Введите количество слов: "))
result = []

for i in range(n):
    word = input(f"Введите слово {i+1}: ")
    result.append(word)

print("Результат:", " ".join(result))