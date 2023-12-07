# Задание 2. Вывести на экран изображение. Протестировать три
# возможных расширения, три различных флага для создания окна и три
# различных флага для чтения изображения.

# Примеры флагов для создания окна
# cv2.WINDOW_NORMAL - Окно с изменяемым размером
# cv2.WINDOW_AUTOSIZE - Окно с фиксированным размером
# cv2.WINDOW_FULLSCREEN - Полноэкранное окно

# Примеры флагов для чтения изображения
# cv2.IMREAD_COLOR - Чтение изображения в цвете (по умолчанию)
# cv2.IMREAD_GRAYSCALE - Чтение изображения в оттенках серого
# cv2.IMREAD_UNCHANGED - Чтение изображения без изменений

import cv2
# Загружаем изображение с разными расширениями
image_extensions = ["png", "jpg", "bmp"]

for ext in image_extensions:
    image_path = r'..\resources\1.jpg'
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Чтение в оттенках серого

    if img is not None:
        cv2.namedWindow(f"Image ({ext})", cv2.WINDOW_NORMAL)  # Окно с изменяемым размером
        cv2.imshow(f"Image ({ext})", img)

        # Ждем нажатия клавиши и закрываем окно по нажатию клавиши
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Не получилось открыть изображение в этом формате {ext}")
