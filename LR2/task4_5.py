import random

import cv2
import numpy as np

cap = cv2.VideoCapture(1)
color_1 = 0
color_2 = 0
color_3 = 0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # определение диапазона красного цвета в HSV
    lower_red = np.array([0, 150, 150])
    upper_red = np.array([100, 255, 255])  # оттенок насыщенность яркость

    # Маска - бинарное изображение, где пиксели, соответствующие заданному диапазону цвета, имеют значение 255 (белый), а остальные пиксели имеют значение 0 (черный).
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
        color_1 = random.randint(0, 255)
        color_2 = random.randint(0, 255)
        color_3 = random.randint(0, 255)
        thickness = 2  # толщина
        print(width)
        c = 5
        cv2.rectangle(frame,
                      (c_x - (width // c), c_y - (height // c)),
                      (c_x + (width // c), c_y + (height // c)),
                      color, thickness)

        a = 7
        b = 1000
        cv2.rectangle(frame,
                      (c_x - (b // 256) - a, c_y - (b // 256)),
                      (c_x + (b // 256) - a, c_y + (b // 256)),
                      (color_1, color_2, color_3), -1)
        cv2.rectangle(frame,
                      (c_x - (b // 256) + a, c_y - (b // 256)),
                      (c_x + (b // 256) + a, c_y + (b // 256)),
                      (color_1, color_2, color_3), -1)
        cv2.rectangle(frame,
                      (c_x - (b // 256), c_y - (b // 256) - a),
                      (c_x + (b // 256), c_y + (b // 256) - a),
                      (color_1, color_2, color_3), -1)
        cv2.rectangle(frame,
                      (c_x - (b // 256), c_y - (b // 256) + a),
                      (c_x + (b // 256), c_y + (b // 256) + a),
                      (color_1, color_2, color_3), -1)

    # cv2.imshow('HSV_frame', hsv)
    cv2.imshow('Result_frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

print("Площадь объекта:", area)

cap.release()
cv2.destroyAllWindows()
