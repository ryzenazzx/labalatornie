from PIL import Image

def crop_image(image_path, x1, y1, x2, y2):
    try:
        img = Image.open(image_path)
        cropped = img.crop((x1, y1, x2, y2))
        cropped.save("cropped_" + image_path)
        print("Изображение обрезано!")
    except FileNotFoundError:
        print("Файл не найден!")

# Пример: crop_image("postcard.jpg", 100, 100, 400, 300)