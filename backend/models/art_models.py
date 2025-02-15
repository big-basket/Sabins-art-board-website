from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ArtPin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_location = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    md_reference = db.Column(db.String(255), nullable=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())