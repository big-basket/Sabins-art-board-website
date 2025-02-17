import os
import uuid
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from backend.models.art_models import ArtPin, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
app.config['UPLOAD_FOLDER_IMAGES'] = 'uploads/images/'  
app.config['UPLOAD_FOLDER_MARKDOWN'] = 'uploads/markdown/'  
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'md'}


os.makedirs(app.config['UPLOAD_FOLDER_IMAGES'], exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER_MARKDOWN'], exist_ok=True)

db.init_app(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files or 'title' not in request.form or 'description' not in request.form:
        return jsonify({'error': 'Missing required fields'}), 400
    
    image = request.files['image']
    md_file = request.files.get('markdown')  # Markdown file is optional
    title = request.form['title']
    description = request.form['description']

    if image and allowed_file(image.filename):
        image_ext = image.filename.rsplit('.', 1)[1].lower()
        image_filename = f"{uuid.uuid4()}.{image_ext}"
        image_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], secure_filename(image_filename))
        image.save(image_path)
    else:
        return jsonify({'error': 'Invalid image file'}), 400

    md_path = None
    if md_file and allowed_file(md_file.filename):
        md_filename = f"{uuid.uuid4()}.md"
        md_path = os.path.join(app.config['UPLOAD_FOLDER_MARKDOWN'], secure_filename(md_filename))
        md_file.save(md_path)

    new_art = ArtPin(
        image_location=image_path,
        title=title,
        description=description,
        md_reference=md_path
    )
    db.session.add(new_art)
    db.session.commit()

    return jsonify({'message': 'File uploaded successfully', 'art_id': new_art.id}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
