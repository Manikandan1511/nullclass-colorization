import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
from keras.models import load_model
import os

# Load the model once at the beginning
model_path = os.path.join("model", "colorization_model.h5")
model = load_model(model_path)

# Set paths
sample_input_dir = "sample_inputs"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# GUI
window = tk.Tk()
window.title("Cross-Domain Image Colorization")
window.configure(bg="#2e2e2e")

# Store image references
label_gray = tk.Label(window, bg="#2e2e2e")
label_color = tk.Label(window, bg="#2e2e2e")
label_gray.pack(pady=10)
label_color.pack(pady=10)

gray_img_display = None
color_img_display = None

def load_and_colorize():
    global gray_img_display, color_img_display

    filepath = filedialog.askopenfilename(
        initialdir=sample_input_dir,
        title="Select a Grayscale Image",
        filetypes=(("JPEG files", "*.jpg"),)
    )
    if not filepath:
        return

    # Load and preprocess grayscale image
    gray = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    gray_resized = cv2.resize(gray, (256, 256))
    gray_input = gray_resized.reshape(1, 256, 256, 1).astype('float32') / 255.0

    # Predict color image
    predicted = model.predict(gray_input)[0]
    predicted_img = (predicted * 255).astype(np.uint8)

    # Save output
    filename = os.path.basename(filepath)
    save_path = os.path.join(output_dir, f"colorized_{filename}")
    cv2.imwrite(save_path, predicted_img)

    # Display grayscale image
    gray_img_pil = Image.fromarray(gray_resized)
    gray_img_display = ImageTk.PhotoImage(gray_img_pil)
    label_gray.config(image=gray_img_display)

    # Display colorized image
    color_img_pil = Image.fromarray(predicted_img)
    color_img_display = ImageTk.PhotoImage(color_img_pil)
    label_color.config(image=color_img_display)

def stop_app():
    window.destroy()

# Buttons
btn_load = tk.Button(window, text="Load Grayscale Image", command=load_and_colorize, bg="#555", fg="white")
btn_load.pack(pady=5)

btn_stop = tk.Button(window, text="Stop", command=stop_app, bg="#555", fg="white")
btn_stop.pack(pady=5)

window.mainloop()
