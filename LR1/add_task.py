# -*- coding: cp1251 -*-
import math
import cv2
import numpy as np

def closest_color(pixel):
    color_distances = [
        np.linalg.norm(pixel - np.array([0, 0, 255])),
        np.linalg.norm(pixel - np.array([0, 255, 0])),
        np.linalg.norm(pixel - np.array([255, 0, 0]))
    ]

    return np.argmin(color_distances)


cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    center_x = width // 2
    center_y = height // 2
    center_pixel = frame[center_y, center_x]

    closest = closest_color(center_pixel)

    star_color = (0, 0, 0)
    if closest == 0:
        star_color = (0, 0, 255)
    elif closest == 1:
        star_color = (0, 255, 0)
    elif closest == 2:
        star_color = (255, 0, 0)

    def draw_star(image, size, angle_degrees, color):
        points = []

        for i in range(5):
            x = int(center_x + size * math.cos(math.radians(i * 72 + angle_degrees)))
            y = int(center_y + size * math.sin(math.radians(i * 72 + angle_degrees)))
            points.append((x, y))

        for i in range(5):
            cv2.line(image, points[i], points[(i + 2) % 5], color, 4)

        cv2.circle(image, (center_x, center_y), size, color, 4)

    draw_star(frame, 100, 54, star_color)

    cv2.imshow("Colored Cross", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

frame.release()
cv2.destroyAllWindows()
