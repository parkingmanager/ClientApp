import cv2
import numpy as np
import copy
from enum import Enum


from QTGraphicInterfaces.DynamicMainInterfaceForm import Ui_MainWindow as Ui
from PyQt5 import QtCore, QtWidgets, QtGui
from Filters.Filter import Filter
from Models.Picture import Picture as Pic
from Models.Utils import Utils as Ut


class TransformActions(Enum):
    Line = 0,
    Eraser = 1,
    ColorPick = 2


class Transform(Filter):
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
        # Grosor de herramienta
        self.thickness = 3
        # Acción por defecto
        self.action = None
        # Ultimo evento de mouse
        self.last_mouse_event = None

        self.set_original_picture(picture)
        self.picture = self.get_original_picture()
        self.ui = ui
        self.draw_widget(row, col, widget_id)
        self.widget_id = widget_id

        self.open_image()

        # Lineas
        self.line_coordinates = [None, None]

    def set_visible(self, state):
        """
        Cambia la visibilidad de un filtro
        :param state:
        :return:
        """
        # Recupera el widget y aplica lógica
        group = getattr(self.ui, f'tl_group_{self.widget_id}')
        group.setVisible(state)

    def draw_widget(self, row: int, col: int, widget_id: int):
        """
        Renderiza el widget del filtro en la pantalla
        :param row:
        :param col:
        :param widget_id:
        :return:
        """

        setattr(self.ui, f'tl_group_{widget_id}', QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents))
        tl_group = getattr(self.ui, f'tl_group_{widget_id}')
        # tl_group.setGeometry(QtCore.QRect(10, 10, 391, 81))
        tl_group.setMinimumSize(QtCore.QSize(0, 90))
        tl_group.setObjectName(f'tl_group_{widget_id}')

        setattr(self.ui, f'tl_btn_clear_{widget_id}', QtWidgets.QPushButton(tl_group))
        tl_btn_clear = getattr(self.ui, f'tl_btn_clear_{widget_id}')
        tl_btn_clear.setGeometry(QtCore.QRect(300, 30, 40, 40))
        tl_btn_clear.setMinimumSize(QtCore.QSize(40, 40))
        tl_btn_clear.setMaximumSize(QtCore.QSize(40, 40))
        tl_btn_clear.setText("")
        icon_btn_clear = QtGui.QIcon()
        icon_btn_clear.addPixmap(QtGui.QPixmap("icons/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tl_btn_clear.setIcon(icon_btn_clear)
        tl_btn_clear.setIconSize(QtCore.QSize(32, 32))
        tl_btn_clear.setObjectName(f'tl_btn_clear_{widget_id}')

        setattr(self.ui, f'tl_btn_lines_{widget_id}', QtWidgets.QPushButton(tl_group))
        tl_btn_lines = getattr(self.ui, f'tl_btn_lines_{widget_id}')
        tl_btn_lines.setGeometry(QtCore.QRect(10, 30, 40, 40))
        tl_btn_lines.setMinimumSize(QtCore.QSize(40, 40))
        tl_btn_lines.setMaximumSize(QtCore.QSize(40, 40))
        tl_btn_lines.setStyleSheet("border-color: rgb(255, 85, 0);")
        tl_btn_lines.setText("")
        icon_btn_lines = QtGui.QIcon()
        icon_btn_lines.addPixmap(QtGui.QPixmap("icons/lineas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tl_btn_lines.setIcon(icon_btn_lines)
        tl_btn_lines.setIconSize(QtCore.QSize(32, 32))
        tl_btn_lines.setObjectName(f'tl_btn_lines_{widget_id}')

        setattr(self.ui, f'tl_btn_eraser_{widget_id}', QtWidgets.QPushButton(tl_group))
        tl_btn_eraser = getattr(self.ui, f'tl_btn_eraser_{widget_id}')
        tl_btn_eraser.setGeometry(QtCore.QRect(50, 30, 40, 40))
        tl_btn_eraser.setMinimumSize(QtCore.QSize(40, 40))
        tl_btn_eraser.setMaximumSize(QtCore.QSize(40, 40))
        tl_btn_eraser.setStyleSheet("border-color: rgb(255, 85, 0);")
        tl_btn_eraser.setText("")
        icon_btn_eraser = QtGui.QIcon()
        icon_btn_eraser.addPixmap(QtGui.QPixmap("icons/borrador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tl_btn_eraser.setIcon(icon_btn_eraser)
        tl_btn_eraser.setIconSize(QtCore.QSize(36, 36))
        tl_btn_eraser.setObjectName(f'tl_btn_eraser_{widget_id}')

        setattr(self.ui, f'tl_btn_color_{widget_id}', QtWidgets.QPushButton(tl_group))
        tl_btn_color = getattr(self.ui, f'tl_btn_color_{widget_id}')
        tl_btn_color.setGeometry(QtCore.QRect(90, 30, 40, 40))
        tl_btn_color.setMinimumSize(QtCore.QSize(40, 40))
        tl_btn_color.setMaximumSize(QtCore.QSize(40, 40))
        tl_btn_color.setText("")
        icon_btn_color = QtGui.QIcon()
        icon_btn_color.addPixmap(QtGui.QPixmap("icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tl_btn_color.setIcon(icon_btn_color)
        tl_btn_color.setIconSize(QtCore.QSize(32, 32))
        tl_btn_color.setObjectName(f'tl_btn_color_{widget_id}')

        setattr(self.ui, f'tl_btn_view_{widget_id}', QtWidgets.QPushButton(tl_group))
        tl_btn_view = getattr(self.ui, f'tl_btn_view_{widget_id}')
        tl_btn_view.setGeometry(QtCore.QRect(260, 30, 40, 40))
        tl_btn_view.setMinimumSize(QtCore.QSize(40, 40))
        tl_btn_view.setMaximumSize(QtCore.QSize(40, 40))
        tl_btn_view.setText("")
        icon_btn_view = QtGui.QIcon()
        icon_btn_view.addPixmap(QtGui.QPixmap("icons/ver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tl_btn_view.setIcon(icon_btn_view)
        tl_btn_view.setIconSize(QtCore.QSize(32, 32))
        tl_btn_view.setObjectName(f'tl_btn_view_{widget_id}')

        setattr(self.ui, f'tl_lbl_color_{widget_id}', QtWidgets.QLabel(tl_group))
        tl_lbl_color = getattr(self.ui, f'tl_lbl_color_{widget_id}')
        tl_lbl_color.setGeometry(QtCore.QRect(130, 30, 38, 38))
        tl_lbl_color.setMinimumSize(QtCore.QSize(38, 38))
        tl_lbl_color.setMaximumSize(QtCore.QSize(38, 38))
        tl_lbl_color.setAutoFillBackground(False)
        tl_lbl_color.setStyleSheet(f"background: rgb({self.color['r']}, {self.color['g']}, {self.color['b']});\n"
                                   "border: 1px solid gray;")
        tl_lbl_color.setText("")
        tl_lbl_color.setObjectName(f'tl_lbl_color_{widget_id}')

        setattr(self.ui, f'tl_sld_thickness_{widget_id}', QtWidgets.QSlider(tl_group))
        tl_sld_thickness = getattr(self.ui, f'tl_sld_thickness_{widget_id}')
        tl_sld_thickness.setGeometry(QtCore.QRect(180, 30, 16, 31))
        tl_sld_thickness.setOrientation(QtCore.Qt.Vertical)
        tl_sld_thickness.setObjectName(f'tl_sld_thickness_{widget_id}')
        tl_sld_thickness.setMinimum(1)
        tl_sld_thickness.setMaximum(20)

        setattr(self.ui, f'tl_lbl_thickness_{widget_id}', QtWidgets.QLabel(tl_group))
        tl_lbl_thickness = getattr(self.ui, f'tl_lbl_thickness_{widget_id}')
        tl_lbl_thickness.setGeometry(QtCore.QRect(210, 40, 31, 16))
        tl_lbl_thickness.setObjectName(f'tl_lbl_thickness_{widget_id}')

        setattr(self.ui, f'tl_btn_delete_{widget_id}', QtWidgets.QPushButton(tl_group))
        tl_btn_delete = getattr(self.ui, f'tl_btn_delete_{widget_id}')
        tl_btn_delete.setGeometry(QtCore.QRect(340, 30, 40, 40))
        tl_btn_delete.setMinimumSize(QtCore.QSize(40, 40))
        tl_btn_delete.setMaximumSize(QtCore.QSize(40, 40))
        tl_btn_delete.setText("")
        icon_btn_delete = QtGui.QIcon()
        icon_btn_delete.addPixmap(QtGui.QPixmap("icons/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tl_btn_delete.setIcon(icon_btn_delete)
        tl_btn_delete.setIconSize(QtCore.QSize(32, 32))
        tl_btn_delete.setObjectName(f'tl_btn_delete_{widget_id}')

        _translate = QtCore.QCoreApplication.translate

        tl_group.setTitle(_translate("MainWindow", "Transformación libre"))
        tl_lbl_thickness.setText(_translate("MainWindow", f"{self.thickness}"))
        tl_btn_delete.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))

        # self.ui.gridLayout.addWidget(tl_frame, row, col, 1, 1)
        self.ui.formLayout.setWidget(widget_id, QtWidgets.QFormLayout.FieldRole, tl_group)

        # Conexiones
        tl_btn_lines.clicked.connect(lambda callback: self.set_action_button(TransformActions.Line))
        tl_btn_eraser.clicked.connect(lambda callback: self.set_action_button(TransformActions.Eraser))
        tl_btn_color.clicked.connect(lambda callback: self.set_action_button(TransformActions.ColorPick))
        tl_sld_thickness.sliderReleased.connect(self.change_thickness)
        tl_btn_clear.clicked.connect(self.clean)
        tl_btn_view.clicked.connect(self.open_image)

    def change_thickness(self):
        """
        Evento de cambio de valor del slider
        :return:
        """
        tl_sld_thickness = getattr(self.ui, f'tl_sld_thickness_{self.widget_id}')
        tl_lbl_thickness = getattr(self.ui, f'tl_lbl_thickness_{self.widget_id}')
        self.thickness = tl_sld_thickness.value()
        tl_lbl_thickness.setText(f"{self.thickness}")

    def open_image(self):
        """
        Abre la imagen lista para dibujar
        :return:
        """
        try:
            cv2.imshow(f'{self.widget_id}_Dibujando imagen...', self.picture)
            # Callback de eventos de mouse
            cv2.setMouseCallback(f'{self.widget_id}_Dibujando imagen...', self.mouse_callback)
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
        # Dependiendo de la action:
        if self.action == TransformActions.Line:

            # Inicia el ciclo y almacena el valor
            if event == cv2.EVENT_LBUTTONDOWN:
                self.last_mouse_event = cv2.EVENT_LBUTTONDOWN
                self.line_coordinates[0] = [x, y]

            # Previo un down click dibuja
            elif event == cv2.EVENT_MOUSEMOVE and self.last_mouse_event == cv2.EVENT_LBUTTONDOWN:

                # Saca una copia de la imagen
                picture = copy.deepcopy(self.picture)

                cv2.line(picture, (self.line_coordinates[0][0], self.line_coordinates[0][1]), (x, y),
                         (int(self.color['b']), int(self.color['g']), int(self.color['r'])), self.thickness)
                cv2.imshow(f'{self.widget_id}_Dibujando imagen...', picture)

            # Libera el last event y el drag
            elif event == cv2.EVENT_LBUTTONUP:
                self.last_mouse_event = None
                cv2.line(self.picture, (self.line_coordinates[0][0], self.line_coordinates[0][1]), (x, y),
                         (int(self.color['b']), int(self.color['g']), int(self.color['r'])), self.thickness)
                cv2.imshow(f'{self.widget_id}_Dibujando imagen...', self.picture)
                self.line_coordinates = [None, None]

        elif self.action == TransformActions.Eraser:
            # Inicia el ciclo y almacena el valor
            if event == cv2.EVENT_LBUTTONDOWN:
                self.last_mouse_event = cv2.EVENT_LBUTTONDOWN
                cv2.circle(self.picture, (x, y), 1, (int(self.color['b']), int(self.color['g']), int(self.color['r'])), self.thickness)
                cv2.imshow(f'{self.widget_id}_Dibujando imagen...', self.picture)

            # Previo un down click dibuja
            elif event == cv2.EVENT_MOUSEMOVE and self.last_mouse_event == cv2.EVENT_LBUTTONDOWN:

                # Saca una copia de la imagen
                picture = copy.deepcopy(self.picture)

                cv2.circle(self.picture, (x, y), 1, (int(self.color['b']), int(self.color['g']), int(self.color['r'])),
                           self.thickness)
                cv2.imshow(f'{self.widget_id}_Dibujando imagen...', picture)

            # Libera el last event y el drag
            elif event == cv2.EVENT_LBUTTONUP:
                self.last_mouse_event = None
                cv2.circle(self.picture, (x, y), 1, (int(self.color['b']), int(self.color['g']), int(self.color['r'])),
                           self.thickness)
                cv2.imshow(f'{self.widget_id}_Dibujando imagen...', self.picture)

        elif self.action == TransformActions.ColorPick:
            if event == cv2.EVENT_LBUTTONDBLCLK:
                # Extrae valores de pixel de la imagen
                r, g, b, h, s, v = Ut.get_pixel_values(self.picture, x, y)

                # Actualiza el color
                self.color['r'] = r
                self.color['g'] = g
                self.color['b'] = b

                Ut.set_line_color(r, g, b)

                # Visualiza el color extraído en el label
                tl_lbl_color = getattr(self.ui, f'tl_lbl_color_{self.widget_id}')
                tl_lbl_color.setStyleSheet(f"background: rgb({self.color['r']}, {self.color['g']}, "
                                           f"{self.color['b']});\n""border: 1px solid gray;")
        else:
            pass

    def set_action_button(self, action):
        """
        Setter del atributo acción usado en callbacks
        :param action:
        :return:
        """
        self.action = action
        self.open_image()

    def view_zones(self):
        """
        Visualiza el resultado del filtro
        :return:
        """
        cv2.imshow(f'{self.widget_id}_Zonas delimitadas', self.get_picture_filtered().content)

        # Bloquea edición del filtro
        getattr(self.ui, f'dz_btn_draw_zone_{self.widget_id}').setDisabled(True)
        getattr(self.ui, f'dz_cbx_executed_{self.widget_id}').setCheckState(QtCore.Qt.Checked)
        self.is_done = True
        self.set_ext_btn_state(True)

    def clean(self):
        """
        Limpieza de las zonas en el objeto imagen y en la interfaz gráfica
        :return:
        """

        self.picture = self.get_original_picture()

    def get_picture_filtered(self):
        """
        Genera el resultado del filtro aplicado
        :return:
        """
        picture = Pic()
        picture.create_picture_from_content(self.picture)

        # Genera la capa filtrada con la mascara adecuada
        return picture

    def set_original_picture(self, picture):
        self._original_picture = copy.deepcopy(picture)

    def get_original_picture(self):
        return copy.deepcopy(self._original_picture)
