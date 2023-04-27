import cv2


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, frame = cap.read()
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # If the q-key is pressed
        break