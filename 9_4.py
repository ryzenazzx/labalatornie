from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text):
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 40)
        
        # Прозрачный водяной знак
        for x in range(0, img.width, 200):
            for y in range(0, img.height, 200):
                draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
        
        img.save("watermarked_" + image_path)
        print("Водяной знак добавлен!")
    except FileNotFoundError:
        print("Файл не найден!")

add_watermark("photo.jpg", "SAMPLE")