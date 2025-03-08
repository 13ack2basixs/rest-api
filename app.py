from flask import Flask
from models import db
from dotenv import load_dotenv
import os
from routes import api_bp

load_dotenv()

app = Flask(__name__)

# Connect to my Neon database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialise database and register API blueprint 
db.init_app(app)
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
