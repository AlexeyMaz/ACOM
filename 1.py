import cv2

img1 = cv2.imread(r'C:\Users\AlmaZ\Documents\The Witcher 3\screenshots\1.png')
# # cv2.imread(	filename[, flags]	)
# # flags = IMREAD_COLOR
# # cv.imread(filename[, flags]) -> retval
# cv2.namedWindow("Display window",cv2.WINDOW_KEEPRATIO)
# cv2.imshow("Display window", img1)
# cv2.waitKey(0)



# cap = cv2.VideoCapture(r'C:\Users\AlmaZ\Videos\Resident Evil 4 Biohazard 4\Resident Evil 4 Biohazard 4 2023.09.05 - 19.43.57.04.DVR', cv2.CAP_ANY)
# ret, frame = cap.read()
# if not(ret):
#     break
# cv2.imshow('frame', frame)
# if cv2.waitKey(1) & 0xFF == 27:
#     break
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
#

# # создадим объект VideoCapture для захвата видео
# cap = cv2.VideoCapture(r'C:\Users\AlmaZ\Videos\papka\11.mp4', cv2.CAP_ANY)
#
# # Если не удалось открыть файл, выводим сообщение об ошибке
# if cap.isOpened() == False:
#     print('Не возможно открыть файл')
#
# # Пока файл открыт
# while cap.isOpened():
#     # поочередно считываем кадры видео
#     fl, img = cap.read()
#     # если кадры закончились, совершаем выход
#     if img is None:
#         break
#     # выводим текущий кадр на экран
#     cv2.imshow("Cat", img)
#     # при нажатии клавиши "q", совершаем выход
#     if cv2.waitKey(25) == ord('q'):
#         break
#
# # освобождаем память от переменной cap
# cap.release()
# # закрываем все открытые opencv окна
# cv2.destroyAllWindows()

#




# cap = cv2.VideoCapture(0)
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video_writer = cv2.VideoWriter("output2.mp4", fourcc, 25, (w, h))
# while True:
#     ret, img = cap.read()
#     cv2.imshow("camera", img)
#     if cv2.waitKey(25) == ord('q'): # Клавиша Esc
#         break
# cap.release()
# cv2.destroyAllWindows()

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.namedWindow("Display window",cv2.WINDOW_KEEPRATIO)
cv2.imshow("Display window", hsv)
cv2.waitKey(0)