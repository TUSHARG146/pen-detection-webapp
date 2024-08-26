# train.py
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import warnings
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

def train_model():
    warnings.filterwarnings("ignore", category=UserWarning)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    dataset_dir = os.path.join('dataset', 'pen')
    
    def load_images():
        images = []
        labels = []

        for img_name in os.listdir(dataset_dir):
            img_path = os.path.join(dataset_dir, img_name)
            img = cv2.imread(img_path)
            
            if img is None:
                continue

            img = cv2.resize(img, (64, 64))
            images.append(img)

            if 'pen' in img_name.lower():
                labels.append(1)
            else:
                labels.append(0)

        return np.array(images), np.array(labels)

    images, labels = load_images()

    if len(images) == 0:
        print("No images found. Please check the dataset directory.")
        return

    images = images.astype('float32') / 255.0
    labels = to_categorical(labels, 2)

    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    datagen = ImageDataGenerator(rotation_range=10, zoom_range=0.1, width_shift_range=0.1, height_shift_range=0.1)
    datagen.fit(X_train)

    model = Sequential([
        Input(shape=(64, 64, 3)),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(2, activation='softmax')
    ])

    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(datagen.flow(X_train, y_train, batch_size=32), validation_data=(X_test, y_test), epochs=10)
    model.save('model/pen_detection_model.keras')

    print("Model training completed and saved.")
