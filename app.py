from flask import Flask, render_template, abort

app = Flask(__name__)

articles = {
    1: {
        'title': 'Основы CSS для бэкенд-разработчиков',
        'body': 'Равным образом рамки и место обучения кадров позволяет оценить значение форм развития.',
        'is_new': True
    },
    2: {
        'title': 'Топ-10 CSS-фреймворков',
        'body': 'Повседневная практика показывает, что постоянное информационно-пропагандистское обеспечение нашей деятельности позволяет выполнять важные задания по разработке дальнейших направлений развития.',
        'is_new': False
    },
}


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
