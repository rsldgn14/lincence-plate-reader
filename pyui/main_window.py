import numpy as np
from PyQt5.QtGui import QDesktopServices, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import cv2
from PyQt5.uic.uiparser import QtCore
from pytesseract import pytesseract

from pyui.list_user import listWindow
from ui.main_python import Ui_Dialog

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.uploadButton.clicked.connect(self.upload)
        self.selected_image = None  # Seçilen resmin yolu için bir sınıf değişkeni
        self.ui.showImage.clicked.connect(self.show_picture)
        self.ui.closeButton.clicked.connect(self.close_picture)
        self.ui.readPlateButton.clicked.connect(self.read_plate)
        self.ui.viewAllUsersButton.clicked.connect(self.show_user_list)
        self.image = None
        self.currentPlate = None

    def upload(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "",
                                                  "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if fileName:
            self.selected_image = fileName
            self.image = cv2.imread(fileName)
            self.ui.platePhoto.setPixmap(QPixmap(fileName).scaled(221, 201))
            if self.image is not None:
                self.image = cv2.resize(self.image, (500, 500))

    def show_user_list(self):
        self.list_widget = listWindow()
        self.list_widget.show()

    def show_picture(self):
        if self.image is not None:
            cv2.imshow("Deneme", self.image)

    def close_picture(self):
        if self.image is not None:
            cv2.destroyAllWindows()

    def read_plate(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (5, 5), 0)
            edged = cv2.Canny(gray, 50, 200)
            contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            plate = None
            for contour in contours:
                # Kontur Yaklaşımı
                perimeter = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

                # Dikdörtgen Kontur
                if len(approx) == 4:
                    plate = approx
                    break

            if plate is not None:
                mask = np.zeros_like(self.image)
                cv2.drawContours(mask, [plate], 0, (255, 255, 255), -1)
                masked = cv2.bitwise_and(self.image, mask)
                (x, y, w, h) = cv2.boundingRect(plate)
                plate_img = masked[y:y + h, x:x + w]
                plate_img = cv2.resize(plate_img, (600, 100))

                # OCR ile Plaka Tanıma
                try:
                    plate_text = pytesseract.image_to_string(plate_img, lang='eng', config='--psm 11')
                    self.ui.plateNumber.setText(plate_text)
                    self.currentPlate = plate_text
                except Exception as e:
                    print("Hata", e)
