import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (64, 64))
    img_resized = img_resized.astype('float32') / 255.0
    img_input = np.expand_dims(img_resized, axis=0)
    return img_input

def detect_pen(img_path):
    model = load_model('model/pen_detection_model.keras')
    
    if img_path:
        img_input = preprocess_image(img_path)
    else:
        print("No image path provided for detection.")
        return
    
    prediction = model.predict(img_input)
    class_index = np.argmax(prediction)

    original_image = cv2.imread(img_path)
    display_image = cv2.resize(original_image, (512, 512))
    
    if class_index == 1:
        cv2.rectangle(display_image, (10, 10), (502, 502), (0, 255, 0), 2)
        cv2.putText(display_image, "Pen Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(display_image, "No Pen Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Pen Detection', display_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_pen()
