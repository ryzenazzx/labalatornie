lst = [1, 2, 3, 2, 4, 5, 4]
duplicates = set(x for x in lst if lst.count(x) > 1)

if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Нет повторяющихся элементов")