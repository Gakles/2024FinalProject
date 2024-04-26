from ultralytics import YOLO 
# Load the model.
model = YOLO('yolov8n.pt')
# Training.
results = model.train(data='data.yaml', imgsz=480, epochs=10, batch=4, name='yolov8n_v8_50e')