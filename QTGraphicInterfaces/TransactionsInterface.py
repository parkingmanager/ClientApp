# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/TransactionsInterface.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransactionInterface(object):
    def setupUi(self, TransactionInterface):
        TransactionInterface.setObjectName("TransactionInterface")
        TransactionInterface.resize(789, 503)
        TransactionInterface.setStyleSheet("QPushButton{\n"
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
        self.centralwidget = QtWidgets.QWidget(TransactionInterface)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 751, 112))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.btns_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.btns_layout.setContentsMargins(5, 5, 5, 5)
        self.btns_layout.setObjectName("btns_layout")
        self.btn_open_camera = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_open_camera.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/camera-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_camera.setIcon(icon)
        self.btn_open_camera.setIconSize(QtCore.QSize(100, 100))
        self.btn_open_camera.setObjectName("btn_open_camera")
        self.btns_layout.addWidget(self.btn_open_camera)
        self.btn_open_keyboard = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_open_keyboard.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/keyboard-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_keyboard.setIcon(icon1)
        self.btn_open_keyboard.setIconSize(QtCore.QSize(100, 100))
        self.btn_open_keyboard.setObjectName("btn_open_keyboard")
        self.btns_layout.addWidget(self.btn_open_keyboard)
        self.btn_reverse_action = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_reverse_action.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/xmark-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reverse_action.setIcon(icon2)
        self.btn_reverse_action.setIconSize(QtCore.QSize(100, 100))
        self.btn_reverse_action.setObjectName("btn_reverse_action")
        self.btns_layout.addWidget(self.btn_reverse_action)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 140, 751, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.txb_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.txb_layout.setContentsMargins(5, 5, 5, 5)
        self.txb_layout.setObjectName("txb_layout")
        self.txb_resume = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txb_resume.setFont(font)
        self.txb_resume.setObjectName("txb_resume")
        self.txb_layout.addWidget(self.txb_resume)
        TransactionInterface.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TransactionInterface)
        self.statusbar.setObjectName("statusbar")
        TransactionInterface.setStatusBar(self.statusbar)

        self.retranslateUi(TransactionInterface)
        QtCore.QMetaObject.connectSlotsByName(TransactionInterface)

    def retranslateUi(self, TransactionInterface):
        _translate = QtCore.QCoreApplication.translate
        TransactionInterface.setWindowTitle(_translate("TransactionInterface", "Transacciones"))
        self.txb_resume.setPlainText(_translate("TransactionInterface", "--------------------------------------------------------\n"
" PARQUEADERO DE PRUEBAS\n"
"--------------------------------------------------------\n"
"  PLACA : BPS75G\n"
"  FECHA : 27/07/2022 16:50:00\n"
"  TARIFA: $52\n"
"--------------------------------------------------------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransactionInterface = QtWidgets.QMainWindow()
    ui = Ui_TransactionInterface()
    ui.setupUi(TransactionInterface)
    TransactionInterface.show()
    sys.exit(app.exec_())
