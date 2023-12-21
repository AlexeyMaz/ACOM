import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r'../resources/2.jpg')
print(pytesseract.image_to_string(img, lang='eng'))
