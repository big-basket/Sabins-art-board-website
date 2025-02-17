from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from models.art_models import db
from routes.upload_route import upload_file 

# Initializing flask app    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER_IMAGES'] = 'uploads/images/'  
app.config['UPLOAD_FOLDER_MARKDOWN'] = 'uploads/markdown/'  
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'md'}

os.makedirs(app.config['UPLOAD_FOLDER_IMAGES'], exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER_MARKDOWN'], exist_ok=True)

db.init_app(app)

with app.app_context():
    db.create_all() 

# Registering routes
app.register_blueprint(upload_file, url_prefix='/api')

# Running app
if __name__ == '__main__':
    app.run(debug=True)
