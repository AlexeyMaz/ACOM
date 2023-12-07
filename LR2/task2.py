# Задание 2. Применить фильтрацию изображения с помощью команды
# inRange и оставить только красную часть, вывести получившееся изображение
# на экран(treshold), выбрать красный объект и потестировать параметры
# фильтрации, подобрав их нужного уровня.

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 150, 150])
    upper_red = np.array([100, 255, 255])  # оттенок насыщенность яркость

    mask = cv2.inRange(hsv, lower_red, upper_red)
    onlyRed_frame = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Red Filtered Image', onlyRed_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
