from ultralytics import YOLO 
# Load the model.
model = YOLO('yolov8n.pt')
# Training.
results = model.train(data='hummingbirds.yaml', imgsz=480, epochs=50, batch=8, name='yolov8n_v8_50e')