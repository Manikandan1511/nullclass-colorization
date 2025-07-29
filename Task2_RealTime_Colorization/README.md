# Real-Time Video Colorization with Deep Learning

This project uses a trained deep learning model to colorize live grayscale video from your webcam in real-time. The GUI is built using Tkinter and OpenCV and offers a simple interface to visualize, capture, and interact with the colorized output.

---

## Project Structure
```
Task2_RealTime_Colorization/
├── model/
│ └── colorization_model.h5 # Trained deep learning model
├── gui/
│ ├── colorization_gui.py # Main GUI application script
│ ├── launch_colorization_gui.command # Double-clickable launcher for Mac
│ └── .venv/ # Virtual environment (local to GUI)
```

## How to Run the Application

### Mac Users (Recommended)

> Double-click the `launch_colorization_gui.command` file to start the application.

If double-click doesn't work, make it executable:

chmod +x launch_colorization_gui.command
🛠️ Manual Execution via Terminal
bash
Copy
Edit
cd gui
source .venv/bin/activate
python3 colorization_gui.py

#### 🧠 Features
📹 Real-time webcam capture and colorization.

🖼️ Option to take screenshots of colorized frames.

📊 Displays real-time FPS (Frames Per Second).

💻 Clean GUI using Tkinter and PIL.

##### 💡 Requirements
This project uses a local virtual environment (.venv) with all dependencies pre-installed.

If you're setting up manually, install these:

bash
Copy
Edit
pip install tensorflow keras opencv-python pillow

🧠 Model Information
Model format: .h5 (Keras)

Input: Grayscale image (128x128)

Output: Colorized RGB image

Trained on: BSD500 Dataset

📸 Screenshots
Grayscale Input	Colorized Output
(from webcam)	(predicted live)

🛠️ Developer
Name: Manikandan

📃 License
This project is for educational and internship purposes under the NULLCLASS Internship Program.
