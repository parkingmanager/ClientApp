# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/VehicleForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VehicleForm(object):
    def setupUi(self, VehicleForm):
        VehicleForm.setObjectName("VehicleForm")
        VehicleForm.resize(477, 425)
        VehicleForm.setStyleSheet("QPushButton{\n"
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
        self.centralwidget = QtWidgets.QWidget(VehicleForm)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 431, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.txb_plate = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txb_plate.setObjectName("txb_plate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txb_plate)
        self.lbl_class = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_class.setObjectName("lbl_class")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lbl_class)
        self.txb_class = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txb_class.setObjectName("txb_class")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txb_class)
        self.lbl_brand = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_brand.setObjectName("lbl_brand")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lbl_brand)
        self.txb_brand = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txb_brand.setObjectName("txb_brand")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txb_brand)
        self.lbl_line = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_line.setObjectName("lbl_line")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lbl_line)
        self.txb_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txb_line.setObjectName("txb_line")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.txb_line)
        self.lbl_model = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_model.setObjectName("lbl_model")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lbl_model)
        self.txb_model = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txb_model.setObjectName("txb_model")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.txb_model)
        self.lbl_color = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_color.setObjectName("lbl_color")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lbl_color)
        self.txb_color = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txb_color.setObjectName("txb_color")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.txb_color)
        self.lbl_plate = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_plate.setObjectName("lbl_plate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_plate)
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(80, 0, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(20, 360, 75, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(380, 360, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        VehicleForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VehicleForm)
        self.statusbar.setObjectName("statusbar")
        VehicleForm.setStatusBar(self.statusbar)

        self.retranslateUi(VehicleForm)
        QtCore.QMetaObject.connectSlotsByName(VehicleForm)

    def retranslateUi(self, VehicleForm):
        _translate = QtCore.QCoreApplication.translate
        VehicleForm.setWindowTitle(_translate("VehicleForm", "Vehiculo"))
        self.lbl_class.setText(_translate("VehicleForm", "Clase"))
        self.lbl_brand.setText(_translate("VehicleForm", "Marca"))
        self.lbl_line.setText(_translate("VehicleForm", "Linea"))
        self.lbl_model.setText(_translate("VehicleForm", "Modelo"))
        self.lbl_color.setText(_translate("VehicleForm", "Color"))
        self.lbl_plate.setText(_translate("VehicleForm", "Placa"))
        self.lbl_title.setText(_translate("VehicleForm", "Información del vehículo"))
        self.btn_ok.setText(_translate("VehicleForm", "Aceptar"))
        self.btn_cancel.setText(_translate("VehicleForm", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VehicleForm = QtWidgets.QMainWindow()
    ui = Ui_VehicleForm()
    ui.setupUi(VehicleForm)
    VehicleForm.show()
    sys.exit(app.exec_())
