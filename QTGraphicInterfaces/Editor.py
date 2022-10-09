# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/Editor.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(875, 442)
        Editor.setStyleSheet("QPushButton{\n"
"    background-color: #4a26fd;\n"
"    border-radius:5px;\n"
"    border: 1px solid  #4a26fd;\n"
"    font:  8pt \"FontAwesome\" ; \n"
"    color: #ffffff\n"
"\n"
"}\n"
"\n"
"QPushButton:Hover{    \n"
"    background-color :#021aee\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.gbr_load_image = QtWidgets.QGroupBox(self.centralwidget)
        self.gbr_load_image.setGeometry(QtCore.QRect(10, 120, 421, 81))
        self.gbr_load_image.setObjectName("gbr_load_image")
        self.btn_load_image = QtWidgets.QPushButton(self.gbr_load_image)
        self.btn_load_image.setGeometry(QtCore.QRect(10, 20, 401, 23))
        self.btn_load_image.setObjectName("btn_load_image")
        self.lbl_load_image = QtWidgets.QLabel(self.gbr_load_image)
        self.lbl_load_image.setGeometry(QtCore.QRect(10, 50, 391, 31))
        self.lbl_load_image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_load_image.setObjectName("lbl_load_image")
        self.scrollArea_filters = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_filters.setGeometry(QtCore.QRect(440, 70, 421, 291))
        self.scrollArea_filters.setWidgetResizable(True)
        self.scrollArea_filters.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scrollArea_filters.setObjectName("scrollArea_filters")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.scrollArea_filters.setWidget(self.scrollAreaWidgetContents)
        self.gbr_add_filter = QtWidgets.QGroupBox(self.centralwidget)
        self.gbr_add_filter.setGeometry(QtCore.QRect(440, 10, 421, 51))
        self.gbr_add_filter.setCheckable(False)
        self.gbr_add_filter.setObjectName("gbr_add_filter")
        self.btn_delimite = QtWidgets.QPushButton(self.gbr_add_filter)
        self.btn_delimite.setGeometry(QtCore.QRect(40, 20, 71, 23))
        self.btn_delimite.setObjectName("btn_delimite")
        self.btn_color = QtWidgets.QPushButton(self.gbr_add_filter)
        self.btn_color.setGeometry(QtCore.QRect(110, 20, 71, 23))
        self.btn_color.setObjectName("btn_color")
        self.btn_transformation = QtWidgets.QPushButton(self.gbr_add_filter)
        self.btn_transformation.setGeometry(QtCore.QRect(180, 20, 71, 23))
        self.btn_transformation.setObjectName("btn_transformation")
        self.btn_perspective = QtWidgets.QPushButton(self.gbr_add_filter)
        self.btn_perspective.setGeometry(QtCore.QRect(250, 20, 71, 23))
        self.btn_perspective.setObjectName("btn_perspective")
        self.btn_search = QtWidgets.QPushButton(self.gbr_add_filter)
        self.btn_search.setGeometry(QtCore.QRect(320, 20, 71, 23))
        self.btn_search.setObjectName("btn_search")
        self.gbr_end = QtWidgets.QGroupBox(self.centralwidget)
        self.gbr_end.setGeometry(QtCore.QRect(440, 370, 421, 51))
        self.gbr_end.setCheckable(False)
        self.gbr_end.setObjectName("gbr_end")
        self.btn_save_json = QtWidgets.QPushButton(self.gbr_end)
        self.btn_save_json.setGeometry(QtCore.QRect(10, 20, 401, 23))
        self.btn_save_json.setObjectName("btn_save_json")
        self.gbr_info = QtWidgets.QGroupBox(self.centralwidget)
        self.gbr_info.setGeometry(QtCore.QRect(10, 210, 421, 211))
        self.gbr_info.setObjectName("gbr_info")
        self.txb_identifier = QtWidgets.QLineEdit(self.gbr_info)
        self.txb_identifier.setGeometry(QtCore.QRect(110, 30, 301, 20))
        self.txb_identifier.setObjectName("txb_identifier")
        self.gbr_lbl_identifier = QtWidgets.QLabel(self.gbr_info)
        self.gbr_lbl_identifier.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.gbr_lbl_identifier.setObjectName("gbr_lbl_identifier")
        self.gbr_lbl_name = QtWidgets.QLabel(self.gbr_info)
        self.gbr_lbl_name.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.gbr_lbl_name.setObjectName("gbr_lbl_name")
        self.txb_name = QtWidgets.QLineEdit(self.gbr_info)
        self.txb_name.setGeometry(QtCore.QRect(80, 90, 331, 20))
        self.txb_name.setObjectName("txb_name")
        self.gbr_lbl_address = QtWidgets.QLabel(self.gbr_info)
        self.gbr_lbl_address.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.gbr_lbl_address.setObjectName("gbr_lbl_address")
        self.txb_address = QtWidgets.QLineEdit(self.gbr_info)
        self.txb_address.setGeometry(QtCore.QRect(80, 120, 331, 20))
        self.txb_address.setObjectName("txb_address")
        self.gbr_lbl_token = QtWidgets.QLabel(self.gbr_info)
        self.gbr_lbl_token.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.gbr_lbl_token.setObjectName("gbr_lbl_token")
        self.txb_token = QtWidgets.QLineEdit(self.gbr_info)
        self.txb_token.setGeometry(QtCore.QRect(110, 60, 301, 20))
        self.txb_token.setObjectName("txb_token")
        self.gbr_lbl_model = QtWidgets.QLabel(self.gbr_info)
        self.gbr_lbl_model.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.gbr_lbl_model.setObjectName("gbr_lbl_model")
        self.txb_model = QtWidgets.QLineEdit(self.gbr_info)
        self.txb_model.setGeometry(QtCore.QRect(80, 150, 331, 20))
        self.txb_model.setObjectName("txb_model")
        self.gbr_config = QtWidgets.QGroupBox(self.centralwidget)
        self.gbr_config.setGeometry(QtCore.QRect(10, 10, 421, 101))
        self.gbr_config.setObjectName("gbr_config")
        self.gbr_lbl_video_source = QtWidgets.QLabel(self.gbr_config)
        self.gbr_lbl_video_source.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.gbr_lbl_video_source.setObjectName("gbr_lbl_video_source")
        self.txb_video_source = QtWidgets.QLineEdit(self.gbr_config)
        self.txb_video_source.setGeometry(QtCore.QRect(110, 30, 301, 20))
        self.txb_video_source.setObjectName("txb_video_source")
        self.btn_capture_image = QtWidgets.QPushButton(self.gbr_config)
        self.btn_capture_image.setGeometry(QtCore.QRect(10, 60, 401, 23))
        self.btn_capture_image.setObjectName("btn_capture_image")
        Editor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Editor)
        self.statusbar.setObjectName("statusbar")
        Editor.setStatusBar(self.statusbar)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "Editor"))
        self.gbr_load_image.setTitle(_translate("Editor", "Carga de imagen"))
        self.btn_load_image.setText(_translate("Editor", "Cargar imagen"))
        self.lbl_load_image.setText(_translate("Editor", "..."))
        self.gbr_add_filter.setTitle(_translate("Editor", "Agregar filtros"))
        self.btn_delimite.setText(_translate("Editor", "Delimitar "))
        self.btn_color.setText(_translate("Editor", "Color"))
        self.btn_transformation.setText(_translate("Editor", "Transf. libre"))
        self.btn_perspective.setText(_translate("Editor", "Perspectiva"))
        self.btn_search.setText(_translate("Editor", "Busqueda"))
        self.gbr_end.setTitle(_translate("Editor", "Guardar configuración"))
        self.btn_save_json.setText(_translate("Editor", "Guardar"))
        self.gbr_info.setTitle(_translate("Editor", "Información"))
        self.gbr_lbl_identifier.setText(_translate("Editor", "Identificador único"))
        self.gbr_lbl_name.setText(_translate("Editor", "Nombre"))
        self.gbr_lbl_address.setText(_translate("Editor", "Dirección"))
        self.gbr_lbl_token.setText(_translate("Editor", "Token"))
        self.gbr_lbl_model.setText(_translate("Editor", "Ruta modelo"))
        self.gbr_config.setTitle(_translate("Editor", "Configuración"))
        self.gbr_lbl_video_source.setText(_translate("Editor", "Fuente de video"))
        self.btn_capture_image.setText(_translate("Editor", "Capturar imagen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QMainWindow()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())
