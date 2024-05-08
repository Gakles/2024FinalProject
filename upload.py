import tkinter as tk
from tkinter import filedialog
import shutil
import os
import subprocess
from PIL import Image

#Code generated or inspired by ChatGPT 3.5

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Open the image file
        with Image.open(file_path) as img:
            # Resize the image to 480x480
            img = img.resize((480, 480))
            # Specify the directory where you want to move the file
            destination_folder = "submitted_image"
            # Create the directory if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            # Copy the file to the destination folder
            shutil.copy(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
            print("File uploaded successfully!")
            # Run inference.py

            chosen_model = chosen_model_var.get()
            #subprocess.run(["python", "inference.py", chosen_model])
            command = f"yolo task=detect mode=predict model=runs/detect/{chosen_model}/weights/best.pt source=submitted_image/ show=True imgsz=480 name=inference/outputs conf=0.5"
            args = command.split()
            subprocess.run(args)

            # Clear the contents of the submitted_image folder
            for file in os.listdir(destination_folder):
                file_path = os.path.join(destination_folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)

# Function to get list of model names from the directory
def get_models():
    model_dir = "runs/detect"
    models = []
    for item in os.listdir(model_dir):
        if os.path.isdir(os.path.join(model_dir, item)) and item != "inference":
            models.append(item)
    return models

# Create the main window
root = tk.Tk()
root.title("Hummingbird Finder")
root.geometry("400x400")

# Set background color
root.configure(bg="#c0c0c0")

# Label for model choice
model_label = tk.Label(root, text="Choose which model to run:", bg="#c0c0c0")
model_label.pack(pady=5)

# Dropdown menu for choosing model
models = get_models()
chosen_model_var = tk.StringVar(root)
chosen_model_var.set(models[0])  # Set default value
model_menu = tk.OptionMenu(root, chosen_model_var, *models)
model_menu.config(width=30)  # Adjust the width of the dropdown menu
model_menu.pack(pady=10)

# Label for the model dropdown
label = tk.Label(root, text="Please submit an image of a hummingbird", bg="#c0c0c0")
label.pack(pady=5)

# Create a button to upload a file
upload_button = tk.Button(root, text="Upload File", command=upload_file, bg="#6495ED", fg="white")
upload_button.pack(pady=5)

# Run the application
root.mainloop()
