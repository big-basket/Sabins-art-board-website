from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from models.art_models import db
from routes.upload_route import upload_file 
from routes.serve_images import serve_images
from routes.get_artpins import get_art_pins

# Initializing flask app    
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER_IMAGES'] = os.path.join(app.static_folder, 'uploads', 'images')
app.config['UPLOAD_FOLDER_MARKDOWN'] = os.path.join(app.static_folder, 'uploads', 'markdown')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'md'}

os.makedirs(app.config['UPLOAD_FOLDER_IMAGES'], exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER_MARKDOWN'], exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, 'database'), exist_ok=True)



db.init_app(app)

# Enabling CORS
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


with app.app_context():
    db.create_all() 

# Registering routes
app.register_blueprint(upload_file, url_prefix='/api')
app.register_blueprint(serve_images)
app.register_blueprint(get_art_pins)

# Running app
if __name__ == '__main__':
    app.run(debug=True)
