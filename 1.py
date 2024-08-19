
from ultralytics import YOLO
import cv2

# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference on the frame
    results = model(frame)
    
    # Display the annotated frame
    annotated_frame = results[0].plot()  # Draw bounding boxes, labels, etc.
    cv2.imshow('YOLOv8 Webcam', annotated_frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()