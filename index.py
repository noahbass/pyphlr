from flask import Flask, render_template, Response
#from PIL import Image, ImageDraw
#import base64
#import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<width>x<height>/')
@app.route('/<width>x<height>')
def show_image(width, height):
    return width + ', ' + height


@app.route('/<width>x<height>/<svg>/')
@app.route('/<width>x<height>/<svg>')
@app.route('/<width>x<height>/<svg>/<color>/')
@app.route('/<width>x<height>/<svg>/<color>')
def show_svg(width, height, svg, color='None'):
    return Response(
        render_template('svg.svg', width=width, height=height, color=color),
        mimetype='image/svg+xml'
    )


#@app.route('/png')
#def show_png():
#    code = base64.b64encode(open('./templates/image.png', 'rb').read())
#    data = 'data:image/png;base64,'
#    #encode('ascii')
#    #img = code + data
#    return Response(
#        base64.b64encode(open('./templates/image.png', 'rb').read()),
#        mimetype='text'
#    )
#    #return Response(data, mimetype='text')
#    #, base64.b64encode(open('./image.png','rb').read())
#
#
#def generate_image(width, height):
#    width = int(width)
#    height = int(height)
#
#    size = (width, height)             # size of the image to create
#    im = Image.new('RGB', size) # create the image
#    draw = ImageDraw.Draw(im)
#
#    del draw
#
#    #return im.show('test.png')
#    #return im.show('img.png', 'PNG')
#    img = im.show('test.png')
#
#    #return img
#
#    return base64.b64encode(open(img, 'rb').read())
#
#
#@app.route('/test/<width>x<height>')
#def show_test(width, height):
#    #ed = (255,0,0)    # color of our text
#    #ext_pos = (10,10) # top-left position of our text
#    #ext = "Hello World!" # text to draw
#    # Now, we'll do the drawing:
#    #raw.text(text_pos, text, fill=red)
#    return Response(generate_image(width, height), mimetype='text')
#
#    # We need an HttpResponse object with the correct mimetype
#    #response = HttpResponse(mimetype="image/png")
#    # now, we tell the image to save as a PNG to the
#    # provided file-like object
#    #im.save(response, 'PNG')
#    #return response
#    #


if __name__ == '__main__':
    app.debug = False
    app.run(host = 'localhost', port = 5000)
