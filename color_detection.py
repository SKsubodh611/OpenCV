import cv2
import numpy as np

# Function to detect a specific color
def detect_color(frame, lower_bound, upper_bound):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return mask, result

# Define color ranges (HSV format)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened
if not cap.isOpened():
    print("Error: Camera not found!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from camera!")
        break

    # Detect red color
    mask, result = detect_color(frame, lower_red, upper_red)

    # Show the original, mask, and result
    cv2.imshow("Original", frame)
    cv2.imshow("Red Mask", mask)
    cv2.imshow("Detected Red", result)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
