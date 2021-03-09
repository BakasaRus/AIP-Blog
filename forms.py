from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()])
    body = StringField('Содержание', validators=[DataRequired()])
    category_id = IntegerField('ID категории', validators=[DataRequired()])
    author_id = IntegerField('ID автора', validators=[DataRequired()])
