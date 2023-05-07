import re

import imutils
import numpy as np
from PyQt5.QtGui import QDesktopServices, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import cv2
from PyQt5.uic.uiparser import QtCore
from pytesseract import pytesseract

from db.init import get_user_information_by_plate
from pyui.addUser import addPage
from pyui.deletUser import deleteUser
from pyui.list_user import listWindow
from pyui.updateUser import updateUser
from pyui.utils import preprocess
from ui.main_python import Ui_Dialog

pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'


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
        self.ui.addUserButton.clicked.connect(self.add_user_page)
        self.ui.deleteUserButton.clicked.connect(self.delete_user_page)
        self.ui.updateUserButton.clicked.connect(self.update_user_page)
        self.image = None
        self.currentPlate = None
        self.data = None

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

    def update_user_page(self):
        self.update_user = updateUser()
        self.update_user.show()

    def delete_user_page(self):
        self.delete_user = deleteUser()
        self.delete_user.show()

    def add_user_page(self):
        self.add_page = addPage()
        self.add_page.show()

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
        try:
            plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

            if plateCascade.empty():
                print("Bulamadımmm")

            # Kamera bağlantısını başlatın
            cap = cv2.VideoCapture(0)

            while True:
                # Görüntü yakalayın
                ret, frame = cap.read()

                # Görüntü boyutunu küçültün
                small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

                # Görüntüyü gri tonlamalı görüntüye dönüştürün
                gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

                # Kenar tespiti yapın
                edges = cv2.Canny(gray, 100, 200)

                # Plakaları tespit edin
                plates = plateCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80),
                                                       maxSize=(300, 300))

                # Plaka bölgesini kesin ve OCR işlemine tabi tutun
                for (x, y, w, h) in plates:
                    plate_frame = small_frame[y:y + h, x:x + w]
                    plate_text = preprocess(plate_frame)

                    # Plaka metnini görüntüye yazdırın
                    plate_text = re.sub(r'\W+', '', plate_text)
                    user = get_user_information_by_plate(plate_text)
                    print(plate_text)
                    print(user)
                    cv2.putText(small_frame, plate_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.rectangle(small_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Görüntüyü ekrana gösterin
                cv2.imshow("Plaka Okuma Uygulaması", small_frame)
                if 'plate_frame' in locals():
                    cv2.imshow("Okunan Plaka Görüntüsü", plate_frame)
                # Eğer "q" tuşuna basılırsa döngüyü sonlandırın
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Kullanılan kaynakları serbest bırakın ve pencereleri kapatın
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
