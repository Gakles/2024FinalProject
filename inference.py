import subprocess

command = "yolo task=detect mode=predict model=runs/detect/yolov8n_v8_e50b4/weights/best.pt source=submitted_image/ show=True imgsz=480 name=yolov8n_v8_e50b4 conf=0.5"
args = command.split()
subprocess.run(args)
