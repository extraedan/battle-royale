from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Today you will participate in a Battle Royale"

if __name__ == '__main__':
    app.run(debug=True)