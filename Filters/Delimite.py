import cv2
import numpy as np
import copy
from enum import Enum

from QTGraphicInterfaces.DynamicMainInterfaceForm import Ui_MainWindow as Ui
from PyQt5 import QtCore, QtWidgets, QtGui
from Filters.Filter import Filter
from Models.Picture import Picture as Pic
from Models.Utils import Utils as Ut


class DelimiteActions(Enum):
    Coordinates = 0,
    Color = 1


class Delimite(Filter):
    """
    Filtro que permite elegir específicamente zonas de una imagen para delimitar un estacionamiento
    """
    ui: Ui

    def __init__(self, picture: Pic, ui: Ui, row: int, col: int, widget_id: int):

        # Imagen original
        self._original_picture = None
        # Coordenadas de limites útiles en la imagen
        self.limits = [[]]
        # Mascaras de limites
        self.masks = []
        # Indica que el filtro fué finalizado
        self.is_done = False
        # Hereda el color de linea de un filtro anterior
        self.color = Ut.get_line_color()
        # Acción por defecto
        self.action = DelimiteActions.Coordinates
        self.set_original_picture(picture)
        self.picture = self.get_original_picture()
        self.ui = ui
        self.draw_widget(row, col, widget_id)
        self.widget_id = widget_id

    def set_visible(self, state):
        """
        Cambia la visibilidad de un filtro
        :param state:
        :return:
        """
        # Recupera el widget y aplica lógica
        group = getattr(self.ui, f'da_group_{self.widget_id}')
        group.setVisible(state)

    def draw_widget(self, row: int, col: int, widget_id: int):
        """
        Renderiza el widget del filtro en la pantalla
        :param row:
        :param col:
        :param widget_id:
        :return:
        """

        setattr(self.ui, f'da_group_{widget_id}', QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents))
        da_group = getattr(self.ui, f'da_group_{widget_id}')
        da_group.setMinimumSize(QtCore.QSize(0, 90))
        da_group.setObjectName(f'da_group_{widget_id}')

        setattr(self.ui, f'da_btn_color_{widget_id}', QtWidgets.QPushButton(da_group))
        da_btn_color = getattr(self.ui, f'da_btn_color_{widget_id}')
        da_btn_color.setGeometry(QtCore.QRect(10, 30, 40, 40))
        da_btn_color.setMinimumSize(QtCore.QSize(40, 40))
        da_btn_color.setMaximumSize(QtCore.QSize(40, 40))
        da_btn_color.setStyleSheet("border-color: rgb(255, 85, 0);")
        da_btn_color.setText("")
        icon_btn_color = QtGui.QIcon()
        icon_btn_color.addPixmap(QtGui.QPixmap("icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        da_btn_color.setIcon(icon_btn_color)
        da_btn_color.setIconSize(QtCore.QSize(32, 32))
        da_btn_color.setObjectName(f'da_btn_color_{widget_id}')

        setattr(self.ui, f'da_lbl_color_{widget_id}', QtWidgets.QLabel(da_group))
        da_lbl_color = getattr(self.ui, f'da_lbl_color_{widget_id}')
        da_lbl_color.setGeometry(QtCore.QRect(50, 30, 40, 40))
        da_lbl_color.setMinimumSize(QtCore.QSize(40, 40))
        da_lbl_color.setMaximumSize(QtCore.QSize(40, 40))
        da_lbl_color.setAutoFillBackground(False)
        da_lbl_color.setStyleSheet(f"background: rgb({self.color['r']}, {self.color['g']}, {self.color['b']});\n"
                                        "border: 1px solid gray;")
        da_lbl_color.setText("")
        da_lbl_color.setObjectName(f'da_lbl_color_{widget_id}')

        setattr(self.ui, f'da_btn_clear_{widget_id}', QtWidgets.QPushButton(da_group))
        da_btn_clear = getattr(self.ui, f'da_btn_clear_{widget_id}')
        da_btn_clear.setGeometry(QtCore.QRect(300, 30, 40, 40))
        da_btn_clear.setMinimumSize(QtCore.QSize(40, 40))
        da_btn_clear.setMaximumSize(QtCore.QSize(40, 40))
        da_btn_clear.setText("")
        icon_btn_clear = QtGui.QIcon()
        icon_btn_clear.addPixmap(QtGui.QPixmap("icons/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        da_btn_clear.setIcon(icon_btn_clear)
        da_btn_clear.setIconSize(QtCore.QSize(32, 32))
        da_btn_clear.setObjectName(f'da_btn_clear_{widget_id}')

        setattr(self.ui, f'da_btn_coordinates_{widget_id}', QtWidgets.QPushButton(da_group))
        da_btn_coordinates = getattr(self.ui, f'da_btn_coordinates_{widget_id}')
        da_btn_coordinates.setGeometry(QtCore.QRect(90, 30, 40, 40))
        da_btn_coordinates.setMinimumSize(QtCore.QSize(40, 40))
        da_btn_coordinates.setMaximumSize(QtCore.QSize(40, 40))
        da_btn_coordinates.setStyleSheet("border-color: rgb(255, 85, 0);")
        da_btn_coordinates.setText("")
        icon_da_btn_coordinates = QtGui.QIcon()
        icon_da_btn_coordinates.addPixmap(QtGui.QPixmap("icons/coordenadas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        da_btn_coordinates.setIcon(icon_da_btn_coordinates)
        da_btn_coordinates.setIconSize(QtCore.QSize(32, 32))
        da_btn_coordinates.setObjectName(f'da_btn_coordinates_{widget_id}')

        setattr(self.ui, f'da_btn_view_{widget_id}', QtWidgets.QPushButton(da_group))
        da_btn_view = getattr(self.ui, f'da_btn_view_{widget_id}')
        da_btn_view.setGeometry(QtCore.QRect(260, 30, 40, 40))
        da_btn_view.setMinimumSize(QtCore.QSize(40, 40))
        da_btn_view.setMaximumSize(QtCore.QSize(40, 40))
        da_btn_view.setText("")
        icon_da_btn_view = QtGui.QIcon()
        icon_da_btn_view.addPixmap(QtGui.QPixmap("icons/ver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        da_btn_view.setIcon(icon_da_btn_view)
        da_btn_view.setIconSize(QtCore.QSize(32, 32))
        da_btn_view.setObjectName(f'da_btn_view_{widget_id}')

        setattr(self.ui, f'da_btn_delete_{widget_id}', QtWidgets.QPushButton(da_group))
        da_btn_delete = getattr(self.ui, f'da_btn_delete_{widget_id}')
        da_btn_delete.setGeometry(QtCore.QRect(340, 30, 40, 40))
        da_btn_delete.setMinimumSize(QtCore.QSize(40, 40))
        da_btn_delete.setMaximumSize(QtCore.QSize(40, 40))
        da_btn_delete.setText("")
        icon_da_btn_delete = QtGui.QIcon()
        icon_da_btn_delete.addPixmap(QtGui.QPixmap("icons/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        da_btn_delete.setIcon(icon_da_btn_delete)
        da_btn_delete.setIconSize(QtCore.QSize(32, 32))
        da_btn_delete.setObjectName(f'da_btn_delete_{widget_id}')

        _translate = QtCore.QCoreApplication.translate

        da_group.setTitle(_translate("MainWindow", "Delimitación de areas"))
        da_btn_clear.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))
        da_btn_coordinates.setToolTip(_translate("MainWindow", "<html><head/><body><p>Dibujar coordenadas</p></body></html>"))
        da_btn_view.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ver imagen</p></body></html>"))
        da_btn_delete.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))

        self.ui.formLayout.setWidget(widget_id, QtWidgets.QFormLayout.FieldRole, da_group)

        # Conexiones
        da_btn_coordinates.clicked.connect(lambda callback: self.set_action_button(DelimiteActions.Coordinates))
        da_btn_color.clicked.connect(lambda callback: self.set_action_button(DelimiteActions.Color))
        da_btn_clear.clicked.connect(self.clean)
        da_btn_view.clicked.connect(self.view_zones)

    def get_pixel_values(self, x, y):
        """
            Extrae valores RGB y HSV de una imagen especificada para una coordenada
        """
        # Extrae canales de forma independiente
        b_ex, g_ex, r_ex = self.picture[:, :, 0], self.picture[:, :, 1], self.picture[:, :, 2]

        r_val = r_ex[y][x]
        g_val = g_ex[y][x]
        b_val = b_ex[y][x]

        # Conforma imagen rgb de 1px * 1px
        rgb = np.array([[[r_val, g_val, b_val]]])
        # Convierte el espacio de color H: 0 -> 179, S: 0 -> 255, V: -> 0 -> 255
        hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
        # Extrae valores pixel a pixel
        h_val = hsv[0][0][0]
        s_val = hsv[0][0][1]
        v_val = hsv[0][0][2]

        return r_val, g_val, b_val, h_val, s_val, v_val

    def open_image(self):
        """
        Abre la imagen lista para dibujar
        :return:
        """
        try:
            cv2.imshow(f'{self.widget_id}_Delimitar', self.picture)
            # Callback de eventos de mouse
            cv2.setMouseCallback(f'{self.widget_id}_Delimitar', self.mouse_callback)
        except Exception as ex:
            raise Exception(ex)

    def mouse_callback(self, event, x, y, flags, param):
        """
        Callback para eventos mouse encargado de gestionar el dibujo de formas
        :param event:
        :param x:
        :param y:
        :param flags:
        :param param:
        :return:
        """

        if self.action == DelimiteActions.Coordinates:

            if event == cv2.EVENT_LBUTTONDOWN:
                # Cada punto dibujado es una coordenada almacenada y dibujada
                self.add_limit_coordinate(x, y, is_last=False)
                cv2.circle(self.picture, (x, y), 3, (int(self.color['b']), int(self.color['g']), int(self.color['r'])),
                           -1)
                # Actualiza la imagen mostrada
                cv2.imshow(f'{self.widget_id}_Delimitar', self.picture)

                # Crea una zona delimitada
                if len(self.limits[-1]) > 3:
                    # Extrae los contornos
                    contours = np.array([self.limits[-1]])
                    # Cierra el contorno
                    self.add_close_last_limit()
                    # Crear una mascara genérica del mismo tamaño de la imagen
                    mask = np.zeros(shape=(self.picture.shape[:2]), dtype=np.uint8)
                    # Itera por los contornos y crea la mascara
                    mask = cv2.drawContours(mask, contours, -1, 255, -1)
                    # Almacena la mascara en la imagen
                    self.masks.append(mask)

                    # Dibuja el contorno en la imagen original
                    cv2.drawContours(self.picture, contours, -1,
                                     (int(self.color['b']), int(self.color['g']), int(self.color['r'])), 4)
                    # Muestra el contorno
                    cv2.imshow(f'{self.widget_id}_Delimitar', self.picture)

        elif self.action == DelimiteActions.Color:
            if event == cv2.EVENT_LBUTTONDBLCLK:
                # Extrae valores de pixel de la imagen
                r, g, b, h, s, v = self.get_pixel_values(x, y)
                # Actualiza el color
                self.color['r'] = r
                self.color['g'] = g
                self.color['b'] = b

                # Almacena el color en memoria estática
                Ut.set_line_color(r, g, b)

                # Visualiza el color extraído en el label
                da_lbl_color = getattr(self.ui, f'da_lbl_color_{self.widget_id}')
                da_lbl_color.setStyleSheet(f"background: rgb({r}, {g}, {b} );\n""border: 1px solid black;")
        else:
            pass

    def set_action_button(self, action):
        """
        Setter del atributo acción usado en callbacks
        :param action:
        :return:
        """
        self.action = action

        # Consulta los botones
        da_btn_color = getattr(self.ui, f'da_btn_color_{self.widget_id}')
        da_btn_coordinates = getattr(self.ui, f'da_btn_coordinates_{self.widget_id}')

        # Modificación de bordes en botones
        if action == DelimiteActions.Coordinates:
            da_btn_color.setStyleSheet("")
            da_btn_coordinates.setStyleSheet("background-color: rgb(109, 255, 231);")
        elif action == DelimiteActions.Color:
            da_btn_color.setStyleSheet("background-color: rgb(109, 255, 231);")
            da_btn_coordinates.setStyleSheet("")

        self.open_image()

    def draw_points_callback(self, event, x, y, flags, param):
        """
        Callback para eventos mouse encargado de gestionar el dibujo de contornos
        :param event:
        :param x:
        :param y:
        :param flags:
        :param param:
        :return:
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            # Cada punto dibujado es una coordenada almacenada y dibujada
            self.add_limit_coordinate(x, y, is_last=False)
            cv2.circle(self.picture, (x, y), 3, (int(self.color['r']), int(self.color['g']), int(self.color['b'])), -1)
            # Actualiza la imagen mostrada
            cv2.imshow(f'{self.widget_id}_Dibujando imagen...', self.picture)

        # control + click añade una nueva zona delimitada
        elif event == cv2.EVENT_MBUTTONDBLCLK:

            # Crea una zona delimitada
            if len(self.limits[-1]) > 3:
                # Extrae los contornos
                contours = np.array([self.limits[-1]])
                # Cierra el contorno
                self.add_close_last_limit()
                # Crear una mascara genérica del mismo tamaño de la imagen
                mask = np.zeros(shape=(self.picture.shape[:2]), dtype=np.uint8)
                # Itera por los contornos y crea la mascara
                mask = cv2.drawContours(mask, contours, -1, 255, -1)
                # Almacena la mascara en la imagen
                self.masks.append(mask)
                # Dibuja el contorno en la imagen original
                cv2.drawContours(self.picture, contours, -1,
                                 (int(self.color['r']), int(self.color['g']), int(self.color['b'])), 2)
                # Muestra el contorno
                cv2.imshow(f'{self.widget_id}_Dibujando imagen...', self.picture)

    def view_zones(self):
        """
        Visualiza el resultado del filtro
        :return:
        """
        cv2.imshow(f'{self.widget_id}_Zonas delimitadas', self.get_picture_filtered().content)

    def clean(self):
        """
        Limpieza de las zonas en el objeto imagen y en la interfaz gráfica
        :return:
        """
        self.limits = [[]]
        self.masks = []
        self.picture = self.get_original_picture()
        self.open_image()

    def add_limit_coordinate(self, x, y, is_last):

        """
        Añade grupos de coordenadas a los límites definidos en la imagen
        :param x: coordenada x
        :param y: coordenada y
        :param is_last: si la coordenada cierra la figura se debe indicar
        :return: void
        """
        # Extrae el indice para insertar los registros
        index = len(self.limits) - 1
        # Añade las coordenadas en los límites
        self.limits[index].append([x, y])

    def get_all_masks_limits(self):

        """
        Retorna todas las mascaras unificadas para concatenar con la imagen real
        :return: mask
        """
        # Crear una mascara genérica del mismo tamaño de la imagen
        mask = np.zeros(shape=(self.picture.shape[:2]), dtype=np.uint8)

        # Itera y concatena las mascaras
        for m in self.masks:
            mask = cv2.bitwise_or(m, mask)

        return mask

    def add_close_last_limit(self):

        """
        Cierra la ultima coordenada
        :return:
        """

        self.limits.append([])

    def get_picture_filtered(self):
        """
        Genera el resultado del filtro aplicado
        :return:
        """
        mask = self.get_all_masks_limits()

        picture = Pic()
        # Sin bordes
        # image_with_contours = cv2.bitwise_and(self.get_original_picture(), self.get_original_picture(), mask=mask)
        image_with_contours = cv2.bitwise_and(self.picture, self.picture, mask=mask)
        picture.create_picture_from_content(image_with_contours)

        # Genera la capa filtrada con la mascara adecuada
        return picture

    def set_original_picture(self, picture):
        self._original_picture = copy.deepcopy(picture)

    def get_original_picture(self):
        return copy.deepcopy(self._original_picture)

    def get_coordinates(self):
        """
        Extracción de coordenadas delimitadas
        :return:
        """
        return [l for l in self.limits if len(l) > 0]
