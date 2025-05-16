from flask import Flask, render_template, request, flash
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

app = Flask(__name__)
app.secret_key = 'any-secret-key'

OUTPUT_FOLDER = os.path.join('static', 'output')
FONT_FOLDER = 'fonts'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def get_available_fonts():
    font_dir = FONT_FOLDER
    fonts = {}
    for file in os.listdir(font_dir):
        if file.endswith('.ttf'):
            display_name = os.path.splitext(file)[0]
            fonts[display_name] = file
    return fonts

@app.route('/', methods=['GET', 'POST'])
def index():
    wordart_path = None
    font_options = get_available_fonts()

    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        font_name = request.form.get('font')

        if text:
            try:
                selected_font_file = font_options.get(font_name, list(font_options.values())[0])
                font_path = os.path.join(FONT_FOLDER, selected_font_file)

                img = Image.new('RGB', (600, 300), color='white')
                draw = ImageDraw.Draw(img)
                
                font_size = 100
                font = ImageFont.truetype(font_path, font_size)

                while True:
                    bbox = draw.textbbox((0, 0), text, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    if text_width <= 960 or font_size <= 10:
                        break
                    font_size -= 2
                    font = ImageFont.truetype(font_path, font_size)

                x = (600 - text_width) // 2
                y = (300 - text_height) // 2

                draw.text((x, y), text, font=font, fill='black')

                filename = f"{uuid.uuid4()}.png"
                filepath = os.path.join(OUTPUT_FOLDER, filename)
                img.save(filepath)
                wordart_path = f"/static/output/{filename}"

            except Exception as e:
                flash(f"Error generating image: {e}")
        else:
            flash("Please enter some text")

    return render_template('index.html', wordart=wordart_path, font_options=font_options)

if __name__ == '__main__':
    app.run(debug=True)
