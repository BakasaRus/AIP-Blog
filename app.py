from flask import Flask, render_template, abort, request
from articles import articles, find_by_text

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', header='Последние статьи', articles=articles)


@app.route('/articles/<int:article_id>')
def get_article(article_id):
    try:
        return render_template('article.html', article=articles[article_id])
    except KeyError:
        abort(404)


@app.route('/search')
def search():
    text = request.args['text']
    return render_template('index.html', header=f'Поиск по слову "{text}"', articles=find_by_text(text))


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
