from PIL import Image, ImageDraw, ImageFont
import os

def add_congratulation(image_path, name, holiday):
    try:
        # Открываем изображение
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        
        # Выбираем шрифт (путь может отличаться в разных ОС)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.truetype("arialbd.ttf", 40)  # Попытка использовать жирный шрифт
        
        # Текст поздравления
        text = f"{name}, поздравляю с {holiday}!"
        
        # Рассчитываем позицию текста (центрирование)
        text_width = draw.textlength(text, font=font)
        x = (img.width - text_width) / 2
        y = img.height - 100  # Размещаем внизу
        
        # Добавляем обводку для лучшей читаемости
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                draw.text((x+dx, y+dy), text, font=font, fill="black")
        
        # Основной текст
        draw.text((x, y), text, font=font, fill="white")
        
        # Сохраняем результат
        output_path = f"congratulation_{os.path.basename(image_path)}"
        img.save(output_path)
        print(f"Открытка сохранена как {output_path}")
        img.show()
        
    except FileNotFoundError:
        print("Ошибка: файл с открыткой не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    image_path = input("Введите путь к изображению открытки: ")
    name = input("Кого хотите поздравить? ")
    holiday = input("С каким праздником? ")
    
    add_congratulation(image_path, name, holiday)