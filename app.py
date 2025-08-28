from flask import Flask, request, jsonify, render_template
from deepface import DeepFace
import cv2
import os
import numpy as np
import base64
from datetime import datetime

app = Flask(__name__)

GUEST_FOLDER = 'static/guest'
THREATS_FOLDER = 'static/threats'
TEMP_PATH = 'static/temp/capture.jpg'

# Ensure necessary folders exist
os.makedirs(GUEST_FOLDER, exist_ok=True)
os.makedirs(THREATS_FOLDER, exist_ok=True)
os.makedirs('static/temp', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    try:
        data = request.json
        base64_img = data['image'].split(',')[1]
        img_data = base64.b64decode(base64_img)
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Save captured image
        cv2.imwrite(TEMP_PATH, img)

        # Check if a face is present in the image
        try:
            faces = DeepFace.extract_faces(img_path=TEMP_PATH, enforce_detection=True)
            if len(faces) == 0:
                raise ValueError("No face detected")
        except:
            # Save threat - no face detected
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            threat_path = os.path.join(THREATS_FOLDER, f"noface_{timestamp}.jpg")
            cv2.imwrite(threat_path, img)
            return jsonify({'match': False, 'reason': 'No face detected'})

        # Match against guest database
        matched_images = []
        matched_name = None

        for filename in os.listdir(GUEST_FOLDER):
            guest_path = os.path.join(GUEST_FOLDER, filename)
            try:
                result = DeepFace.verify(TEMP_PATH, guest_path, enforce_detection=True)
                if result['verified']:
                    matched_images.append(f"/static/guest/{filename}")
                    matched_name = filename
            except:
                continue

        if matched_images:
            return jsonify({
                'match': True,
                'name': matched_name,
                'images': matched_images
            })
        else:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            threat_path = os.path.join(THREATS_FOLDER, f"unknown_{timestamp}.jpg")
            cv2.imwrite(threat_path, img)
            return jsonify({'match': False, 'reason': 'Face not recognized'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
