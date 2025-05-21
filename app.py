from flask import Flask, render_template, request, flash
from PIL import Image, ImageDraw, ImageFont
import os
import uuid
import base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'any-secret-key'

FONT_FOLDER = 'fonts'
os.makedirs(FONT_FOLDER, exist_ok=True)

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
    wordart_data_uri = None
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

                    if text_width <= 560 or font_size <= 10:
                        break
                    font_size -= 2
                    font = ImageFont.truetype(font_path, font_size)

                x = (600 - text_width) // 2
                y = (300 - text_height) // 2

                draw.text((x, y), text, font=font, fill='black')

                img_io = BytesIO()
                img.save(img_io, format='PNG')
                img_io.seek(0)
                img_base64 = base64.b64encode(img_io.read()).decode('utf-8')
                wordart_data_uri = f"data:image/png;base64,{img_base64}"

            except Exception as e:
                flash(f"Error generating image: {e}")
        else:
            flash("Please enter some text")

    return render_template('index.html', wordart=wordart_data_uri, font_options=font_options)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2000)
