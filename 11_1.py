from PIL import Image
import os

def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                img = Image.open(f"{input_dir}/{filename}")
                gray_img = img.convert('L')  # Ч/Б фильтр
                gray_img.save(f"{output_dir}/gray_{filename}")
            except Exception as e:
                print(f"Ошибка обработки {filename}: {e}")

process_images("photos", "processed_photos")