# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cfg_group = QtWidgets.QGroupBox(self.centralwidget)
        self.cfg_group.setGeometry(QtCore.QRect(10, 30, 461, 80))
        self.cfg_group.setObjectName("cfg_group")
        self.cfg_btn_create = QtWidgets.QPushButton(self.cfg_group)
        self.cfg_btn_create.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.cfg_btn_create.setObjectName("cfg_btn_create")
        self.cfg_btn_edit = QtWidgets.QPushButton(self.cfg_group)
        self.cfg_btn_edit.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.cfg_btn_edit.setObjectName("cfg_btn_edit")
        self.cfg_btn_delete = QtWidgets.QPushButton(self.cfg_group)
        self.cfg_btn_delete.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.cfg_btn_delete.setObjectName("cfg_btn_delete")
        self.op_group = QtWidgets.QGroupBox(self.centralwidget)
        self.op_group.setGeometry(QtCore.QRect(10, 120, 461, 71))
        self.op_group.setObjectName("op_group")
        self.op_btn_start = QtWidgets.QPushButton(self.op_group)
        self.op_btn_start.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.op_btn_start.setObjectName("op_btn_start")
        self.op_txb_id = QtWidgets.QLineEdit(self.op_group)
        self.op_txb_id.setGeometry(QtCore.QRect(40, 30, 61, 20))
        self.op_txb_id.setObjectName("op_txb_id")
        self.op_lbl_id = QtWidgets.QLabel(self.op_group)
        self.op_lbl_id.setGeometry(QtCore.QRect(20, 30, 16, 21))
        self.op_lbl_id.setObjectName("op_lbl_id")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parking manager"))
        self.cfg_group.setTitle(_translate("MainWindow", "Configuración de lote"))
        self.cfg_btn_create.setText(_translate("MainWindow", "Crear"))
        self.cfg_btn_edit.setText(_translate("MainWindow", "Editar"))
        self.cfg_btn_delete.setText(_translate("MainWindow", "Eliminar"))
        self.op_group.setTitle(_translate("MainWindow", "Operación"))
        self.op_btn_start.setText(_translate("MainWindow", "Iniciar"))
        self.op_lbl_id.setText(_translate("MainWindow", "Id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
