countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим"
}

# a) Все пары ключ-значение
print("Страны и их столицы:")
for country, capital in countries.items():
    print(f"{country}: {capital}")

# b) Столица для определённой страны
country = input("\nВведите страну: ")
print(f"Столица: {countries.get(country, 'Не найдена')}")

# c) Сортировка по алфавиту
print("\nОтсортированный словарь:")
for country in sorted(countries):
    print(f"{country}: {countries[country]}")