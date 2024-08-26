from flask import Flask, render_template, request, jsonify
from live_detection import detect_pen_live
import cv2
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from werkzeug.utils import secure_filename
from train import train_model

app = Flask(__name__)

# Directory for saving uploaded images
UPLOAD_FOLDER = 'dataset/pen'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"})

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"success": True, "message": "Image uploaded successfully."})

@app.route('/train', methods=['POST'])
def train():
    train_model()  # Trigger the training process
    return jsonify({"success": True, "message": "Model trained successfully."})

@app.route('/detect', methods=['POST'])
def detect():
    detect_pen_live()  # Start live detection using webcam
    return jsonify({"success": True, "message": "Real-time detection started."})

if __name__ == '__main__':
    app.run(debug=True)
