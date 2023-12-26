# Задание №8
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.


from flask import Flask, render_template, redirect, url_for
from models import db, User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = b'6d172fcc5b984575b8535562699f4f8f979e041a1089ca0a547295524ac8e1be'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
db.init_app(app)


@app.route('/')
def index():
    return render_template('registration.html')


@app.post('/register/')
@csrf.exempt
def register():
    form = RegistrationForm()

    name = form.name.data
    last_name = form.last_name.data
    email = form.email.data
    password = generate_password_hash(form.password.data)

    user = User(name=name, last_name=last_name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login_success', name=name))


@app.route('/success/<name>')
def login_success(name: str):
    return render_template('greeting.html', context=name)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created DB!')


if __name__ == '__main__':
    app.run(debug=True)
