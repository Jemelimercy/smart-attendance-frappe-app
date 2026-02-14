import cv2
import mediapipe as mp
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

# This tells Python to look in the current folder for the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Now check if it loaded
print(f"DEBUG: API_KEY is {os.getenv('FRA_API_KEY')}")

# Load the variables from .env
load_dotenv()

# Use them in your code
BASE_URL = f"http://{os.getenv('FRA_IP')}:8000"
API_KEY = os.getenv('FRA_API_KEY')
API_SECRET = os.getenv('FRA_API_SECRET')

if not API_KEY or not API_SECRET or "None" in BASE_URL:
    print("❌ Critical Error: .env variables not loaded! Check your .env file.")
    exit()

mp_face = mp.solutions.face_detection
cap = cv2.VideoCapture(0)  # Use the first webcam

print("AI Camera Started. Looking for faces...")

with mp_face.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success: continue

        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.detections:
            print("Face Detected! Sending log...")
            headers = {"Authorization": f"token {API_KEY}:{API_SECRET}"}
            
            # fiiling fields according to the doctype in ERPNext
            payload = {
                "employee_name": "Jemeli",
                "confidence": 99.0,
                "timestamp": str(datetime.now())
            }
            try:
                r = requests.post(f"{BASE_URL}/api/resource/Warehouse Attendance", headers=headers, json=payload)
                print(f"Logged! Status: {r.status_code}")
                cv2.waitKey(5000) # Wait 5 seconds so it doesn't log too fast
            except Exception as e:
                print(f"Error: {e}")

        cv2.imshow('Warehouse AI', image)
        if cv2.waitKey(5) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()