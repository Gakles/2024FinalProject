from ultralytics import YOLO 
import torch
def main():
    # Load the model.
    model = YOLO('yolov8n.pt')
    #model.to('cuda') will specify device per function
    #model.to('cpu')
    # Training.
    results = model.train(data='data.yaml', imgsz=480, epochs=50, batch=4, name='yolov8n_v8_e50b4', device=0)

#yolo task=detect mode=predict model=runs/detect/yolov8n_v8_e50/weights/best.pt source=inference_data/ show=True imgsz=480 name=yolov8n_v8_50e_infer480 conf=0.5


#    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
#    model.train(data='HRPlanesV2.yaml', epochs=50, workers=10)

if __name__ == '__main__':
    main()