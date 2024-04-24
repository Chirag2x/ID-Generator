import csv
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import zipfile
import os

ID_WIDTH, ID_HEIGHT = 85.60 * 2.83465, 53.98 * 2.83465
template_path = 'ute_id_template.png'
csv_path = 'Book - Copy - Copy(Sheet1).csv'
zip_path = 'Images.zip'
output_pdf_path = 'employee_id_cards.pdf'
font_path = 'Merriweather-Italic.ttf'

def draw_id_card(template_path, photo_path, name, title):
    template_image = Image.open(template_path)
    photo_image = Image.open(photo_path)

    photo_image = photo_image.resize((100, 100)) 
    template_image.paste(photo_image, (185, 30))  
    draw = ImageDraw.Draw(template_image)

    font_size = 30
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Font file not found at {font_path}. Using default font.")
        font = ImageFont.load_default()
    draw.text((70, 160), name, font=font, fill=(0, 0, 0)) 
    return template_image

c = canvas.Canvas(output_pdf_path, pagesize=(ID_WIDTH, ID_HEIGHT))

with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        photo_filename = os.path.basename(row['Location']) 
        photo_path = f'Images/{photo_filename}' 
        id_image = draw_id_card(template_path, photo_path, row['Name'], row['Title'])
        id_image_path = f'Images/{row["ID"]}_id_card.png'
        id_image.save(id_image_path)
        c.drawImage(id_image_path, 0, 0, width=ID_WIDTH, height=ID_HEIGHT)
        c.showPage()

c.save()
