import os
import uuid
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from models.art_models import ArtPin, db

upload_file = Blueprint('upload_file', __name__)  # Define a Blueprint

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@upload_file.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files or 'title' not in request.form or 'description' not in request.form:
        return jsonify({'error': 'Missing required fields'}), 400
    
    image = request.files['image']
    md_file = request.files.get('markdown')  # Markdown file is optional
    title = request.form['title']
    description = request.form['description']

    if image and allowed_file(image.filename):
        image_ext = image.filename.rsplit('.', 1)[1].lower()
        image_filename = f"{uuid.uuid4()}.{image_ext}"
        image_path = os.path.join(current_app.config["UPLOAD_FOLDER_IMAGES"], secure_filename(image_filename))
        image.save(image_path)
    else:
        return jsonify({"error": "Invalid image file"}), 400

    md_path = None
    if md_file and allowed_file(md_file.filename):
        md_filename = f"{uuid.uuid4()}.md"
        md_path = os.path.join(current_app.config['UPLOAD_FOLDER_MARKDOWN'], secure_filename(md_filename))
        md_file.save(md_path)

    new_art = ArtPin(
        image_filename=image_filename,
        title=title,
        description=description,
        md_reference=md_path
    )
    db.session.add(new_art)
    db.session.commit()

    return jsonify({'message': 'File uploaded successfully', 'art_id': new_art.id}), 201
