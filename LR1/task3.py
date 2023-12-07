# Задание 3. Отобразить видео в окне. Рассмотреть методы класса
# VideoCapture и попробовать отображать видео в разных форматах, в частности
# размеры и цветовая гамма.

import cv2

cap = cv2.VideoCapture(r'..\resources\Dream_lake_1.mp4')

# cv2.CAP_PROP_BRIGHTNESS - яркость (0-1)
# cv2.CAP_PROP_CONTRAST - контраст (0-1)
# cv2.CAP_PROP_SATURATION - насыщенность (0-1)
# cv2.CAP_PROP_HUE - оттенок (0-1)

# cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.1)
# cap.set(cv2.CAP_PROP_CONTRAST, 0.1)
# cap.set(cv2.CAP_PROP_SATURATION, 0.2)
#
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
#
# print("CAP_PROP_BRIGHTNESS:", cap.get(cv2.CAP_PROP_BRIGHTNESS))
# print("CAP_PROP_CONTRAST:", cap.get(cv2.CAP_PROP_CONTRAST))
# print("CAP_PROP_SATURATION:", cap.get(cv2.CAP_PROP_SATURATION))
# print("CAP_PROP_HUE:", cap.get(cv2.CAP_PROP_HUE))
# print("CAP_PROP_FRAME_WIDTH:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print("CAP_PROP_FRAME_HEIGHT:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    # Захват кадра из видеопотока
    ret, frame = cap.read()

    if not ret:
        print('Конец видео')
        break

    # frame = cv2.resize(frame, (1000, 760))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", frame)

    # Выход на Esc
    if cv2.waitKey(10) & 0xFF == 27:
        break

# Освобождение памяти
cap.release()
cv2.destroyAllWindows()
