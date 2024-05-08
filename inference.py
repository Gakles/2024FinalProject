import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python inference.py <chosen_model_folder>")
    sys.exit(1)

chosen_model = sys.argv[1]
command = f"yolo task=detect mode=predict model=runs/detect/{chosen_model}/weights/best.pt source=submitted_image/ show=True imgsz=480 name=inference/outputs conf=0.5"
args = command.split()
subprocess.run(args)

#yolo task=detect mode=predict model=runs/detect/yolo8m_e600_b8/weights/best.pt source=inference_data/ show=True imgsz=480 name=inference/outputs conf=0.5
