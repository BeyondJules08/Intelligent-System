import cv2
import numpy as np
from tensorflow.keras.models import load_model
import serial
import time
import pyttsx3

engine = pyttsx3.init(driverName='espeak')

try:
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)
    time.sleep(2)
    print("Connected to Arduino")
except:
    print("Arduino not found - running in simulation mode")
    arduino = None

np.set_printoptions(suppress=True)
model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

cap = cv2.VideoCapture(0)

print("Starting Camera...")

while True:
    ret, image = cap.read()
    if not ret:
        break

    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    image_input = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)

    image_input = (image_input / 127.5) - 1

    prediction = model.predict(image_input, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    clean_text = class_name[2:].strip()

    if confidence_score > 0.90:
        print(f"Detected: {clean_text} ({confidence_score*100:.2f}%)")

        cv2.putText(image, clean_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2, cv2.LINE_AA)
        if arduino:
            arduino.write((clean_text + '\n').encode())
            engine.say(clean_text)
            engine.runAndWait()
    cv2.imshow("LSM Translator", image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()