from ultralytics import YOLO 
# Load the model.
model = YOLO('yolov8n.pt')
# Training.

	
results = model.train(data='data.yaml', imgsz=480, epochs=10, batch=4, name='yolov8n_v8_50e')

#yolo task=detect mode=predict model=runs/detect/yolov8n_v8_50e5/weights/best.pt source=inference_data/testbird.png show=True imgsz=480 name=yolov8n_v8_50e_infer480 conf=0.05
