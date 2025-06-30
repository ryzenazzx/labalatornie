result = []

while True:
    word = input("Введите слово (для остановки введите 'stop'): ")
    if word == "stop":
        break
    result.append(word)

print("Результат:", " ".join(result))