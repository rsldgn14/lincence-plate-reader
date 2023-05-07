import cv2
import numpy as np
from pytesseract import pytesseract


def preprocess(frame):
    # Görüntüyü griye çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gürültüyü azaltmak için median blur uygula
    gray = cv2.medianBlur(gray, 3)

    # Dilate (genişletme) işlemi uygula
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    gray = cv2.dilate(gray, kernel, iterations=1)

    # OCR işlemini gerçekleştir ve metni döndür
    text = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')

    return text
