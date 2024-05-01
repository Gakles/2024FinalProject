# 2024FinalProject
My final project
Ideal setup: 
    pip install everything in ultralyics_requirements.txt, pip install ultralytics

How to do a hummingbird check:
You can either:
    1 - Add images that you want to inference check to the inference_data folder and then run in command line the commented out line at the bottom of inference.py 
    This is currently set to run the on a yolo8m model trained on 400 images
    2 - Run upload.py and select a model and an image to check. The models are currently poorly named but I'd recommend ones with v8m or e300b4 in the name. 
    For both, results with appear in runs/detect/inference/