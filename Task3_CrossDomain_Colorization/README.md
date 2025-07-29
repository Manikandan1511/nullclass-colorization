# 🎨 Task 3: Cross-Domain Image Colorization with GUI

This project is part of the NULLCLASS internship and focuses on **Cross-Domain Image Colorization** using deep learning. The application enables users to upload grayscale images and view their colorized versions using a pre-trained model—all within an intuitive GUI.


## 🚀 Project Overview

Cross-domain colorization means applying a model trained on one type of data (like natural images) to colorize images from **different or unseen domains**, such as sketches, old photos, or medical images. This task focuses on demonstrating generalization capability of the model via a user-friendly GUI.


## 🧠 Technologies Used

- Python 3.9
- TensorFlow / Keras
- OpenCV
- Pillow (PIL)
- Tkinter
- Matplotlib


## 🗂️ Folder Structure
```
Task3_CrossDomain_Colorization/
├── gui/
│ └── cross_domain_gui.py # Main GUI code
├── model/
│ └── colorization_model.h5 # Pre-trained model
├── sample_inputs/
│ └── image1.jpg # Grayscale sample inputs
├── outputs/
│ └── colorized_output.jpg # Saved outputs
├── requirements.txt # Dependency list
└── README.md # Project documentation
```

## 🎯 Key Features

- Upload grayscale `.jpg` image from any domain
- Automatic colorization using a deep learning model
- Display the output image inside the GUI
- Save the colorized image
- Stop button to cancel the process


## ⚙️ How to Run

### Step 1: Clone the Repository

git clone https://github.com/Manikandan1511/nullclass-colorization.git
cd nullclass-colorization/Task3_CrossDomain_Colorization

### Step 2: Create Virtual Environment

python3 -m venv .venv
source .venv/bin/activate      # On Mac/Linux
.venv\Scripts\activate       # On Windows

### Step 3: Install Dependencies

pip install -r requirements.txt

### Step 4: Launch GUI

python gui/cross_domain_gui.py

## 📸 Sample Run

Click Select Image → choose a .jpg grayscale image from sample_inputs/

Click Colorize → view the output inside the GUI

Click Save Output to export the result

Use Stop to cancel any ongoing process

## 🧪 Model Info

Dataset Used: BSD300

Model Type: CNN-based encoder-decoder

Color Space: LAB (for better luminance-color separation)

Format: .h5 (Keras-compatible)

## ✅ Internship Milestone

[✔️] Task 1: Basic Image Colorization

[✔️] Task 2: Real-Time Video Colorization with GUI

[✔️] Task 3: Cross-Domain Image Colorization with GUI ✅

## ✍️ Author
Manikandan S
