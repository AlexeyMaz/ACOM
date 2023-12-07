# Задание 7 (самостоятельно). Отобразить информацию с вебкамеры,
# записать видео в файл, продемонстрировать видео.

import cv2

cap = cv2.VideoCapture(0)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(r'..\resources\output7.mp4', fourcc, 25, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    rect_width = 100  # Ширина прямоугольника
    rect_height = 300  # Высота прямоугольника

    top_left_x = (width - rect_width) // 2
    top_left_y = (height - rect_height) // 2
    bottom_right_x = top_left_x + rect_width
    bottom_right_y = top_left_y + rect_height
    cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)

    rect_width = 300  # Ширина прямоугольника
    rect_height = 100  # Высота прямоугольника

    top_left_x = (width - rect_width) // 2
    top_left_y = (height - rect_height) // 2
    bottom_right_x = top_left_x + rect_width
    bottom_right_y = top_left_y + rect_height
    cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)
    ROI = frame[top_left_y:top_left_y + rect_height, top_left_x:top_left_x + rect_width]

    blur = cv2.GaussianBlur(ROI, (101, 1), 30)
    frame[top_left_y:top_left_y + rect_height, top_left_x:top_left_x + rect_width] = blur

    cv2.imshow("Video", frame)
    video_writer.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

video_writer.release()
cap.release()
cv2.destroyAllWindows()
