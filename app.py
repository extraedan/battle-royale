from flask import Flask, render_template
from forms import InputCharacter
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create')
def choose_characters():
    form = InputCharacter()
    return render_template("choose_characters.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)