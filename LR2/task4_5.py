import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 150, 150])
    upper_red = np.array([15, 255, 255])  # оттенок насыщенность яркость

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # применение маски на изображение
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # вычисление момента на основе маски
    moments = cv2.moments(mask)

    # поиск момента первого порядка
    area = moments['m00']

    if area > 0:
        # ширина и высота прямоугольника равны квадратному корню из площади объекта
        width = height = int(np.sqrt(area))
        # вычисление координат центра объекта на изображении с использованием момент первого порядка
        c_x = int(moments["m10"] / moments["m00"])
        c_y = int(moments["m01"] / moments["m00"])
        # отрисовка прямоугольника
        color = (0, 0, 0)  # черный цвет
        thickness = 2  # толщина
        cv2.rectangle(frame,
                      (c_x - (width // 8), c_y - (height // 8)),
                      (c_x + (width // 8), c_y + (height // 8)),
                      color, thickness)

    cv2.imshow('Result_frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

print("Площадь объекта:", area)

cap.release()
cv2.destroyAllWindows()
