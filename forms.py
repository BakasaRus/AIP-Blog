from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea, TextInput


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()])
    body = StringField('Содержание', validators=[DataRequired()], widget=TextArea())
    category_id = IntegerField('ID категории', validators=[Optional()], widget=TextInput('number'))
    author_id = IntegerField('ID автора', validators=[Optional()], widget=TextInput('number'))
