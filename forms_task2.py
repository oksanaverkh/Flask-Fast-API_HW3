from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

REQUIRED_SYMBOLS = [chr(i) for i in range(ord('a'), ord('z'))] + \
    [chr(i) for i in range(ord('A'), ord('Z'))] + \
    [chr(i) for i in range(ord('а'), ord('я'))] + \
    [chr(i) for i in range(ord('А'), ord('Я'))]

NUMBERS = [chr(i) for i in range(ord('0'), ord('9'))]


class RegistrationForm(FlaskForm):
    first_name = StringField(
        'Name', validators=[DataRequired(message='Введите имя!')])
    last_name = StringField('Last name', validators=[
                            DataRequired(message='Введите фамилию!')])
    email = StringField('Email', validators=[
                        DataRequired(), Email(message='Некорректный формат email!')])
    password = PasswordField('Password', validators=[
                             DataRequired('Пароль не введен!'), Length(min=8, message='Недостаточная длина пароля!')])

    def validate_password(form, field):
        message = 'Поле пароль должно содержать хотя бы одну букву и одну цифру!'
        count = 0
        for symbol in REQUIRED_SYMBOLS:
            if symbol in field.data:
                count += 1
                break
        for symbol in NUMBERS:
            if symbol in field.data:
                count += 1
                break
        if count < 2:
            raise ValidationError(message)

    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password', message='Пароли не совпадают!')])
