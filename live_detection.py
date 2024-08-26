import cv2
import numpy as np
from tensorflow.keras.models import load_model

def preprocess_frame(frame):
    img_resized = cv2.resize(frame, (64, 64))  # Resize frame to match model input
    img_resized = img_resized.astype('float32') / 255.0  # Normalize the image
    img_input = np.expand_dims(img_resized, axis=0)  # Add batch dimension
    return img_input

def detect_pen_live():
    # Load the trained model
    model = load_model('model/pen_detection_model.keras')

    # Start live video capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        # Preprocess the frame
        img_input = preprocess_frame(frame)

        # Make a prediction
        prediction = model.predict(img_input)
        class_index = np.argmax(prediction)

        # Draw bounding box and label if a pen is detected
        if class_index == 1:
            cv2.rectangle(frame, (10, 10), (frame.shape[1] - 10, frame.shape[0] - 10), (0, 255, 0), 2)
            cv2.putText(frame, "Pen Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "No Pen Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Pen Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
