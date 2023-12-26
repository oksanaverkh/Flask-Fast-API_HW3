# Задание №7
# Создайте форму регистрации пользователей в приложении Flask. Форма должна
# содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
# формы данные должны валидироваться на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from forms_task2 import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = b'6d172fcc5b984575b8535562699f4f8f979e041a1089ca0a547295524ac8e1be'
csrf = CSRFProtect(app)

REQUIRED_SYMBOLS = [chr(i) for i in range(ord('a'), ord('z'))] + \
    [chr(i) for i in range(ord('A'), ord('Z'))] + \
    [chr(i) for i in range(ord('а'), ord('я'))] + \
    [chr(i) for i in range(ord('А'), ord('Я'))]

NUMBERS = [chr(i) for i in range(ord('0'), ord('9'))]


@app.route('/')
def index():
    return f'Welcome!' and redirect(url_for('register'))


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        return redirect(url_for('login_success', name=first_name))

    return render_template('register.html', form=form)


@app.route('/success/<name>')
def login_success(name: str):
    return render_template('greeting.html', context=name)


if __name__ == "__main__":
    app.run(debug=True)
