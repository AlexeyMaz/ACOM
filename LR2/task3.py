# Задание 3. Провести морфологические преобразования (открытие и
# закрытие) фильтрованного изображения, вывести результаты на экран,
# посмотреть смысл подобного применения операций erode и dilate.

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 150, 150])
    upper_red = np.array([15, 255, 255])  # оттенок насыщенность яркость

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


def erode(image, kernel):
    m, n = image.shape
    km, kn = kernel.shape
    hkm = km // 2
    hkn = kn // 2
    eroded = np.copy(image)

    for i in range(hkm, m - hkm):
        for j in range(hkn, n - hkn):
            eroded[i, j] = np.min(
                image[i - hkm:i + hkm + 1, j - hkn:j + hkn + 1][kernel == 1])
                # это срез изображения вокруг пикселя (i, j) с использованием размеров ядра
    return eroded


def dilate(image, kernel):
    m, n = image.shape
    km, kn = kernel.shape
    hkm = km // 2
    hkn = kn // 2
    dilated = np.copy(image)

    for i in range(hkm, m - hkm):
        for j in range(hkn, n - hkn):
            dilated[i, j] = np.max(
                image[i - hkm:i + hkm + 1, j - hkn:j + hkn + 1][kernel == 1])

    return dilated
