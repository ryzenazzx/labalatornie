import json

def add_product(filename):
    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            new_product = {
                "name": input("Название: "),
                "price": float(input("Цена: ")),
                "available": input("В наличии (да/нет): ").lower() == "да",
                "weight": int(input("Вес: "))
            }
            data["products"].append(new_product)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Товар добавлен!")
    except FileNotFoundError:
        print("Файл не найден!")

add_product("products.json")