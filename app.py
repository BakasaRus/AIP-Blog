from flask import Flask, render_template, abort
from articles import articles

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title='Just Another Blog', articles=articles)


@app.route('/articles/<int:article_id>')
def get_article(article_id):
    try:
        return render_template('article.html', article=articles[article_id])
    except KeyError:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
