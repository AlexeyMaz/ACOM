# Задание 8 (самостоятельно). Залить крест одним из 3 цветов – красный,
# зеленый, синий по следующему правилу: НА ОСНОВАНИИ ФОРМАТА RGB
# определить, центральный пиксель ближе к какому из цветов красный,
# зеленый, синий и таким цветом заполнить крест.

import cv2
import numpy as np


def closest_color(pixel):
    color_distances = [
        np.linalg.norm(pixel - np.array([0, 0, 255])),
        np.linalg.norm(pixel - np.array([0, 255, 0])),
        np.linalg.norm(pixel - np.array([255, 0, 0]))
    ]

    return np.argmin(color_distances)


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    center_x = width // 2
    center_y = height // 2
    center_pixel = frame[center_y, center_x]

    closest = closest_color(center_pixel)
    print(closest)

    rect_width = 60  # Ширина прямоугольника
    rect_height = 300  # Высота прямоугольника

    top_left_x = (width - rect_width) // 2
    top_left_y = (height - rect_height) // 2
    bottom_right_x = top_left_x + rect_width
    bottom_right_y = top_left_y + rect_height
    if closest == 0:
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), -1)
    if closest == 1:
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), -1)
    if closest == 2:
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), -1)

    rect_width = 300  # Ширина прямоугольника
    rect_height = 60  # Высота прямоугольника

    top_left_x = (width - rect_width) // 2
    top_left_y = (height - rect_height) // 2
    bottom_right_x = top_left_x + rect_width
    bottom_right_y = top_left_y + rect_height
    if closest == 0:
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), -1)
    if closest == 1:
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), -1)
    if closest == 2:
        cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), -1)

    cv2.imshow("Colored Cross", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
