import os
import uuid
import requests
from flask import Flask
from models.art_models import ArtPin, db

# Initialize Flask app context 
app = Flask(__name__)
app.config['UPLOAD_FOLDER_IMAGES'] = "backend/uploads/images"
app.config['UPLOAD_FOLDER_MARKDOWN'] = "backend/uploads/markdown"
os.makedirs(app.config['UPLOAD_FOLDER_IMAGES'], exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER_MARKDOWN'], exist_ok=True)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'database.db')}"
os.makedirs(os.path.join(BASE_DIR, 'database'), exist_ok=True)

db.init_app(app)

# Sample data 
art_data = [
    {
        "image_url": "https://i.pinimg.com/736x/97/68/45/976845ee7cc001720e9ad68eaab4f2a8.jpg",
        "title": "Sunset Over the Ocean",
        "description": "A beautiful painting of a sunset over the sea.",
        "md_content": "# Sunset\nThis painting captures the beauty of a sunset over the ocean."
    },
    {
        "image_url": "https://i.pinimg.com/736x/12/9c/f4/129cf464f43f242801bf746de3a78a48.jpg",
        "title": "Mountain Peaks",
        "description": "Snowy mountain peaks under a starry sky.",
        "md_content": "# Mountains\nThe grandeur of nature is evident in this piece."
    }
]

def download_image(image_url, save_folder):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        ext = image_url.split('.')[-1].split('?')[0]  # Extract file extension
        filename = f"{uuid.uuid4()}.{ext}"
        image_path = os.path.join(save_folder, filename)

        with open(image_path, "wb") as img_file:
            for chunk in response.iter_content(1024):
                img_file.write(chunk)

        return image_path
    return None

def save_markdown(content, save_folder):
    filename = f"{uuid.uuid4()}.md"
    md_path = os.path.join(save_folder, filename)

    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(content)

    return md_path

def seed_database():
    with app.app_context():
        db.create_all()  

        for art in art_data:
            image_path = download_image(art["image_url"], app.config['UPLOAD_FOLDER_IMAGES'])
            md_path = save_markdown(art["md_content"], app.config['UPLOAD_FOLDER_MARKDOWN'])

            if image_path:
                new_art = ArtPin(
                    image_location=image_path,
                    title=art["title"],
                    description=art["description"],
                    md_reference=md_path
                )
                db.session.add(new_art)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
