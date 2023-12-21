import os

import pytesseract
import easyocr
from PIL import Image

from calculate_similarity_score import calculate_similarity_score
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

tesseract_config = r'--oem 1 --psm 6'  # Настройки для TesseractOCR
reader = easyocr.Reader(['en', 'ru'])  # EasyOCR с поддержкой английского и русского


# Tesseract, запись результатов в файл аннотаций.
def annotate_images(image_paths, annotation_file):
    annotations = {}
    for image_path in image_paths:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, config=tesseract_config, lang='rus+eng')
        annotations[image_path] = text.strip()

    with open(annotation_file, 'w', encoding='utf-8',errors='replace') as file:
        for image_path, annotation in annotations.items():
            file.write(f"{image_path}: {annotation}\n")

# tesseract
def straight_recognition(image_paths):
    predictions = {}
    for image_path in image_paths:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, config=tesseract_config, lang='rus+eng')
        predictions[image_path] = text.strip()

    return predictions

# easyocr
def easyocr_recognition(image_paths):
    predictions = {}
    for image_path in image_paths:
        img = Image.open(image_path)
        result = reader.readtext(image_path)
        text = ' '.join([item[1] for item in result])
        predictions[image_path] = text.strip()

    return predictions


def test_recognition(rec_type, val_type, image_paths, truth_file):
    if rec_type == 'straight':
        predictions = straight_recognition(image_paths)
    elif rec_type == 'easyocr':
        predictions = easyocr_recognition(image_paths)
    else:
        raise ValueError(f"Unsupported recognition type: {rec_type}")

    ground_truth = {}
    with open(truth_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) >= 2:
                image_path = parts[0].strip()
                true_text = parts[1].strip()
                ground_truth[image_path] = true_text
            else:
                # Обработка случая, когда в строке нет символа ':' или после ':' нет текста
                print(f"Invalid line format: {line}")
    # Оцениваем точность на основе указанного типа проверки
    if val_type == 'full_match':
        accuracy = evaluate_accuracy_wordwise(ground_truth, predictions)
    if val_type == "part_match":
        accuracy = evaluate_partial_accuracy_wordwise(ground_truth, predictions, 0.7)

    # Сохраняем прогнозы в файл в кодировке UTF-8
    predictions_file = f'{rec_type}_predictions.txt'
    with open(predictions_file, 'w', encoding='utf-8') as file:
        for image_path, prediction in predictions.items():
            file.write(f"{image_path}: {prediction}\n")

        return accuracy

# СРАВНИВАЕМ ПОСЛОВНО
def compare_predictions_wordwise(truth_file, straight_predictions_file, easyocr_predictions_file):
    ground_truth = {}
    with open(truth_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) >= 2:
                image_path = parts[0].strip()
                true_text = parts[1].strip()
                ground_truth[image_path] = true_text

    # Загрузка предсказаний от straight_recognition
    straight_predictions = {}
    with open(straight_predictions_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) >= 2:
                image_path = parts[0].strip()
                prediction_text = parts[1].strip()
                straight_predictions[image_path] = prediction_text
            #else:
                #print(f"Invalid line format in {straight_predictions_file}: {line}")

    # Загрузка предсказаний от easyocr_recognition
    easyocr_predictions = {}
    with open(easyocr_predictions_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) >= 2:
                image_path = parts[0].strip()
                prediction_text = parts[1].strip()
                easyocr_predictions[image_path] = prediction_text
            #else:
                #print(f"Invalid line format in {easyocr_predictions_file}: {line}")

    # Сравнение по словам
    straight_accuracy = evaluate_accuracy_wordwise(ground_truth, straight_predictions)
    easyocr_accuracy = evaluate_accuracy_wordwise(ground_truth, easyocr_predictions)

    return straight_accuracy, easyocr_accuracy


def evaluate_accuracy_wordwise(ground_truth, predictions):
    correct = 0
    total = len(ground_truth)

    for image_path, true_text in ground_truth.items():
        predicted_text = predictions.get(image_path, '')
        true_words = set(true_text.split())
        predicted_words = set(predicted_text.split())
        if true_words == predicted_words:
            correct += 1

    accuracy = correct / total
    return accuracy

def evaluate_partial_accuracy_wordwise(ground_truth, predictions, threshold):
    correct = 0
    total = len(ground_truth)

    for image_path, true_text in ground_truth.items():
        predicted_text = predictions.get(image_path, '')
        true_words = true_text.split()
        predicted_words = predicted_text.split()

        matched_words = 0
        for true_word in true_words:
            for predicted_word in predicted_words:
                if calculate_similarity_score(true_word, predicted_word) >= threshold:  # Пример использования порогового значения
                    matched_words += 1
                    break

        if matched_words == len(predicted_words) and len(predicted_words) == len(true_words):
            correct += 1

    accuracy = correct / total
    return accuracy




# аугментируем датасет
def augment_dataset(original_path, augmented_path):

    # Создаем новый каталог для расширенного набора данных
    if not os.path.exists(augmented_path):
        os.makedirs(augmented_path)

    for image_path in os.listdir(original_path):
        if image_path.endswith(('.jpg', '.jpeg', '.png')):
            original_image = Image.open(os.path.join(original_path, image_path))

            original_image = original_image.convert('RGB')

            for angle in range(-20, 21):
                rotated_image = original_image.rotate(angle)
                rotated_image_path = os.path.join(augmented_path, f"{os.path.splitext(image_path)[0]}_{angle}.jpg")
                rotated_image.save(rotated_image_path)


def main():
    image_paths = ['yandex_capchi/1-.jpg', 'yandex_capchi/2-.jpg', 'yandex_capchi/3-.jpg', 'yandex_capchi/4-.jpg', 'yandex_capchi/5-.jpg', 'yandex_capchi/6-.jpg',
                   'yandex_capchi/7-.jpg', 'yandex_capchi/8-.jpg', 'yandex_capchi/9-.jpg', 'yandex_capchi/10-.jpg', 'yandex_capchi/11-.jpg']

    captcha_txt = 'yandex_capchi/from_captcha_text.txt'
    true_captcha_txt = 'yandex_capchi/true_text.txt'

    # # Tesseract
    # annotate_images(image_paths, captcha_txt)
    #
    # recognition_type = 'easyocr'  #straight   easyocr
    # validation_type = 'full_match'  # или другой способ оценки
    #
    # accuracy = test_recognition(recognition_type, validation_type, image_paths, true_captcha_txt)
    # print(f"Точность для {recognition_type} распознавания: {accuracy * 100:.2f}%")
    #
    # recognition_type = 'straight'  #straight   easyocr
    # validation_type = 'full_match'  # или другой способ оценки
    #
    # accuracy = test_recognition(recognition_type, validation_type, image_paths, true_captcha_txt)
    # print(f"Точность для {recognition_type} распознавания: {accuracy * 100:.2f}%")

    print("\nPart Match")

    recognition_type = 'easyocr'
    validation_type = 'part_match'

    accuracy = test_recognition(recognition_type, validation_type, image_paths, true_captcha_txt)
    print(f"Точность для {recognition_type} распознавания: {accuracy * 100:.2f}%")

    recognition_type = 'straight'
    validation_type = 'part_match'

    accuracy = test_recognition(recognition_type, validation_type, image_paths, true_captcha_txt)
    print(f"Точность для {recognition_type} распознавания: {accuracy * 100:.2f}%")

    print("\nFull Match")

    recognition_type = 'easyocr'
    validation_type = 'full_match'

    accuracy = test_recognition(recognition_type, validation_type, image_paths, true_captcha_txt)
    print(f"Точность для {recognition_type} распознавания: {accuracy * 100:.2f}%")

    recognition_type = 'straight'
    validation_type = 'full_match'

    accuracy = test_recognition(recognition_type, validation_type, image_paths, true_captcha_txt)
    print(f"Точность для {recognition_type} распознавания: {accuracy * 100:.2f}%")
    print("\nМетод 2")
    straight_predictions_file = 'straight_predictions.txt'
    easyocr_predictions_file = 'easyocr_predictions.txt'

    straight_accuracy, easyocr_accuracy = compare_predictions_wordwise(true_captcha_txt,
                                                                       straight_predictions_file,
                                                                       easyocr_predictions_file)

    print(f"Точность распознавания EasyOCR: {easyocr_accuracy * 100:.2f}%")
    print(f"Точность распознавания Straight: {straight_accuracy * 100:.2f}%")


if __name__ == "__main__":
    main()