import cv2
import numpy as np
from keras.models import load_model
from tkinter import Tk, Label, Button, Canvas, Frame
from PIL import Image, ImageTk
import time
import os
import sys

# Function to resolve path (for py2app or normal run)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # for bundled app
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load the trained model
model_path = resource_path("../model/colorization_model.h5")
model = load_model(model_path)

# GUI setup
window = Tk()
window.title("Real-Time Video Colorization")
window.geometry("900x700")
window.configure(bg='#2e2e2e')

# Frame and canvas for displaying video
video_frame = Frame(window, bg='#2e2e2e')
video_frame.pack(pady=20)
canvas = Canvas(video_frame, width=640, height=480, bg='black', highlightthickness=0)
canvas.pack()

# Global flags
running = True
cap = cv2.VideoCapture(0)
last_time = time.time()
fps_label = Label(window, text="", font=("Helvetica", 12), fg="white", bg='#2e2e2e')
fps_label.pack()

# Function to preprocess frame
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_resized = cv2.resize(gray, (128, 128)) / 255.0
    gray_resized = gray_resized.reshape(1, 128, 128, 1)
    return gray_resized

# Function to colorize frame
def colorize_frame(frame):
    input_img = preprocess_frame(frame)
    predicted_img = model.predict(input_img)[0]
    predicted_img = (predicted_img * 255).astype(np.uint8)
    predicted_img = cv2.resize(predicted_img, (frame.shape[1], frame.shape[0]))
    return predicted_img

# Function to update frames
def update_frame():
    global running, last_time

    if not running:
        return

    ret, frame = cap.read()
    if ret:
        colorized = colorize_frame(frame)
        img = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor='nw', image=imgtk)
        canvas.imgtk = imgtk

        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - last_time)
        last_time = current_time
        fps_label.config(text=f"FPS: {fps:.2f}")

    window.after(10, update_frame)

# Stop video function
def stop_video():
    global running
    running = False
    if cap:
        cap.release()
    window.destroy()

# Take screenshot
def take_screenshot():
    ret, frame = cap.read()
    if ret:
        colorized = colorize_frame(frame)
        filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, colorized)
        print(f"Screenshot saved: {filename}")

# Buttons
button_frame = Frame(window, bg='#2e2e2e')
button_frame.pack(pady=10)

stop_btn = Button(button_frame, text="Stop", font=("Helvetica", 12), command=stop_video, bg="#e74c3c", fg="white", width=10)
stop_btn.grid(row=0, column=0, padx=10)

screenshot_btn = Button(button_frame, text="Take Screenshot", font=("Helvetica", 12), command=take_screenshot, bg="#3498db", fg="white", width=15)
screenshot_btn.grid(row=0, column=1, padx=10)

# Start updating frames
update_frame()
window.mainloop()
