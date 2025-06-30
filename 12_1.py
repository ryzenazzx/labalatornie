import json

def display_products(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            print("Информация о продуктах:")
            for product in data['products']:
                print(f"\nНазвание: {product['name']}")
                print(f"Цена: {product['price']} руб.")
                print(f"Вес: {product['weight']} г")
                if product['available']:
                    print("В наличии")
                else:
                    print("Нет в наличии!")
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except json.JSONDecodeError:
        print("Ошибка: файл содержит некорректные JSON-данные")
    except KeyError:
        print("Ошибка: в JSON отсутствуют необходимые поля")

# Пример использования
if __name__ == "__main__":
    filename = input("Введите имя JSON-файла (например: products.json): ")
    display_products(filename)