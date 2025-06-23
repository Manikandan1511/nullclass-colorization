## Task 1: Basic Image Colorization - NULLCLASS Internship

##  Project Description
This project focuses on building a deep learning model using CNN to colorize grayscale images using the BSD300 dataset.

## Dataset link - https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300-images.tgz


##  Model Summary
- Input shape: (128, 128, 1)
- Output shape: (128, 128, 3)
- Loss Function: Mean Squared Error (MSE)
- Final Validation Loss: 0.0111

##  Folder Structure
Task1_Basic_Image_Colorization/
├── data/
├── colorize_bsd500.ipynb
├── preprocess_bsd500.py
├── colorization_model.h5
├── requirements.txt
├── README.md

##  How to Run
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run preprocessing:
    ```
    python preprocess_bsd500.py
    ```
3. Run training notebook: `colorize_bsd500.ipynb`

## 📊 Performance
- Final Val Loss: `0.0111`
- Generated images visually match original colors with minor blurring.

##  Author
- Manikandan S