import cv2
import numpy as np
import time
def detect_heart_rate():
    # Load the video
    cap = cv2.VideoCapture("C:\\Users\\Ayan\Downloads\\video-48320.mp4")

    # Variables initialization
    start_time = time.time()
    frame_count = 0
    heart_rate = 0

    # Loop over frames
    while True:
        # Read the frame
        ret, frame = cap.read()

        # Break the loop if the video is finished
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw bounding boxes around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Heart Rate Detection', frame)

        # Calculate heart rate
        elapsed_time = time.time() - start_time
        frame_count += 1
        if elapsed_time > 5:  # Update the heart rate every 5 seconds
            heart_rate = int(frame_count / elapsed_time * 60)
            start_time = time.time()
            frame_count = 0
            print('Heart Rate:', heart_rate)

        # Quit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()
