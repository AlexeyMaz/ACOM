import cv2
import numpy as np
i = 0
# Здесь определяется функция main с четырьмя аргументами:
# kernel_size (размер ядра для гауссова размытия),
# standard_deviation (стандартное отклонение для гауссова размытия),
# delta_tresh (порог значений для бинаризации разности между кадрами)
# и min_area (минимальная площадь контура для рассмотрения).
def main(kernel_size, standard_deviation, delta_tresh, min_area):
    global i
    i += 1
    video = cv2.VideoCapture('vid/main_video.mov', cv2.CAP_ANY)
    ret, frame = video.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (kernel_size, kernel_size), standard_deviation)
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # Формируется кодек для записи видео, который соответствует формату
    # MP4(в данном случае 'mp4v').
    video_writer = cv2.VideoWriter('result_videos/result' + str(i) + '.mp4', fourcc, 144, (w, h))
    # Создается объект VideoWriter, который будет использовать
    # вышеуказанный кодек для записи выводимого видео с заданной
    # частотой кадров(144 кадров в секунду) и размерами кадров w на h.

    while True:
        # сохраняем старый кадр чтобы вычислить разниц между кадрами
        print("...")
        old_img = img.copy()
        ok, frame = video.read()
        if not ok:
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (kernel_size, kernel_size), standard_deviation)

        # вычисляем разницу
        diff = cv2.absdiff(img, old_img)

        # Абсолютная разность бинаризуется: пиксели с
        # интенсивностью выше delta_tresh становятся
        # белыми(255), остальные - черными.
        thresh = cv2.threshold(diff, delta_tresh, 255, cv2.THRESH_BINARY)[1]
        # print(thresh)
        # cv2.imshow("a",thresh)
        # находим контуры
        (contors, hierarchy) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)