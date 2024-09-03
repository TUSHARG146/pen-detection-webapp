import cv2
import os

def collect_data():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return jsonify({"success": False, "message": "Could not open video capture."})  # Updated for Flask return

    save_dir = 'dataset/pen'
    os.makedirs(save_dir, exist_ok=True)

    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        img_path = os.path.join(save_dir, f"pen_{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Image {count} saved at {img_path}")

        count += 1

        cv2.imshow('Data Collection - Press q to quit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return jsonify({"success": True, "message": "Data collection completed successfully."})  # Updated for Flask return