from PIL import Image

def analyze_image(image_path):
    try:
        img = Image.open(image_path)
        print(f"Формат: {img.format}")
        print(f"Размер: {img.size}")
        print(f"Цветовая модель: {img.mode}")
        img.show()
    except FileNotFoundError:
        print("Файл не найден!")

analyze_image("example.jpg")