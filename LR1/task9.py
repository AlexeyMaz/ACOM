# Задание 9 (самостоятельно). Подключите телефон, подключитесь к его
# камере, выведете на экран видео с камеры. Продемонстрировать процесс на
# ноутбуке преподавателя и своем телефоне.

import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Конец видео.")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == 27:
        break

# Освобождение памяти
cap.release()
cv2.destroyAllWindows()

