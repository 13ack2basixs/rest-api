from flask import Flask
from models import db

app = Flask(__name__)

# Initialise database
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
