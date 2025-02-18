from models.art_models import ArtPin
from flask import Blueprint, send_from_directory, current_app, jsonify, request, url_for


get_art_pins = Blueprint("get_art_pins", __name__)  

@get_art_pins.route("/api/artpins", methods=["GET"])
def fetch_art_pins():
    art_pins = ArtPin.query.all()
    
    pins_list = [
        {
            "id": pin.id,
            "image_filename": f"{request.host_url}uploads/images/{pin.image_filename}"
            if not pin.image_filename.startswith("http") else pin.image_filename,
            "title": pin.title,
            "description": pin.description,
            "md_reference": pin.md_reference,
            "date_created": pin.date_created
        }
        for pin in art_pins
    ]
    return jsonify(pins_list)