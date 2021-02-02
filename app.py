from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/articles/<int:article_id>')
def get_article(article_id):
    return str(article_id)


if __name__ == '__main__':
    app.run()
