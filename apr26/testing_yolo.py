import cv2
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

model = YOLO('yolov8l.pt')

while True:
    _, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.predict(img, conf=0.5, verbose=False)

    for result in results:
        annotator = Annotator(frame)
        boxes = result.boxes
        for box in boxes:
            b = box.xyxy[0]
            c = box.cls
            annotator.box_label(b, model.names[int(c)], color=[0, 123, 255])
    frame = annotator.result()
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()