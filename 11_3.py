import csv

def calculate_expenses(filename):
    try:
        total = 0
        print("Нужно купить:")
        
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                product = row['Продукт']
                quantity = int(row['Количество'])
                price = int(row['Цена'])
                cost = quantity * price
                total += cost
                
                print(f"{product} - {quantity} шт. за {price} руб.")
        
        print(f"\nИтоговая сумма: {total} руб.")
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден!")
    except KeyError:
        print("Ошибка: некорректные заголовки столбцов в CSV-файле")
    except ValueError:
        print("Ошибка: некорректные данные в столбцах 'Количество' или 'Цена'")

# Пример использования
if __name__ == "__main__":
    filename = input("Введите имя CSV-файла (например: products.csv): ")
    calculate_expenses(filename)