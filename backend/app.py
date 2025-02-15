from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from models.art_models import db

# Initializing flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_pins.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all() 

    
# Running app
if __name__ == '__main__':
    app.run(debug=True)
