import cv2
import numpy as np


def preprocess(img):
    # Görüntüyü gri tonlamaya dönüştürün
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Kenar tespiti yapın
    canny = cv2.Canny(gray, 170, 200)

    # Gürültüyü azaltın
    blur = cv2.GaussianBlur(canny, (5, 5), 0)

    # Dilate (genişletme) işlemi yapın
    kernel = np.ones((3, 3))
    dilate = cv2.dilate(blur, kernel, iterations=1)

    return dilate
