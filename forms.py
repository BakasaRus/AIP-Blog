from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional, Email, EqualTo
from wtforms.widgets import TextArea, TextInput, PasswordInput


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()])
    body = StringField('Содержание', validators=[DataRequired()], widget=TextArea())
    category_id = IntegerField('ID категории', validators=[Optional()], widget=TextInput('number'))
    author_id = IntegerField('ID автора', validators=[Optional()], widget=TextInput('number'))


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Видимое имя на сайте', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    password_confirmation = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')], widget=PasswordInput())
