from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from instance.models import db, User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '142bab312b10c9eddeed3f4646a959ac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstdatabase.db'
csrf = CSRFProtect(app)

db.init_app(app)


@app.route('/')
def index():
    context = {'title': 'Главная страница'}
    return render_template('main.html', **context)


@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
    print('OK')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        name = form.name.data
        surname = form.surname.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        user = User(name=name, surname=surname, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
