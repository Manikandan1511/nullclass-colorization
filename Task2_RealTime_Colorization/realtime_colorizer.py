import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('/Users/manikandan/Desktop/nullclass_colorization_backup/Task1_Basic_Image_Colorization/model/colorization_model.h5')

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize and convert to grayscale
    img = cv2.resize(frame, (128, 128))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Normalize and reshape for model: (1, 128, 128, 1)
    input_img = gray / 255.0
    input_img = np.expand_dims(input_img, axis=0)
    input_img = np.expand_dims(input_img, axis=-1)

    # Predict
    predicted_img = model.predict(input_img)
    predicted_img = np.squeeze(predicted_img) * 255
    predicted_img = predicted_img.astype(np.uint8)

    # Convert grayscale back to 3-channels for display only
    gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Resize and show
    combined = np.hstack((cv2.resize(gray_3ch, (256, 256)), cv2.resize(predicted_img, (256, 256))))
    cv2.imshow("Grayscale vs Colorized", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
