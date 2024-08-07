from ultralytics import YOLO
import cv2
import cvzone
import math
import time

#cap = cv2.VideoCapture(0)
path = 'IMG_1599.mp4'
cap = cv2.VideoCapture(path)
cap.set(3, 640)
cap.set(4, 480)
model_path = 'train_model_863+51photo_yolos_448_v1.1.pt'
model = YOLO(model_path)

classNames = ['car', 'armor', 'mobic', 'smoke', 'build']

while True:
    success, img = cap.read()
    if not success:
        print("Помилка при читанні з відеопристрою.")
        break
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = math.ceil((box.conf[0] * 100)) / 100

            if conf > 0.55:
                cvzone.cornerRect(img, (x1, y1, w, h))

                cls = int(box.cls[0])
                if cls < len(classNames):
                    cvzone.putTextRect(img, f"{classNames[cls]} {conf}", (max(0, x1), max(0, y1 - 20)))

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
