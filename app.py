import os
from flask import Flask
from flask_bootstrap import Bootstrap
from routes import init_routes


# Create Flask Server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
bootstrap = Bootstrap(app)

# Create upload folder for images
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'character_images')

# Passes flask app to routes file
init_routes(app)

# Makes sure only app.py runs
if __name__ == '__main__':
    app.run(debug=True)