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

def detect_pen():
    # Load the trained model
    model = load_model('model/pen_detection_model.keras')
    
    # Get the most recent image from the dataset
    dataset_dir = os.path.join('dataset', 'pen')
    image_files = sorted(os.listdir(dataset_dir), key=lambda x: os.path.getctime(os.path.join(dataset_dir, x)), reverse=True)
    
    if not image_files:
        print("No images found in the dataset directory.")
        return

    # Path of the latest image
    latest_image_path = os.path.join(dataset_dir, image_files[0])
    
    # Preprocess the image
    img_input = preprocess_image(latest_image_path)
    
    # Make a prediction
    prediction = model.predict(img_input)
    class_index = np.argmax(prediction)

    # Load the original image for display
    original_image = cv2.imread(latest_image_path)
    display_image = cv2.resize(original_image, (512, 512))
    
    # Draw bounding box and label if a pen is detected
    if class_index == 1:
        cv2.rectangle(display_image, (10, 10), (502, 502), (0, 255, 0), 2)
        cv2.putText(display_image, "Pen Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(display_image, "No Pen Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the image
    cv2.imshow('Pen Detection', display_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_pen()
