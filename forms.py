from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class ArticleForm(FlaskForm):
    title = StringField('Название статьи')
    body = StringField('Содержание')
    category_id = IntegerField('ID категории')
    author_id = IntegerField('ID автора')
