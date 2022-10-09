import cv2
import numpy as np
import copy
import json
import re
import math
from enum import Enum

import Windows.Editor
from QTGraphicInterfaces.DynamicMainInterfaceForm import Ui_MainWindow as Ui
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from Filters.Filter import Filter
from Models.Picture import Picture as Pic
from Models.Utils import Utils as Ut

# Negocio
from Bussiness.Models.Lote import Lote as Lote
from Bussiness.Models.DefinedSpace import DefinedSpace as DefinedSpace

# Integración
from Integration.ParkingApi import ParkingApi as ParkingApi


# noinspection SpellCheckingInspection
class SpaceConfig:
    """
    Filtro que permite elegir específicamente zonas de una imagen para delimitar un estacionamiento
    """

    def __init__(self, picture: Pic, ui: Ui, row: int, col: int, widget_id: int, context):

        # Creación del lote
        self.lot = Lote()
        self._original_picture = None
        self.set_original_picture(picture)
        self.picture = self.get_original_picture()
        self.ui = ui
        self.context = context
        self.widget_id = widget_id
        self.draw_widget(row, col, widget_id)

        if self.context.mode == Windows.Editor.Modes.Creator:
            self.generate_spaces()
        elif self.context.mode == Windows.Editor.Modes.Editor:
            self.generate_spaces_for_edit()

        self.json_info = {}

        # Conexiones fijas
        self.ui.btn_save_json.clicked.connect(lambda callback: self.save_json_file())

    def set_visible(self, state):
        """
        Cambia la visibilidad de un filtro
        :param state:
        :return:
        """
        # Recupera el widget y aplica lógica
        group = getattr(self.ui, f'ce_group_{self.widget_id}')
        group.setVisible(state)

    def draw_widget(self, row: int, col: int, widget_id: int):
        """
        Renderiza el widget del filtro en la pantallaS
        :param row:
        :param col:
        :param widget_id:
        :return:
        """

        setattr(self.ui, f'ce_group_{widget_id}', QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents))
        ce_group = getattr(self.ui, f'ce_group_{widget_id}')
        ce_group.setMinimumSize(QtCore.QSize(0, 90))
        ce_group.setObjectName(f'ce_group_{widget_id}')

        setattr(self.ui, f'ce_btn_clear_{widget_id}', QtWidgets.QPushButton(ce_group))
        ce_btn_clear = getattr(self.ui, f'ce_btn_clear_{widget_id}')
        ce_btn_clear.setGeometry(QtCore.QRect(300, 30, 40, 40))
        ce_btn_clear.setMinimumSize(QtCore.QSize(40, 40))
        ce_btn_clear.setMaximumSize(QtCore.QSize(40, 40))
        ce_btn_clear.setText("")
        icon_ce_btn_clear = QtGui.QIcon()
        icon_ce_btn_clear.addPixmap(QtGui.QPixmap("icons/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ce_btn_clear.setIcon(icon_ce_btn_clear)
        ce_btn_clear.setIconSize(QtCore.QSize(32, 32))
        ce_btn_clear.setObjectName(f'ce_btn_clear_{widget_id}')

        setattr(self.ui, f'ce_btn_start_{widget_id}', QtWidgets.QPushButton(ce_group))
        ce_btn_start = getattr(self.ui, f'ce_btn_start_{widget_id}')
        ce_btn_start.setGeometry(QtCore.QRect(10, 30, 40, 40))
        ce_btn_start.setMinimumSize(QtCore.QSize(40, 40))
        ce_btn_start.setMaximumSize(QtCore.QSize(40, 40))
        ce_btn_start.setText("")
        icon_ce_btn_start = QtGui.QIcon()
        icon_ce_btn_start.addPixmap(QtGui.QPixmap("icons/iniciar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ce_btn_start.setIcon(icon_ce_btn_start)
        ce_btn_start.setIconSize(QtCore.QSize(32, 32))
        ce_btn_start.setObjectName(f'ce_btn_start_{widget_id}')

        setattr(self.ui, f'ce_btn_delete_{widget_id}', QtWidgets.QPushButton(ce_group))
        ce_btn_delete = getattr(self.ui, f'ce_btn_delete_{widget_id}')
        ce_btn_delete.setGeometry(QtCore.QRect(340, 30, 40, 40))
        ce_btn_delete.setMinimumSize(QtCore.QSize(40, 40))
        ce_btn_delete.setMaximumSize(QtCore.QSize(40, 40))
        ce_btn_delete.setText("")
        icon_ce_btn_delete = QtGui.QIcon()
        icon_ce_btn_delete.addPixmap(QtGui.QPixmap("icons/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ce_btn_delete.setIcon(icon_ce_btn_delete)
        ce_btn_delete.setIconSize(QtCore.QSize(32, 32))
        ce_btn_delete.setObjectName(f'ce_btn_delete_{widget_id}')

        setattr(self.ui, f'ce_btn_view_{widget_id}', QtWidgets.QPushButton(ce_group))
        ce_btn_view = getattr(self.ui, f'ce_btn_view_{widget_id}')
        ce_btn_view.setGeometry(QtCore.QRect(260, 30, 40, 40))
        ce_btn_view.setMinimumSize(QtCore.QSize(40, 40))
        ce_btn_view.setMaximumSize(QtCore.QSize(40, 40))
        ce_btn_view.setText("")
        icon_ce_btn_view = QtGui.QIcon()
        icon_ce_btn_view.addPixmap(QtGui.QPixmap("icons/ver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ce_btn_view.setIcon(icon_ce_btn_view)
        ce_btn_view.setIconSize(QtCore.QSize(32, 32))
        ce_btn_view.setObjectName(f'ce_btn_view_{widget_id}')

        _translate = QtCore.QCoreApplication.translate

        ce_group.setTitle(_translate("MainWindow", "Configuración de espacios"))
        ce_btn_clear.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))
        ce_btn_view.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ver imagen</p></body></html>"))
        ce_btn_delete.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpiar</p></body></html>"))
        ce_btn_start.setToolTip(_translate("MainWindow", "<html><head/><body><p>Dibujar coordenadas</p></body></html>"))

        self.ui.formLayout.setWidget(widget_id, QtWidgets.QFormLayout.FieldRole, ce_group)

        if self.context.mode == Windows.Editor.Modes.Creator:
            ce_btn_start.clicked.connect(lambda callback: self.generate_spaces())
        elif self.context.mode == Windows.Editor.Modes.Editor:
            ce_btn_start.clicked.connect(lambda callback: self.generate_spaces_for_edit())

    @staticmethod
    def clean_coordinates(coord):
        return re.sub("[^\w\s]", "", coord)

    @staticmethod
    def generate_numpy_coordinates(space):
        coord1 = np.fromstring(SpaceConfig.clean_coordinates(space["Coord1"]), dtype=int, sep='  ')
        coord2 = np.fromstring(SpaceConfig.clean_coordinates(space["Coord2"]), dtype=int, sep='  ')
        coord3 = np.fromstring(SpaceConfig.clean_coordinates(space["Coord3"]), dtype=int, sep='  ')
        coord4 = np.fromstring(SpaceConfig.clean_coordinates(space["Coord4"]), dtype=int, sep='  ')

        return [coord1, coord2, coord3, coord4]

    def generate_spaces_for_edit(self):

        try:

            # Extrae la imagen inicial
            initial_image = Ut.get_original_image_content()

            for space in self.context.parking["EspaciosDelimitados"]:
                c = SpaceConfig.generate_numpy_coordinates(space)

                contour = [
                    np.array([[[c[0][0], c[0][1]]], [[c[1][0], c[1][1]]], [[c[2][0], c[2][1]]], [[c[3][0], c[3][1]]]],
                             dtype=np.int32)]

                color = (0, 255, 0)

                if space["Tipo"] == 'discapacitado':
                    color = (255, 0, 0)

                # Dibuja el contorno por defecto
                cv2.drawContours(image=initial_image, contours=contour, thickness=2, color=color,
                                 lineType=cv2.LINE_AA, contourIdx=-1)

                moment = cv2.moments(contour[0])
                center_x = int(moment["m10"] / moment["m00"])
                center_y = int(moment["m01"] / moment["m00"])

                # Texto que enumera el espacio
                cv2.putText(initial_image, f"{space['Indice']}", (center_x - 20, center_y - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                print(f'Puntos_: {len(contour[0])}, approx: {str(contour[0][0])}')

                ds = DefinedSpace(contour[0], True, space["Tipo"], space['Indice'], [center_x, center_y])
                ds.IdEspacioDelimitado = space["IdEspacioDelimitado"]
                ds.IdLote = space["IdLote"]

                self.lot.add_defined_space(ds)

            cv2.imshow(f'{self.widget_id}_Configuracion...', initial_image)

            # Habilita botón
            self.ui.btn_save_json.setDisabled(False)
            print(self.lot.serialize())

            # Habilita edición
            cv2.setMouseCallback(f'{self.widget_id}_Configuracion...', self.mouse_callback)

        except Exception as ex:
            raise Exception(ex)

    def generate_spaces(self):

        try:
            # Extrae la imagen inicial
            initial_image = Ut.get_original_image_content()

            # Binariza la mascara
            original_bw = cv2.cvtColor(self.picture, cv2.COLOR_BGR2GRAY)
            _, original_bin = cv2.threshold(original_bw, 100, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(original_bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            index = 0

            # Dibuja el rectangulo:
            for c in contours:
                epsilon = 0.01 * cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, epsilon, True)

                moment = cv2.moments(c)
                center_x = int(moment["m10"] / moment["m00"])
                center_y = int(moment["m01"] / moment["m00"])

                index += 1

                # Dibuja el contorno por defecto
                cv2.drawContours(image=initial_image, contours=[approx], thickness=2, color=(0, 255, 0),
                                 lineType=cv2.LINE_AA, contourIdx=-1)
                # Texto que enumera el espacio
                cv2.putText(initial_image, f"{index}", (center_x - 20, center_y - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                print(f'Puntos: {len(approx)}, approx: {str(approx[0][0])}')
                ds = DefinedSpace(approx, True, "normal", index, [center_x, center_y])
                self.lot.add_defined_space(ds)

            cv2.imshow(f'{self.widget_id}_Configuracion...', initial_image)

            # Habilita botón
            self.ui.btn_save_json.setDisabled(False)
            print(self.lot.serialize())

            # Habilita edición
            cv2.setMouseCallback(f'{self.widget_id}_Configuracion...', self.mouse_callback)

        except Exception as ex:
            raise Exception(ex)

    def mouse_callback(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDBLCLK:

            # Extrae la imagen inicial
            initial_image = Ut.get_original_image_content()

            # Verifica en que espacio señaló
            for ds in self.lot.EspaciosDelimitados:
                cont, color = ds.change_state(x, y)

                # Calcula el centro

                cv2.putText(initial_image, f"{ds.Indice}", (ds.Centro[0] - 20, ds.Centro[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                cv2.drawContours(image=initial_image, contours=cont, thickness=2, color=color,
                                     lineType=cv2.LINE_AA, contourIdx=-1)

            cv2.imshow(f'{self.widget_id}_Configuracion...', initial_image)

    def save_json_file(self):
        """
        Almacena el espaciop configurado
        :return:
        """
        json_file_path, _ = QFileDialog.getSaveFileName(self.context, self.context.tr("Guardar configuración..."), ".", self.context.tr("Archivos JSON "
                                                                                                      "(*.json)"))

        # Actualiza la información escrita en los textbox
        self.lot.update_property("Nombre", self.ui.txb_name.text())
        self.lot.update_property("Identificador", self.ui.txb_identifier.text())
        self.lot.update_property("Token", self.ui.txb_token.text())
        self.lot.update_property("Direccion", self.ui.txb_address.text())
        self.lot.update_property("RutaModelo", self.ui.txb_model.text())
        self.lot.update_property("FuenteVideo", self.ui.txb_video_source.text())


        with open(json_file_path, 'w') as fp:
            json.dump(self.lot.get_dict(), fp)

        print(f"File name: {json_file_path}")

        self.save_json_data()

    def save_json_data(self):

        api = ParkingApi()

        if self.context.mode == Windows.Editor.Modes.Editor:
            self.lot.update_property("IdLote", self.context.parking["IdLote"])
            lot = api.update_parking(self.lot.get_dict())

        elif self.context.mode == Windows.Editor.Modes.Creator:
            lot = api.create_parking(self.lot.get_dict())
            # Crea el lote en la ventana principal
            self.context.add_lot_in_main(lot)

        self.context.close()

    def set_original_picture(self, picture):
        self._original_picture = copy.deepcopy(picture)

    def get_original_picture(self):
        return copy.deepcopy(self._original_picture)