import json
import cv2
import numpy as np
from math import dist
import pytesseract
import re


from QTGraphicInterfaces.TransactionsInterfaceNew import Ui_TransactionInterfaceNew
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import QSizeF
import Bussiness.Models.Runt as runt
# Comunicaciones
from Integration.ParkingApi import ParkingApi as api
#Modelos
from Bussiness.Models.VehicleTransaction import VehicleTransaction
from Windows.TransactionsForm import TransactionsForm

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
custom_config = r'--psm 6 '


class Transaction(QtWidgets.QMainWindow):

    def __init__(self, main_context, parking_id):
        """
            Constructor donde se inicializan parámetros de interfaz gráfica
        """
        super(Transaction, self).__init__()
        self.ui = Ui_TransactionInterfaceNew()
        self.ui.setupUi(self)
        self.api = api()
        self.parking_id = parking_id
        self.main_context = main_context
        self.ui.txb_resume.setPlainText("")
        self.ui.btn_open_camera.clicked.connect(lambda callback: self.open_camera())
        self.ui.btn_open_keyboard.clicked.connect(lambda callback: self.open_transactions_form(None))
        self.ui.btn_print.clicked.connect(lambda callback: self.print_file())

    def open_camera(self):

        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1290)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while True:
            ret, frame = cap.read()

            if ret:
                cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('w'):
                self.process_card(frame)

        cap.release()
        cv2.destroyAllWindows()

    def print_transaction(self, text):
        self.ui.txb_resume.setPlainText(text)

    @staticmethod
    def sort_coordinates(coord_a, coord_b, coord_c, coord_d):
        """
        Ordenar coordenadas en el espacio absoluto
        :param coord_a:
        :param coord_b:
        :param coord_c:
        :param coord_d:
        :return:
        """
        work_list = [coord_a.tolist(), coord_b.tolist(), coord_c.tolist(), coord_d.tolist()]
        final_work_list = []

        for wl in work_list:
            # Quita el wl de la lista
            partial_work_list_2nd = [pwl for pwl in work_list if pwl != wl]
            # Duplicador para generar todos los casos posibles
            for pwl2 in partial_work_list_2nd:
                partial_work_list_3rd = [pwl3 for pwl3 in partial_work_list_2nd if pwl3 != pwl2]

                first = [wl, pwl2, partial_work_list_3rd[0], partial_work_list_3rd[1]]
                second = [wl, pwl2, partial_work_list_3rd[1], partial_work_list_3rd[0]]

                final_work_list.append(first)
                final_work_list.append(second)

        sorted_list = []

        # Comprobación de reglas de coordenadas
        for i in final_work_list:
            # Reglas de elección
            if i[0][0] < i[1][0] and i[0][1] < i[3][1]:
                if i[1][0] > i[0][0] and i[1][1] < i[2][1]:
                    if i[2][0] > i[3][0] and i[2][1] > i[1][1]:
                        if i[3][0] < i[2][0] and i[3][1] > i[0][1]:
                            # Regla de orientación cruzada
                            if i[1][1] < i[3][1] and i[0][1] < i[2][1]:

                                sorted_list = np.array(i)

                                p1 = i[0]
                                p2 = i[1]
                                p3 = i[3]
                                p4 = i[2]

                                # Verificación de orientación

                                # Horizontales
                                dp1p2 = dist(p1, p2)
                                dp3p4 = dist(p3, p4)
                                dw = int((dp1p2 + dp3p4) / 2)

                                # Verticales
                                dp1p3 = dist(p1, p3)
                                dp2p4 = dist(p2, p4)
                                dh = int((dp1p3 + dp2p4) / 2)

                                if dw > dh:
                                    sorted_list = np.array([p2, p4, p3, p1])

        return sorted_list

    @staticmethod
    def save_image(name, image):

        if True == True:
            #file_name = 'C:/Users/R5 3400/Desktop/imagenes proyecto/pasos/' + name + ".png"
            cv2.imwrite(file_name, image)

    def process_card(self, frame):

        #Transaction.save_image('0 Original', frame)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Transaction.save_image('1 Blanco y negro', image)
        GB = cv2.GaussianBlur(image, (15, 15), 1)
        #Transaction.save_image('2 Gaussian blur', GB)
        GB = cv2.medianBlur(GB, 15)
        #Transaction.save_image('3 MedianBlur', GB)
        kernel = np.ones((10, 10), np.uint8)
        GB = cv2.morphologyEx(GB, cv2.MORPH_OPEN, kernel)
        #Transaction.save_image('4 Transf morfologica open', GB)
        kernelopening = np.ones((2, 2), np.uint8)
        # GB = cv2.erode(GB,kernel,iterations = 4)
        th3 = cv2.adaptiveThreshold(GB, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        #Transaction.save_image('5 Adaptative threshold', th3)
        th3 = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernelopening)
        #Transaction.save_image('6 Transf morfologica open', th3)
        # erosion = cv2.erode(th3, kernelopening, iterations=3)
        # Transaction.save_image('7 Erosion', erosion)
        # th4 = cv2.morphologyEx(erosion, cv2.MORPH_GRADIENT, kernelopening)
        # closing = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)
        # kernel = np.ones((2, 2), np.uint8)
        # th4 = cv2.dilate(th4, kernel, iterations=2)
        # erosion = cv2.erode(th3,kernel,iterations = 3)
        # GB = cv2.GaussianBlur(image, (5, 5), 1)
        contornos, hierachy = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frame_contornos = cv2.drawContours(frame, contornos, -1, (0, 255, 0), 3)
        #Transaction.save_image('7 contornos', frame_contornos)

        c = max(contornos, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        epsilon = 0.01 * cv2.arcLength(c, True)
        aprox = cv2.approxPolyDP(c, epsilon, True)

        coords = Transaction.sort_coordinates(aprox[0][0], aprox[1][0], aprox[2][0], aprox[3][0])

        c1 = coords[0]
        c2 = coords[1]
        c3 = coords[2]
        c4 = coords[3]

        # Transformación de perspectivas
        tc = np.float32([c4, c1, c3, c2])
        perspective_zone = np.float32([[0, 0], [800, 0], [0, 497], [800, 497]])
        m = cv2.getPerspectiveTransform(tc, perspective_zone)
        transformed = cv2.warpPerspective(frame, m, (800, 497))
        #Transaction.save_image('9 perspectiva', transformed)

        transformed = cv2.cvtColor(transformed, cv2.COLOR_BGR2GRAY)

        plate_img = transformed[141:220, 0:144]
        #ret, plate_img = cv2.threshold(plate_img, 70, 255, cv2.THRESH_BINARY)

        #cv2.imshow("plate_img", plate_img)
        plate_text = pytesseract.image_to_string(plate_img, lang="spa", config=custom_config)

        cleaned_plate = re.findall('[A-Z]{3}[0-9]{3}|[A-Z]{3}[0-9]{2}[A-Z]{1}', plate_text)

        vt = VehicleTransaction()
        vt.IdLote = self.parking_id

        if len(cleaned_plate) >= 1:
            print(f"Plate: {cleaned_plate[0]}")
            self.ui.txb_resume.setPlainText(f"Placa: {cleaned_plate[0]}")
            vt.Placa = cleaned_plate[0]

        else:
            print("No se obtuvo una placa válida")
            self.ui.txb_resume.setPlainText("No se obtuvo una placa válida")

        class_img = transformed[240:320, 6:240]
        #ret, class_img = cv2.threshold(class_img, 70, 255, cv2.THRESH_BINARY)
        #cv2.imshow("class_img", class_img)
        class_text = pytesseract.image_to_string(class_img, lang="spa", config=custom_config)

        class_cleaned = ""
        for c in runt.classes:

            if c in class_text:
                class_cleaned = c
        vt.Clase = class_cleaned
        print(f"class_text:   {class_cleaned}")

        brand_img = transformed[142:217, 150:397]
        #ret, brand_img = cv2.threshold(brand_img, 70, 255, cv2.THRESH_BINARY)
        #cv2.imshow("brand_img", brand_img)
        brand_text = pytesseract.image_to_string(brand_img, lang="spa", config=custom_config)

        brand_cleaned = ""
        for b in runt.brands:
            if b in brand_text:
                brand_cleaned = b
                break
        vt.Marca = brand_cleaned
        print(f"brand_text:   {brand_cleaned}")

        line_img = transformed[139:240, 395:585]
        #ret, line_img = cv2.threshold(line_img, 70, 255, cv2.THRESH_BINARY)
        #cv2.imshow("line_img", line_img)
        line_text = pytesseract.image_to_string(line_img, lang="spa", config=custom_config)
        vt.Linea = line_text
        print(f"line_text:   {line_text}")

        color_img = transformed[214:265, 150:400]
        #ret, color_img = cv2.threshold(color_img, 70, 255, cv2.THRESH_BINARY)
        #cv2.imshow("color_img", color_img)
        color_text = pytesseract.image_to_string(color_img, lang="spa", config=custom_config)
        color_cleaned = ""
        for cc in runt.colors:
            if cc in color_text:
                color_cleaned = cc
                break

        vt.Color = color_cleaned
        print(f"color_text:   {color_text}")

        model_img = transformed[156:240, 672:796]
        #ret, model_img = cv2.threshold(model_img, 70, 255, cv2.THRESH_BINARY)
        #cv2.imshow("model_img", model_img)
        model_text = pytesseract.image_to_string(model_img, lang="spa", config=custom_config)
        model_cleaned = ""
        for m in runt.models:
            if m in model_text:
                model_cleaned = m
                break
        vt.Modelo = model_cleaned
        print(f"model_text:   {model_cleaned}")

        #cv2.imshow('Perspectiva', transformed)

        self.open_transactions_form(vt)

    def open_transactions_form(self, info):
        self.form_transactions = TransactionsForm(self, info=info, parking_id=self.parking_id)
        self.form_transactions.show()

    def print_file(self):

        printer = QPrinter()
        printer.setPaperSize(QSizeF(300, 300), QPrinter.Millimeter)
        printer.setPageMargins(10, 10, 10, 10, QPrinter.Millimeter)
        printer.setFullPage(True)

        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == dialog.Accepted:
            self.ui.txb_resume.print(printer)
