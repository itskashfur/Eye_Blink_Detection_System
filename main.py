import cv2
import numpy as np
import dlib
from math import hypot

# Initialize video capture
cap = cv2.VideoCapture(0)

# Load the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Ensure the path is correct

# Function to calculate midpoint
def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

# Font for displaying text
font = cv2.FONT_HERSHEY_PLAIN

# Function to get the blinking ratio
def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_length / ver_line_length
    return ratio

# Initialize blink counter and frame counter for state management
blink_count = 0
blink_detected = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the gray frame
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        # Calculate blinking ratio for both eyes
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # Detect blink
        if blinking_ratio > 5.7:
            if not blink_detected:
                blink_count += 1
                blink_detected = True
        else:
            blink_detected = False

        # Display blink count on the frame
        cv2.putText(frame, f"Blink Count: {blink_count}", (50, 100), font, 2, (255, 0, 0), 2)

        # Optional: Display BLINKING text if a blink is detected
        if blinking_ratio > 5.7:
            cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0), 2)

   # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Exit on 'q' key
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()