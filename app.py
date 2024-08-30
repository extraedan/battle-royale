from flask import Flask, render_template
from sqlalchemy.orm import DeclarativeBase

from forms import InputCharacter
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# cCREATE FLASK SERVEr
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
bootstrap = Bootstrap5(app)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///battle_royale.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create')
def choose_characters():
    form = InputCharacter()
    return render_template("choose_characters.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)