from PIL import Image, ImageEnhance
import os

def apply_filter(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(1, 6):
        try:
            img = Image.open(f"{input_folder}/{i}.jpg")
            enhancer = ImageEnhance.Contrast(img)
            filtered_img = enhancer.enhance(1.5)  # Увеличение контраста
            filtered_img.save(f"{output_folder}/filtered_{i}.jpg")
        except FileNotFoundError:
            print(f"Файл {i}.jpg не найден!")

apply_filter("input_images", "output_images")