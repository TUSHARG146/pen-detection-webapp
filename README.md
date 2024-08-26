
# Pen Detection Project

This project is a simple pen detection system built using TensorFlow and OpenCV, wrapped in a Flask web application. The system captures video input from a webcam and uses a pre-trained model to detect the presence of a pen in real-time.

## Features

- **Real-time Pen Detection:** The model detects the presence of a pen in the video feed from your webcam.
- **Flask Web Interface:** The application is served via a Flask web server, making it accessible through a web browser.
- **OpenCV Integration:** Used for handling the webcam input and displaying the output with detection results.

## Project Structure

![image](https://github.com/user-attachments/assets/6e33af26-ac73-4df1-8c9a-5b3356cecb51)


## Prerequisites
1. Python 3.7+
2. TensorFlow 2.x
3. OpenCV
4. Flask


##Installation

1. Clone the repository:

git clone https://github.com/TUSHARG146/pen-detection-webapp.git
cd pen-detection

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

pip install -r requirements.txt

## Run the application:

1. Start the application:
python app.py

2. Open a web browser and navigate to http://127.0.0.1:5000/ to view the real-time pen detection.

## Usage

- Run the application using the command python app.py.
- The web server will start, and you can access the video feed via the browser.
- The system will automatically detect a pen in the frame and highlight it with a bounding box.

## Troubleshooting

If you encounter a BadZipFile error related to the model file, you can reload and save the model again using the following script:

from tensorflow.keras.models import load_model, save_model
model = load_model('model/pen_detection_model_original.keras')
save_model(model, 'model/pen_detection_model.keras')

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

