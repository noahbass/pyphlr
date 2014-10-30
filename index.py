from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<width>x<height>/<svg>/')
@app.route('/<width>x<height>/<svg>')
@app.route('/<width>x<height>/<svg>/<color>/')
@app.route('/<width>x<height>/<svg>/<color>')
def show_svg(width, height, svg, color='None'):
    return Response(
        render_template('svg.svg', width=width, height=height, color=color),
        mimetype='image/svg+xml'
    )


if __name__ == '__main__':
    app.debug = False
    app.run(host = 'localhost', port = 5000)
