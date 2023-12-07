# Задание 1. Прочитать изображение с камеры и перевести его в формат HSV.

import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('hsv_frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
