from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMessageBox
import sys
from QTGraphicInterfaces.UiMainMenu import Ui_Manager


# Ventanas
from Windows.Editor import Editor
from Windows.Editor import Modes
from Windows.Visor import Visor
from Windows.Transactions import Transaction
from Windows.Stats import Stats
# Comunicación
from Integration.ParkingApi import ParkingApi


class Maqueta(QtWidgets.QMainWindow):

    def __init__(self):
        """
            Constructor donde se inicializan parámetros de interfaz gráfica
        """
        super(Maqueta, self).__init__()
        self.ui = Ui_Manager()
        self.ui.setupUi(self)

        self.api = ParkingApi()

        # Consulta la información necesaria
        lotes = self.api.get_parkings()

        # Mapea lo lotes en la interfaz
        for lot in lotes:
            self.draw_widget(lot)

        # Conexiones
        self.ui.btn_create.clicked.connect(lambda callback: self.open_editor(Modes.Creator, 0))

    def draw_widget(self,  lote: dict):

        id = lote["IdLote"]
        lot_frame = QtWidgets.QFrame(self.ui.scroll_area_widget_contents)
        lot_frame.setMinimumSize(QtCore.QSize(100, 40))
        lot_frame.setStyleSheet("QFrame{\n"
                                     "    border:1px solid #4a26fd;\n"
                                     "    border-radius: 10px;\n"
                                      "}\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "    background-color: #ffffff;\n"
                                     "    border-radius:5px;\n"
                                     "    border: 1px solid  #ffffff\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:Hover{    \n"
                                     "    border: 1px solid  #4a26fd;\n"
                                     "}")
        lot_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        lot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        lot_frame.setObjectName(f"lot_frame_{id}")

        ly_lot = QtWidgets.QHBoxLayout(lot_frame)
        ly_lot.setObjectName(f"ly_lot_{id}")

        lbl_lot_id = QtWidgets.QLabel(lot_frame)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(13)
        lbl_lot_id.setFont(font)
        lbl_lot_id.setStyleSheet("border:none")
        lbl_lot_id.setObjectName(f"lbl_lot_id_{id}")
        ly_lot.addWidget(lbl_lot_id)
        lbl_lot_id_spacer_item = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        ly_lot.addItem(lbl_lot_id_spacer_item)

        lbl_lot_name = QtWidgets.QLabel(lot_frame)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(13)
        lbl_lot_name.setFont(font)
        lbl_lot_name.setStyleSheet("border:none")
        lbl_lot_name.setObjectName(f"lbl_lot_name_{id}")
        ly_lot.addWidget(lbl_lot_name)
        lbl_lot_name_spacer_item = QtWidgets.QSpacerItem(227, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        ly_lot.addItem(lbl_lot_name_spacer_item)

        btn_transactions_interface = QtWidgets.QPushButton(lot_frame)
        btn_transactions_interface.setText("")
        btn_transactions_icon = QtGui.QIcon()
        btn_transactions_icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/car-solid.svg"), QtGui.QIcon.Normal,
                                         QtGui.QIcon.Off)
        btn_transactions_interface.setIcon(btn_transactions_icon)
        btn_transactions_interface.setObjectName(f"btn_transactions_interface_{id}")
        ly_lot.addWidget(btn_transactions_interface)

        line_separator = QtWidgets.QFrame(lot_frame)
        line_separator.setFrameShape(QtWidgets.QFrame.VLine)
        line_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_separator.setObjectName(f"line_separator_{id}")
        ly_lot.addWidget(line_separator)

        btn_lot_view = QtWidgets.QPushButton(lot_frame)
        btn_lot_view.setText("")
        btn_lot_view_icon = QtGui.QIcon()
        btn_lot_view_icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/eye-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn_lot_view.setIcon(btn_lot_view_icon)
        btn_lot_view.setObjectName(f"btn_lot_view_{id}")
        ly_lot.addWidget(btn_lot_view)

        btn_lot_edit = QtWidgets.QPushButton(lot_frame)
        btn_lot_edit.setText("")
        btn_lot_edit_icon = QtGui.QIcon()
        btn_lot_edit_icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/pen-to-square-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn_lot_edit.setIcon(btn_lot_edit_icon)
        btn_lot_edit.setObjectName(f"btn_lot_edit_{id}")
        ly_lot.addWidget(btn_lot_edit)

        btn_lot_stats = QtWidgets.QPushButton(lot_frame)
        btn_lot_stats.setText("")
        btn_lot_stats_icon = QtGui.QIcon()
        btn_lot_stats_icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/chart-line-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn_lot_stats.setIcon(btn_lot_stats_icon)
        btn_lot_stats.setObjectName(f"btn_lot_stats_{id}")
        ly_lot.addWidget(btn_lot_stats)

        btn_lot_delete = QtWidgets.QPushButton(lot_frame)
        btn_lot_delete.setText("")
        btn_lot_delete_icon = QtGui.QIcon()
        btn_lot_delete_icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/trash-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn_lot_delete.setIcon(btn_lot_delete_icon)
        btn_lot_delete.setObjectName("btn_lot_delete")
        ly_lot.addWidget(btn_lot_delete)

        setattr(self.ui, f'lot_frame{id}', lot_frame)

        # Parametrización del lote
        lbl_lot_id.setText(str(lote["IdLote"]))
        lbl_lot_name.setText(lote["Nombre"])

        self.ui.ly_lots.setWidget(id, QtWidgets.QFormLayout.SpanningRole, lot_frame)

        # Eventos dinámicos de los botones
        btn_lot_view.clicked.connect(lambda callback: self.view_lot(id))
        btn_lot_edit.clicked.connect(lambda callback: self.open_editor(Modes.Editor, id))
        btn_lot_delete.clicked.connect(lambda callback: self.delete_lot(id))
        btn_lot_stats.clicked.connect(lambda callback: self.open_stats_interface(id))
        btn_transactions_interface.clicked.connect(lambda callback: self.open_transactions_interface(id))

    def view_lot(self, parking_id):

        # Lectura del Id
        data = self.api.get_parking(parking_id)

        # Instancia del visor
        app_visor = Visor(data)

    def delete_lot(self, parking_id):

        ret = QMessageBox.question(self, 'Eliminar lote', "¿Está seguro de eliminar el lote?", QMessageBox.Yes | QMessageBox.No )

        if ret == QMessageBox.Yes:
            # Actualizar la lista
            if self.api.delete_parking(parking_id):
                lot_frame = getattr(self.ui, f'lot_frame{parking_id}')
                lot_frame.deleteLater()
        else:
            return

    def add_lot(self, lot: object):
        self.draw_widget(lot)

    def open_editor(self, mode: Modes, parking_id):
        self.app_editor = Editor(self, mode, parking_id)
        self.app_editor.show()

    def open_transactions_interface(self, parking_id):
        self.app_transactions = Transaction(self, parking_id)
        self.app_transactions.show()

    def open_stats_interface(self, parking_id):
        self.app_stats = Stats(self, parking_id)
        self.app_stats.show()


app = QtWidgets.QApplication([])
application = Maqueta()
application.show()
sys.exit(app.exec())