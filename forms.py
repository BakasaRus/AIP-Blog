from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, Email, EqualTo
from wtforms.widgets import TextArea, TextInput, PasswordInput, CheckboxInput


class ArticleForm(FlaskForm):
    title = StringField('Название статьи', validators=[DataRequired()])
    body = StringField('Содержание', validators=[DataRequired()], widget=TextArea())
    category_id = IntegerField('ID категории', validators=[Optional()], widget=TextInput('number'))


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    remember_me = BooleanField('Запомнить меня', widget=CheckboxInput())


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Видимое имя на сайте', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    password_confirmation = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')], widget=PasswordInput())
