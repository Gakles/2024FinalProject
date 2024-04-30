import subprocess

command = "yolo task=detect mode=predict model=runs/detect/yolov8n_v8_e50/weights/best.pt source=inference_data/ show=True imgsz=480 name=yolov8n_v8_50e_infer480 conf=0.1"
args = command.split()
subprocess.run(args)
