#Ignore this file

from flask import Flask, request, jsonify
import yolo8  # import your YOLOv8 module

app = Flask(__name__)
yolo_model = yolo8.load_model()  # Load your YOLOv8 model

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image']
    # Process the image using your YOLOv8 model
    annotated_image = yolo8.detect_objects(image, yolo_model)

    return jsonify({'annotated_image': annotated_image})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
