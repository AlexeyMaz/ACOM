# импорт библиотеки Keras и необходимых соответствующих модулей
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.callbacks import TensorBoard
from torch.utils.tensorboard import SummaryWriter
import numpy as np
import time

start_time = time.time()
writer = SummaryWriter(log_dir='/LR_6/logs_1')

# загрузка данных MNIST (первый кортеж - тренировочные изображения и метки, а второй - тестовые изображения и метки)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# преобразование каждого изображения (тренировочных и тестовых) в одномерный массив
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
# преобразования типа данных тренировочных и тестовых изображений MNIST из uint8 в float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
# нормализация значений пикселей изображений в диапазоне от 0 до 1
x_train /= 255
x_test /= 255
# в базе данных MNIST содержится 10 классов цифр от 0 до 9
num_classes = 10
# преобразование меток в категории для каждого типа данных
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
# создание новой модели многослойного персептрона
model = Sequential()
# добавление первого слоя
model.add(Dense(512, activation='relu', input_shape=(784,)))
# метод регуляризации, который случайным образом удаляет нейроны из сети во время обучения для предотвращения
# переобучения
model.add(Dropout(0.2))
# добавление второго слоя
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
# добавление выходного слоя
model.add(Dense(num_classes, activation='softmax'))
# Компиляция модели и обучение ее на тренировочных данных
# настройка процесса обучения модели
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir=r'Logs', histogram_freq=0,
                          write_graph=True, write_images=False)

# запись данные изображений в файлы событий
images = x_train[:20].reshape(-1, 28, 28, 1)
images = (images * 255).astype(np.uint8)
writer.add_images('mnist_images', images, dataformats='NHWC')
writer.close()

# обучение модели на тренировочных данных
history = model.fit(x_train, y_train,
                    batch_size=128,  # размер пакета
                    epochs=15,  # количество эпох
                    verbose=1,  # вывод информации о потерях, метриках и прогресс-бар
                    # тестовые данные будут использоваться для проверки производительности модели во время обучения
                    validation_data=(x_test, y_test),
                    callbacks=[tensorboard])

# сохранение модели
model.save(r'Models/multilayer_perceptron.keras')

print('==============================================================')
# оценка потерь и точности модели
score = model.evaluate(x_test, y_test, verbose=0)
print('Потери на тестовых данных:', score[0])
print('Точность модели на тестовых данных:', score[1])

# подсчёт процента корректной работы на тестовой базе
accuracy = score[1]
percent_correct = accuracy * 100
print('Процент корректной работы:', percent_correct)

# подсчёт затраченного времени
end_time = time.time()
print('Затраченное время:', end_time - start_time)
print('==============================================================')
