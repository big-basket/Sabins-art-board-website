from flask import Blueprint, send_from_directory, current_app, jsonify
import os

serve_images = Blueprint("serve_images", __name__)

@serve_images.route("/uploads/images/<filename>")
def serve_image(filename):
    # Ensure absolute path
    image_folder = os.path.abspath(current_app.config["UPLOAD_FOLDER_IMAGES"])
    full_path = os.path.join(image_folder, filename)

    print(f"Serving from: {image_folder}")
    print(f"Full file path: {full_path}")

    if not os.path.exists(full_path):
        return jsonify({"error": "File not found", "path": full_path}), 404

    return send_from_directory(image_folder, filename)
