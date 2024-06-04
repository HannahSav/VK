import os
from werkzeug.utils import secure_filename
from flask import current_app

def save_media(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(current_app.config['MEDIA_FOLDER'], filename)
    file.save(file_path)
    return file_path
