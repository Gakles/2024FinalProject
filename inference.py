import subprocess

command = "yolo task=detect mode=predict model=runs/detect/yolov8n_v8_e300b163/weights/best.pt source=inference_data/ show=True imgsz=480 name=yolov8n_v8_e50b4 conf=0.5"
args = command.split()
subprocess.run(args)
