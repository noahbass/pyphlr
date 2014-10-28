from flask import Flask, render_template, Response, json
from flask_sslify import SSLify
import png

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<width>x<height>/')
@app.route('/<width>x<height>')
def show_image(width, height):
    return width + ', ' + height


@app.route('/<width>x<height>/<svg>/')
@app.route('/<width>x<height>/<svg>')
def show_svg(width, height, svg):
    return Response(
        render_template('svg.svg', width=width, height=height),
        mimetype='image/svg+xml'
    )


@app.route('/test')
def show_test():
    content = [
        { 'param': 'foo' }
    ]

    return Response(json.dumps(content),  mimetype='image/gif')

@app.route('/png')
def show_png():
    #f = open('ramp.png', 'wb')      # binary mode is important
    #w = png.Writer(255, 1, greyscale=True)
    #w.write(f, [range(256)])
    #f.close()
#
    #return w.write(f, [range(256)])
    return Response(png.from_array([[255, 0, 0, 255], [0, 255, 255, 0]], 'L'),  mimetype='image/png')
    #return png.from_array([[255, 0, 0, 255], [0, 255, 255, 0]], 'L')


if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port = 5000)
