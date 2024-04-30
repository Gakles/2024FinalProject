import tkinter as tk
from tkinter import filedialog
import shutil
import os
import subprocess
from PIL import Image

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
            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
            print("File uploaded successfully!")
            # Run inference.py
            subprocess.run(["python", "inference.py"])
            # Clear the contents of the submitted_image folder
            for file in os.listdir(destination_folder):
                file_path = os.path.join(destination_folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)

# Create the main window
root = tk.Tk()
root.title("Hummingbird Finder")
root.geometry("400x400")

# Set background color
root.configure(bg="#c0c0c0")

# Label with instructions
label = tk.Label(root, text="Please submit an image of a hummingbird", bg="#c0c0c0")
label.pack(pady=20)

# Create a button to upload a file
upload_button = tk.Button(root, text="Upload File", command=upload_file, bg="#6495ED", fg="white")
upload_button.pack(pady=20)

# Run the application
root.mainloop()
