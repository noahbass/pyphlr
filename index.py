from flask import Flask, render_template, Response, send_file
from PIL import Image, ImageDraw
from io import BytesIO
import os


app = Flask(__name__)

if 'ON_HEROKU' in os.environ:
    app.debug = False
    app.config['hash'] = os.environ['hash_short']
else:
    app.debug = True
    from subprocess import check_output
    app.config['hash'] = check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<width>x<height>/')
@app.route('/<width>x<height>')
@app.route('/<width>/')
@app.route('/<width>')
def generate_image(width, height='None'):
    width = int(width)

    if height == 'None':
        height = width
    else:
        height = int(height)

    size = (width, height)             # size of the image to create
    im = Image.new('RGB', size) # create the image
    draw = ImageDraw.Draw(im)

    del draw

    img = BytesIO()
    im.save(img, 'PNG')
    img.seek(0)

    return send_file(img, mimetype='image/png')


@app.route('/<width>x<height>/svg/')
@app.route('/<width>x<height>/svg')
@app.route('/<width>x<height>/svg/<color>/')
@app.route('/<width>x<height>/svg/<color>')
def show_svg(width, height, color='None'):
    return Response(
        render_template('svg.svg', width=width, height=height, color=color),
        mimetype='image/svg+xml'
    )


if __name__ == '__main__':
    app.debug = False
    app.run(host = 'localhost', port = 5000)
