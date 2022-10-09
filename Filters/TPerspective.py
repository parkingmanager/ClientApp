import cv2
import numpy as np
import copy
import math
from random import random
from enum import Enum
from Models import Utils

from QTGraphicInterfaces.DynamicMainInterfaceForm import Ui_MainWindow as Ui
from PyQt5 import QtCore, QtWidgets, QtGui
from Filters.Filter import Filter
from Models.Picture import Picture as Pic


class TPerspective:
    """
    Filtro que permite elegir específicamente zonas de una imagen para delimitar un estacionamiento
    """

    def __init__(self, picture: Pic, ui: Ui, row: int, col: int, widget_id: int, coordinates):

        # Imagen original
        self._original_picture = None
        self.coordinates = coordinates
        self.set_original_picture(picture)
        self.picture = self.get_original_picture()
        self.ui = ui
        self.widget_id = widget_id
        self.draw_widget(row, col, widget_id)
        self.mask = []

        # Parámetros funcionales
        self.tp_height = 500
        self.tp_width = 1200
        self.vertical_degrees = 25
        self.horizontal_degrees = 5
        self.horizontal_tolerance = 15
        self.vertical_tolerance = 20

    def set_visible(self, state):
        """
        Cambia la visibilidad de un filtro
        :param state:
        :return:
        """
        # Recupera el widget y aplica lógica
        group = getattr(self.ui, f'tp_group_{self.widget_id}')
        group.setVisible(state)

    def draw_widget(self, row: int, col: int, widget_id: int):
        """
        Renderiza el widget del filtro en la pantallaS
        :param row:
        :param col:
        :param widget_id:
        :return:
        """

        setattr(self.ui, f'tp_group_{widget_id}', QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents))
        tp_group = getattr(self.ui, f'tp_group_{widget_id}')
        tp_group.setMinimumSize(QtCore.QSize(0, 150))
        tp_group.setObjectName(f'tp_group_{widget_id}')

        setattr(self.ui, f'tp_btn_clear_{widget_id}', QtWidgets.QPushButton(tp_group))
        tp_btn_clear = getattr(self.ui, f'tp_btn_clear_{widget_id}')
        tp_btn_clear.setGeometry(QtCore.QRect(300, 30, 40, 40))
        tp_btn_clear.setMinimumSize(QtCore.QSize(40, 40))
        tp_btn_clear.setMaximumSize(QtCore.QSize(40, 40))
        tp_btn_clear.setText("")
        icon_tp_btn_clear = QtGui.QIcon()
        icon_tp_btn_clear.addPixmap(QtGui.QPixmap("icons/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tp_btn_clear.setIcon(icon_tp_btn_clear)
        tp_btn_clear.setIconSize(QtCore.QSize(32, 32))
        tp_btn_clear.setObjectName(f'tp_btn_clear_{widget_id}')

        setattr(self.ui, f'tp_btn_start_{widget_id}', QtWidgets.QPushButton(tp_group))
        tp_btn_start = getattr(self.ui, f'tp_btn_start_{widget_id}')
        tp_btn_start.setGeometry(QtCore.QRect(220, 30, 40, 40))
        tp_btn_start.setMinimumSize(QtCore.QSize(40, 40))
        tp_btn_start.setMaximumSize(QtCore.QSize(40, 40))
        tp_btn_start.setStyleSheet("border-color: rgb(255, 85, 0);")
        tp_btn_start.setText("")
        icon_tp_btn_start = QtGui.QIcon()
        icon_tp_btn_start.addPixmap(QtGui.QPixmap("icons/iniciar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tp_btn_start.setIcon(icon_tp_btn_start)
        tp_btn_start.setIconSize(QtCore.QSize(36, 36))
        tp_btn_start.setObjectName(f'tp_btn_start_{widget_id}')

        setattr(self.ui, f'tp_btn_view_{widget_id}', QtWidgets.QPushButton(tp_group))
        tp_btn_view = getattr(self.ui, f'tp_btn_view_{widget_id}')
        tp_btn_view.setGeometry(QtCore.QRect(260, 30, 40, 40))
        tp_btn_view.setMinimumSize(QtCore.QSize(40, 40))
        tp_btn_view.setMaximumSize(QtCore.QSize(40, 40))
        tp_btn_view.setText("")
        icon_tp_btn_view = QtGui.QIcon()
        icon_tp_btn_view.addPixmap(QtGui.QPixmap("icons/ver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tp_btn_view.setIcon(icon_tp_btn_view)
        tp_btn_view.setIconSize(QtCore.QSize(32, 32))
        tp_btn_view.setObjectName(f'tp_btn_view_{widget_id}')

        setattr(self.ui, f'tp_btn_delete_{widget_id}', QtWidgets.QPushButton(tp_group))
        tp_btn_delete = getattr(self.ui, f'tp_btn_delete_{widget_id}')
        tp_btn_delete.setGeometry(QtCore.QRect(340, 30, 40, 40))
        tp_btn_delete.setMinimumSize(QtCore.QSize(40, 40))
        tp_btn_delete.setMaximumSize(QtCore.QSize(40, 40))
        tp_btn_delete.setText("")
        icon_tp_btn_delete = QtGui.QIcon()
        icon_tp_btn_delete.addPixmap(QtGui.QPixmap("icons/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tp_btn_delete.setIcon(icon_tp_btn_delete)
        tp_btn_delete.setIconSize(QtCore.QSize(32, 32))
        tp_btn_delete.setObjectName(f'tp_btn_delete_{widget_id}')

        setattr(self.ui, f'tp_sb_v_lines_{widget_id}', QtWidgets.QSpinBox(tp_group))
        tp_sb_v_lines = getattr(self.ui, f'tp_sb_v_lines_{widget_id}')
        tp_sb_v_lines.setGeometry(QtCore.QRect(80, 40, 42, 20))
        tp_sb_v_lines.setMinimum(1)
        tp_sb_v_lines.setMaximum(60)
        tp_sb_v_lines.setProperty("value", 20)
        tp_sb_v_lines.setObjectName(f'tp_sb_v_lines_{widget_id}')

        setattr(self.ui, f'tp_sb_h_lines_{widget_id}', QtWidgets.QSpinBox(tp_group))
        tp_sb_h_lines = getattr(self.ui, f'tp_sb_h_lines_{widget_id}')
        tp_sb_h_lines.setGeometry(QtCore.QRect(20, 40, 42, 20))
        tp_sb_h_lines.setMinimum(1)
        tp_sb_h_lines.setMaximum(60)
        tp_sb_h_lines.setProperty("value", 15)
        tp_sb_h_lines.setObjectName(f'tp_sb_h_lines_{widget_id}')

        setattr(self.ui, f'tp_lbl_h_lines_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_h_lines = getattr(self.ui, f'tp_lbl_h_lines_{widget_id}')
        tp_lbl_h_lines.setGeometry(QtCore.QRect(10, 40, 31, 16))
        tp_lbl_h_lines.setObjectName(f'tp_lbl_h_lines_{widget_id}')

        setattr(self.ui, f'tp_lbl_v_lines_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_v_lines = getattr(self.ui, f'tp_lbl_v_lines_{widget_id}')
        tp_lbl_v_lines.setGeometry(QtCore.QRect(70, 40, 31, 16))
        tp_lbl_v_lines.setObjectName(f'tp_lbl_v_lines_{widget_id}')

        setattr(self.ui, f'tp_lbl_lines_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_lines = getattr(self.ui, f'tp_lbl_lines_{widget_id}')
        tp_lbl_lines.setGeometry(QtCore.QRect(10, 20, 121, 16))
        tp_lbl_lines.setObjectName(f'tp_lbl_lines_{widget_id}')

        setattr(self.ui, f'tp_sb_h_degrees_{widget_id}', QtWidgets.QSpinBox(tp_group))
        tp_sb_h_degrees = getattr(self.ui, f'tp_sb_h_degrees_{widget_id}')
        tp_sb_h_degrees.setGeometry(QtCore.QRect(20, 100, 42, 20))
        tp_sb_h_degrees.setMinimum(1)
        tp_sb_h_degrees.setMaximum(45)
        tp_sb_h_degrees.setProperty("value", 5)
        tp_sb_h_degrees.setObjectName(f'tp_sb_h_degrees_{widget_id}')

        setattr(self.ui, f'tp_lbl_v_degrees_{widget_id}',  QtWidgets.QLabel(tp_group))
        tp_lbl_v_degrees = getattr(self.ui, f'tp_lbl_v_degrees_{widget_id}')
        tp_lbl_v_degrees.setGeometry(QtCore.QRect(70, 100, 31, 16))
        tp_lbl_v_degrees.setObjectName(f'tp_lbl_v_degrees_{widget_id}')

        setattr(self.ui, f'tp_lbl_degrees_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_degrees = getattr(self.ui, f'tp_lbl_degrees_{widget_id}')
        tp_lbl_degrees.setGeometry(QtCore.QRect(10, 80, 111, 16))
        tp_lbl_degrees.setObjectName(f'tp_lbl_degrees_{widget_id}')

        setattr(self.ui, f'tp_sb_v_degrees_{widget_id}', QtWidgets.QSpinBox(tp_group))
        tp_sb_v_degrees = getattr(self.ui, f'tp_sb_v_degrees_{widget_id}')
        tp_sb_v_degrees.setGeometry(QtCore.QRect(80, 100, 42, 20))
        tp_sb_v_degrees.setMinimum(1)
        tp_sb_v_degrees.setMaximum(45)
        tp_sb_v_degrees.setProperty("value", 25)
        tp_sb_v_degrees.setObjectName(f'tp_sb_v_degrees_{widget_id}')

        setattr(self.ui, f'tp_lbl_h_degrees_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_h_degrees = getattr(self.ui, f'tp_lbl_h_degrees_{widget_id}')
        tp_lbl_h_degrees.setGeometry(QtCore.QRect(10, 100, 31, 16))
        tp_lbl_h_degrees.setObjectName(f'tp_lbl_h_degrees_{widget_id}')

        setattr(self.ui, f'tp_sb_w_size_{widget_id}', QtWidgets.QSpinBox(tp_group))
        tp_sb_w_size = getattr(self.ui, f'tp_sb_w_size_{widget_id}')
        tp_sb_w_size.setGeometry(QtCore.QRect(310, 100, 51, 20))
        tp_sb_w_size.setMinimum(100)
        tp_sb_w_size.setMaximum(1920)
        tp_sb_w_size.setProperty("value", 1200)
        tp_sb_w_size.setObjectName(f'tp_sb_w_size_{widget_id}')

        setattr(self.ui, f'tp_sb_h_size_{widget_id}', QtWidgets.QSpinBox(tp_group))
        tp_sb_h_size = getattr(self.ui, f'tp_sb_h_size_{widget_id}')
        tp_sb_h_size.setGeometry(QtCore.QRect(229, 100, 51, 20))
        tp_sb_h_size.setMinimum(100)
        tp_sb_h_size.setMaximum(1080)
        tp_sb_h_size.setProperty("value", 500)
        tp_sb_h_size.setObjectName(f'tp_sb_h_size_{widget_id}')

        setattr(self.ui, f'tp_lbl_size_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_size = getattr(self.ui, f'tp_lbl_size_{widget_id}')
        tp_lbl_size.setGeometry(QtCore.QRect(219, 80, 111, 16))
        tp_lbl_size.setObjectName(f'tp_lbl_size_{widget_id}')

        setattr(self.ui, f'tp_lbl_w_size_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_w_size = getattr(self.ui, f'tp_lbl_w_size_{widget_id}')
        tp_lbl_w_size.setGeometry(QtCore.QRect(289, 100, 31, 16))
        tp_lbl_w_size.setObjectName(f'tp_lbl_w_size_{widget_id}')

        setattr(self.ui, f'tp_lbl_h_size_{widget_id}', QtWidgets.QLabel(tp_group))
        tp_lbl_h_size = getattr(self.ui, f'tp_lbl_h_size_{widget_id}')
        tp_lbl_h_size.setGeometry(QtCore.QRect(219, 100, 31, 16))
        tp_lbl_h_size.setObjectName(f'tp_lbl_h_size_{widget_id}')

        _translate = QtCore.QCoreApplication.translate
        tp_group.setTitle(_translate("MainWindow", "Transformación de perspectiva"))
        tp_btn_clear.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))
        tp_btn_start.setToolTip(_translate("MainWindow", "<html><head/><body><p>Dibujar coordenadas</p></body></html>"))
        tp_btn_view.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ver imagen</p></body></html>"))
        tp_btn_delete.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))
        tp_lbl_h_lines.setText(_translate("MainWindow", "H"))
        tp_lbl_v_lines.setText(_translate("MainWindow", "V"))
        tp_lbl_lines.setText(_translate("MainWindow", "Tolerancias entre lineas"))
        tp_lbl_v_degrees.setText(_translate("MainWindow", "V"))
        tp_lbl_degrees.setText(_translate("MainWindow", "Tolerancias en grados"))
        tp_lbl_h_degrees.setText(_translate("MainWindow", "H"))
        tp_lbl_size.setText(_translate("MainWindow", "Tamaño perspectiva"))
        tp_lbl_w_size.setText(_translate("MainWindow", "W"))
        tp_lbl_h_size.setText(_translate("MainWindow", "H"))

        self.ui.formLayout.setWidget(widget_id, QtWidgets.QFormLayout.FieldRole, tp_group)

        # Conexiones
        tp_btn_start.clicked.connect(lambda callback: self.execute_perspective_transform())
        tp_sb_h_lines.valueChanged.connect(lambda callback: self.update_parameters())
        tp_sb_v_lines.valueChanged.connect(lambda callback: self.update_parameters())
        tp_sb_h_degrees.valueChanged.connect(lambda callback: self.update_parameters())
        tp_sb_v_degrees.valueChanged.connect(lambda callback: self.update_parameters())
        tp_sb_h_size.valueChanged.connect(lambda callback: self.update_parameters())
        tp_sb_w_size.valueChanged.connect(lambda callback: self.update_parameters())

    def update_parameters(self):
        """
        Actualización de parametros
        :return:
        """
        tp_sb_h_lines = getattr(self.ui, f'tp_sb_h_lines_{self.widget_id}')
        tp_sb_v_lines = getattr(self.ui, f'tp_sb_v_lines_{self.widget_id}')
        tp_sb_h_degrees = getattr(self.ui, f'tp_sb_h_degrees_{self.widget_id}')
        tp_sb_v_degrees = getattr(self.ui, f'tp_sb_v_degrees_{self.widget_id}')
        tp_sb_h_size = getattr(self.ui, f'tp_sb_h_size_{self.widget_id}')
        tp_sb_w_size = getattr(self.ui, f'tp_sb_w_size_{self.widget_id}')

        self.tp_height = int(tp_sb_h_size.value())
        self.tp_width = int(tp_sb_w_size.value())
        self.vertical_degrees = int(tp_sb_v_degrees.value())
        self.horizontal_degrees = int(tp_sb_h_degrees.value())
        self.horizontal_tolerance = int(tp_sb_h_lines.value())
        self.vertical_tolerance = int(tp_sb_v_lines.value())

    def get_lines(self, transformed, tolerance):

        #cv2.imshow(f"Antes de Canny_th{int(random() *10000)}", transformed)
        # Aplica algoritmos de detección de bordes
        image_canny = cv2.Canny(transformed, 0, 100, 0)
        #cv2.imshow(f"Canny_th{int(random() *10000)}", image_canny)
        lines = cv2.HoughLines(image_canny, 1, np.pi / 180, tolerance)

        verticals = []
        horizontals = []

        if lines is not None:

            max_size = max([self.tp_height, self.tp_width])

            for l in lines:
                for rho, theta in l:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    x1 = int(x0 + max_size * (-b))
                    y1 = int(y0 + max_size * (a))
                    x2 = int(x0 - max_size * (-b))
                    y2 = int(y0 - max_size * (a))

                    angle = theta * 180 / np.pi
                    magnitude = abs(int(rho))

                    # Vertical lines
                    if (((360 - self.vertical_degrees) < angle and angle < self.vertical_degrees)) or (
                    ((-1 * self.vertical_degrees) < angle and angle < self.vertical_degrees)) or (
                    ((180 - self.vertical_degrees) < angle and angle < 180 + self.vertical_degrees)):

                        if rho < 0:
                            theta = theta - np.pi
                            rho = -1 * rho

                        cv2.line(transformed, (x1, y1), (x2, y2), (0, 0, 255), 1)
                        verticals.append({'angle': angle, 'magnitude': magnitude, 'rho': rho, 'theta': theta})

                        # Horizontal lines
                    elif (((90 - self.horizontal_degrees) < angle and angle < (90 + self.horizontal_degrees))) or (
                    ((270 - self.horizontal_degrees) < angle and angle < (270 + self.horizontal_degrees))):

                        cv2.line(transformed, (x1, y1), (x2, y2), (255, 0, 255), 1)
                        horizontals.append({'angle': angle, 'magnitude': magnitude, 'rho': rho, 'theta': theta})

                    verticals = sorted(verticals, key=lambda i: i['magnitude'])
                    horizontals = sorted(horizontals, key=lambda i: i['magnitude'])

            #cv2.imshow(f"Hough_th{int(random() * 10000)}", transformed)

        return verticals, horizontals

    def execute_perspective_transform(self):
        """
        Realiza la detección de espacios de parqueo según se requiere
        :return:
        """
        mask = None
        cont = 0

        for c in self.coordinates[0]:

            tc = np.float32([c[0], c[1], c[3], c[2]])
            is_horizontal = True

            if TPerspective.is_horizontal(tc):
                perspective_zone = np.float32([[0, 0], [self.tp_width, 0], [0, self.tp_height], [self.tp_width, self.tp_height]])
                m = cv2.getPerspectiveTransform(tc, perspective_zone)
                m_inverse = cv2.getPerspectiveTransform(perspective_zone, tc)
                transformed = cv2.warpPerspective(self.picture, m, (self.tp_width, self.tp_height))
                _, binary = cv2.threshold(transformed, 200, 255, cv2.THRESH_BINARY)
            else:
                is_horizontal = False
                perspective_zone = np.float32([[0, 0], [self.tp_height, 0], [0, self.tp_width], [self.tp_height, self.tp_width]])
                m = cv2.getPerspectiveTransform(tc, perspective_zone)
                m_inverse = cv2.getPerspectiveTransform(perspective_zone, tc)
                transformed_no_rotated = cv2.warpPerspective(self.picture, m, (self.tp_height, self.tp_width))
                transformed = np.rot90(transformed_no_rotated, k=1)
                transformed = transformed.copy()
                _, binary = cv2.threshold(transformed, 200, 255, cv2.THRESH_BINARY)

            cont += 1

            # Generación y clasificación de lineas
            verticals, horizontals = self.get_lines(transformed, 120)
            verticals_filtered = self.get_classified_lines_by_rho(verticals, self.vertical_tolerance, transformed, False)
            horizontals_filtered = self.get_classified_lines_by_rho(horizontals, self.horizontal_tolerance, transformed, True)

            verticals_filtered = self.filter_bad_distances(verticals_filtered, 0.5, 0.9, transformed)

            # Imagen inversa en perspectiva
            empty_image = np.zeros((self.tp_height, self.tp_width, 3), np.uint8)

            # Dibuja lineas
            TPerspective.draw_lines(empty_image, verticals_filtered, (255, 255, 255), 15, cont)
            TPerspective.draw_lines(empty_image, horizontals_filtered, (255, 255, 255), 15, cont)

            # Detección de contornos
            empty_image_bw = cv2.cvtColor(empty_image, cv2.COLOR_BGR2GRAY)
            _, empty_image_bin = cv2.threshold(empty_image_bw, 100, 255, cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(empty_image_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Encuentra los contornos:
            internal_contours = []

            # Filtra contornos hijos:
            for i in range(len(contours)):
                if hierarchy[0][i][3] == 0:
                    internal_contours.append(contours[i])

            # Formatea la imagen vacía de nuevo para dibujar contornos limpios
            empty_image = np.zeros((self.tp_height, self.tp_width, 3), np.uint8)

            if len(internal_contours) > 0:
                cv2.drawContours(empty_image, internal_contours, -1, (0, 255, 0), cv2.FILLED)

            # Gira en caso de ser vertical.
            if not is_horizontal:
                empty_image = np.rot90(empty_image, k=-1)

            # Reversa la perspectiva
            back_perspective = cv2.warpPerspective(empty_image, m_inverse, (1919, 1079))

            # Genera la mascara
            back_perspective_gray = cv2.cvtColor(back_perspective, cv2.COLOR_BGR2GRAY)
            _, back_perspective_bin = cv2.threshold(back_perspective_gray, 100, 255, cv2.THRESH_BINARY)

            if mask is None:
                mask = back_perspective_bin
            else:
                mask = cv2.bitwise_or(back_perspective_bin, mask)

            cv2.imshow(f'{cont}_Pruebas perspectiva', mask)

        self.mask = mask

    @staticmethod
    def draw_lines(image, lines: list, color: tuple, thickness: int, counter: int):
        """
        Dibuja lineas en la imagen
        :param image:
        :param lines:
        :param color:
        :param thickness:
        :param counter:
        :return:
        """
        for line in lines:
            cv2.line(image, (line['x1'], line['y1']), (line['x2'], line['y2']), color, thickness)

        #cv2.imshow(f'{counter}_Nueva perspectiva', image)

    def get_classified_lines_by_rho(self, lines: list, tolerance: int, image, is_horizontal: bool):

        clusters = []
        final = []
        base = [lines[0]]
        max_size = max([self.tp_height, self.tp_width])

        for i in range(1, len(lines)):

            d = abs(lines[i]["magnitude"] - lines[i - 1]["magnitude"])

            if d < tolerance:
                base.append(lines[i])
            else:
                clusters.append(base)
                base = [lines[i]]

                # Punto final
            if i == len(lines) - 1:
                clusters.append(base)

        # if is_horizontal:
        #     pass
        #     clusters = filter(lambda x: (len(x) > 5), clusters)

        # Calculate mean
        for c in clusters:

            rho = 0
            theta = 0

            for l in c:

                if is_horizontal:
                    rho += l['rho']
                    theta += l['theta']
                else:

                    radianes_vertical = self.vertical_degrees * np.pi / 180

                    if np.pi - radianes_vertical < theta < radianes_vertical + np.pi:
                        l['rho'] = -1 * l['rho']
                        l['theta'] = l['theta'] - np.pi
                    elif (2 * np.pi) - radianes_vertical < theta < radianes_vertical:
                        l['theta'] = l['theta'] - (2 * np.pi)

                    rho += l['rho']
                    theta += l['theta']

            rho = rho / len(c)
            theta = theta / len(c)

            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + max_size * (-b))
            y1 = int(y0 + max_size * a)
            x2 = int(x0 - max_size * (-b))
            y2 = int(y0 - max_size * a)

            # Calcula la linea equivalente
            final.append({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'rho': rho, 'theta': theta})
            # cv2.line(image, (x1, y1), (x2, y2), (255, 125, 125), 15)

        return final

    def filter_bad_distances(self, clusters: list, percent_1: float, percent_2: float, image):

        distances_1 = []

        for i in range(len(clusters) - 1):
            distances_1.append(abs(clusters[i]['rho'] - clusters[i + 1]['rho']))

        median_1 = np.median(distances_1)

        bad_distances_1 = [d[0] for d in enumerate(distances_1) if d[1] < (percent_1 * median_1)]
        filtered_clusters_1 = [c[1] for c in enumerate(clusters) if c[0] not in bad_distances_1]

        distances_2 = []
        for i in range(len(filtered_clusters_1) - 1):
            distances_2.append(abs(filtered_clusters_1[i]['rho'] - filtered_clusters_1[i + 1]['rho']))

        median_2 = np.median(distances_2)

        clustes_distances = []

        for i in range(len(clusters)):

            # First
            if i == 0:
                d_left = median_2 * percent_2 + 1
                d_right = abs(clusters[i]['rho'] - clusters[i + 1]['rho'])
            # Last
            elif i == len(clusters) - 1:
                d_left = abs(clusters[i]['rho'] - clusters[i - 1]['rho'])
                d_right = median_2 * percent_2 + 1
            else:
                d_left = abs(clusters[i]['rho'] - clusters[i - 1]['rho'])
                d_right = abs(clusters[i]['rho'] - clusters[i + 1]['rho'])

            clustes_distances.append({'rho': clusters[i]['rho'], 'd_left': d_left, 'd_right': d_right})

        clustes_distances_filtered = [c for c in clustes_distances if
                                      c['d_right'] < (percent_2 * median_2) and c['d_left'] < (percent_2 * median_2)]
        clusters_to_return = []

        for cl in clusters:
            if cl['rho'] not in [cl['rho'] for cl in clustes_distances_filtered]:
                clusters_to_return.append(cl)
                cv2.line(image, (cl['x1'], cl['y1']), (cl['x2'], cl['y2']), (255, 125, 125), 15)

        return clusters_to_return

    def set_original_picture(self, picture):
        self._original_picture = copy.deepcopy(picture)

    def get_original_picture(self):
        return copy.deepcopy(self._original_picture)

    @staticmethod
    def is_horizontal(coordinates):
        """
        :param coordinates:
        :return:
        """
        # Segmento 1 - 3
        d_x = abs(coordinates[0][0] - coordinates[2][0])
        d_y = abs(coordinates[0][1] - coordinates[2][1])
        s_13 = math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2))

        # Segmento 2 -4
        d_x = abs(coordinates[1][0] - coordinates[3][0])
        d_y = abs(coordinates[1][1] - coordinates[3][1])
        s_24 = math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2))

        # Segmento 1 - 2
        d_x = abs(coordinates[0][0] - coordinates[1][0])
        d_y = abs(coordinates[0][1] - coordinates[1][1])
        s_12 = math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2))

        # Segmento 3 - 4
        d_x = abs(coordinates[2][0] - coordinates[3][0])
        d_y = abs(coordinates[2][1] - coordinates[3][1])
        s_34 = math.sqrt(math.pow(d_x, 2) + math.pow(d_y, 2))

        # Medias
        hor = (s_12 + s_34) / 2
        ver = (s_13 + s_24) / 2

        if hor >= ver:
            return True
        else:
            return False

    def get_picture_filtered(self):

        # Convierte la mascara en RGB
        rgb_mask = cv2.cvtColor(self.mask, cv2.COLOR_GRAY2RGB)

        picture = Pic()
        picture.create_picture_from_content(rgb_mask)

        # Genera la capa filtrada con la mascara adecuada
        return picture


