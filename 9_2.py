from PIL import Image, ImageOps

def process_image(image_path):
    try:
        img = Image.open(image_path)
        
        # Уменьшение в 3 раза
        small_img = img.resize((img.width // 3, img.height // 3))
        small_img.save("small_" + image_path)
        
        # Зеркальное отражение
        mirror_h = ImageOps.mirror(img)
        mirror_v = ImageOps.flip(img)
        
        mirror_h.save("mirror_h_" + image_path)
        mirror_v.save("mirror_v_" + image_path)
        
        print("Обработка завершена!")
    except FileNotFoundError:
        print("Файл не найден!")

process_image("example.jpg")