import cv2
import os
import time
import uuid


labels = ['thumbs_up', 'thumbs_down', 'hello', 'fingers_crossed']
number_of_images = 6
camera_id = 0

image_path = os.path.join('images', 'grabbed')

# Check and create a folder if needed
if not os.path.exists(image_path):
    if os.name == 'posix':   # Mac, Linux
        os.system(f'mkdir -p {image_path}')
    elif os.name == 'nt':  # Windows
        os.system(f'mkdir {image_path}')

# Create a folder for each gesture
for label in labels:
    path = os.path.join(image_path, label)
    if not os.path.exists(path):
        os.system(f'mkdir {path}')


cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)

if not cap.isOpened():
    print('Cannot open camera')
    exit()

for label in labels:
    print(f'Collecting images for label {label}')
    time.sleep(5)

    run = True

    for img_num in range(number_of_images):
        print(f'\tCapture image {img_num+1}')

        _, image = cap.read()

        image_name = os.path.join(image_path, label, f'{label}-{uuid.uuid1()}.jpg')
        cv2.imwrite(image_name, image)
        cv2.imshow('Grabbed Image', image)

        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'): # If the q-key is pressed
            run = False
            break
    if not run:
        break

cap.release()
cv2.destroyAllWindows()

