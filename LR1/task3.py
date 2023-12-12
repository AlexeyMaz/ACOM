# Задание 3. Отобразить видео в окне. Рассмотреть методы класса
# VideoCapture и попробовать отображать видео в разных форматах, в частности
# размеры и цветовая гамма.

import cv2

cap = cv2.VideoCapture(r'..\resources\Dream_lake_1.mp4')


while True:
    # Захват кадра из видеопотока
    ret, frame = cap.read()

    if not ret:
        print('Конец видео')
        break

    frame = cv2.resize(frame, (500, 360))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", frame)

    # Выход на Esc
    if cv2.waitKey(10) & 0xFF == 27:
        break

# Освобождение памяти
cap.release()
cv2.destroyAllWindows()
