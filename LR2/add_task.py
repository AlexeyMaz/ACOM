import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 200])
    upper_red = np.array([100, 255, 255])

    # Создаем маску для красного цвета
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Находим контуры в бинарном изображении
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Пропускаем слишком маленькие контуры
        if cv2.contourArea(contour) < 500:
            continue

        # Вычисляем координаты и размеры прямоугольника, в который вписан контур
        x, y, w, h = cv2.boundingRect(contour)

        # Рисуем черный прямоугольник вокруг контура на оригинальном кадре
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # Рисуем зеленые прицелы в центре прямоугольника
        a = 7
        b = 1000
        c_x = x + w // 2
        c_y = y + h // 2

        color2 = (0, 255, 0)

        # левая часть прицела
        cv2.rectangle(frame,
                      (c_x - (b // 256) - a, c_y - (b // 256)),
                      (c_x + (b // 256) - a, c_y + (b // 256)),
                      color2, -1)
        # правая часть прицела
        cv2.rectangle(frame,
                      (c_x - (b // 256) + a, c_y - (b // 256)),
                      (c_x + (b // 256) + a, c_y + (b // 256)),
                      color2, -1)
        # верхняя часть прицела
        cv2.rectangle(frame,
                      (c_x - (b // 256), c_y - (b // 256) - a),
                      (c_x + (b // 256), c_y + (b // 256) - a),
                      color2, -1)
        # нижняя часть прицела
        cv2.rectangle(frame,
                      (c_x - (b // 256), c_y - (b // 256) + a),
                      (c_x + (b // 256), c_y + (b // 256) + a),
                      color2, -1)

    cv2.imshow('Result_frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
