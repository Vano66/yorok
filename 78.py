from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    with open('55.html', "r", encoding="utf-8") as f:
        return f.read()


@app.route('/image_mars')
def image():
    return f'''<img src="img1/MAAARS.jpg" alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
