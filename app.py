from flask import Flask, render_template

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
    return render_template('article.html', article=articles[article_id])


if __name__ == '__main__':
    app.run()
