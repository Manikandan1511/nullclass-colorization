# 🎨 Deep Learning-Based Image & Video Colorization System

This repository showcases a comprehensive **Image & Video Colorization** project completed as part of an internship program at **NullClass**. The project is divided into three core tasks, each targeting different aspects of image colorization using deep learning and GUI application development.

> 📘 **Note**: This project is intended purely for **educational and study purposes**.

---

## 📁 Tasks Overview

### ✅ Task 1: Basic Image Colorization

- **Objective**: Convert grayscale images to color using a trained deep learning model.
- **Model Used**: Trained on the **BSD500 dataset**.
- **Dataset**: BSD300/500 grayscale-to-color image pairs.
- **Output**: Automatically colorized versions of grayscale test images.
- **Technologies**: TensorFlow/Keras, OpenCV, NumPy, Matplotlib.

📂 Directory: `Task1_Basic_Image_Colorization`  
📄 Outputs stored in: `outputs/` folder

---

### ✅ Task 2: Real-Time Video Colorization with GUI

- **Objective**: Capture live grayscale video feed from webcam and display it colorized in real time using a GUI.
- **GUI Framework**: `Tkinter`
- **Features**:
  - Live video feed
  - Real-time frame-by-frame colorization
  - User-friendly GUI
- **Technologies**: OpenCV, Tkinter, TensorFlow/Keras, PIL

📂 Directory: `Task2_RealTime_Colorization`  
🧠 GUI script: `colorization_gui.py`

---

### ✅ Task 3: Cross-Domain Image Colorization with GUI

- **Objective**: Enable users to **upload grayscale images from various domains (nature, cartoons, objects)** and colorize them using a pre-trained model.
- **Features**:
  - Simple and interactive **GUI interface**
  - Upload images
  - Display original and colorized images side-by-side
  - Save output
  - Stop/reset feature
- **Model Used**: Custom-trained CNN on **BSD300 dataset**
- **Technologies**: OpenCV, TensorFlow/Keras, PIL, NumPy, Tkinter

📂 Directory: `Task3_CrossDomain_Colorization`  
🖼️ GUI script: `cross_domain_gui.py`  
🗂️ Sample inputs: `sample_inputs/`  
📤 Colorized outputs: `outputs/`

---

## 🛠️ Installation

1. Clone the repository:
   
   git clone https://github.com/Manikandan1511/nullclass-colorization.git
   
   cd nullclass-colorization
   
2. Create a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:

   pip install -r requirements.txt

4. Run GUI:

   For Task 2:

   python Task2_RealTime_Colorization/gui/colorization_gui.py

   For Task 3:

   python Task3_CrossDomain_Colorization/gui/cross_domain_gui.py

---

## 📦 Requirements

See requirements.txt for the full list of dependencies.

## 🎓 Purpose

This project was developed as part of the Internship Program at NullClass under the guidance of their AI team. The goal was to apply deep learning techniques to practical, real-world tasks involving image processing and user interaction via GUI.

## ✍️ Author

Manikandan S
