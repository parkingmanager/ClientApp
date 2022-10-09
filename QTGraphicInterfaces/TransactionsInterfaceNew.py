# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/TransactionsInterfaceNew.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransactionInterfaceNew(object):
    def setupUi(self, TransactionInterfaceNew):
        TransactionInterfaceNew.setObjectName("TransactionInterfaceNew")
        TransactionInterfaceNew.resize(530, 761)
        TransactionInterfaceNew.setStyleSheet("QPushButton{\n"
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
        self.centralwidget = QtWidgets.QWidget(TransactionInterfaceNew)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_open_camera = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_open_camera.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/camera-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_camera.setIcon(icon)
        self.btn_open_camera.setIconSize(QtCore.QSize(32, 32))
        self.btn_open_camera.setObjectName("btn_open_camera")
        self.horizontalLayout.addWidget(self.btn_open_camera)
        self.btn_open_keyboard = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_open_keyboard.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/keyboard-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_keyboard.setIcon(icon1)
        self.btn_open_keyboard.setIconSize(QtCore.QSize(32, 32))
        self.btn_open_keyboard.setObjectName("btn_open_keyboard")
        self.horizontalLayout.addWidget(self.btn_open_keyboard)
        self.btn_print = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_print.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/print-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_print.setIcon(icon2)
        self.btn_print.setIconSize(QtCore.QSize(32, 32))
        self.btn_print.setObjectName("btn_print")
        self.horizontalLayout.addWidget(self.btn_print)
        self.btn_reverse_action = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_reverse_action.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/xmark-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reverse_action.setIcon(icon3)
        self.btn_reverse_action.setIconSize(QtCore.QSize(32, 32))
        self.btn_reverse_action.setObjectName("btn_reverse_action")
        self.horizontalLayout.addWidget(self.btn_reverse_action)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txb_layout = QtWidgets.QHBoxLayout()
        self.txb_layout.setContentsMargins(5, 5, 5, 5)
        self.txb_layout.setObjectName("txb_layout")
        self.txb_resume = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.txb_resume.setFont(font)
        self.txb_resume.setPlainText("")
        self.txb_resume.setObjectName("txb_resume")
        self.txb_layout.addWidget(self.txb_resume)
        self.verticalLayout.addLayout(self.txb_layout)
        TransactionInterfaceNew.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TransactionInterfaceNew)
        self.statusbar.setObjectName("statusbar")
        TransactionInterfaceNew.setStatusBar(self.statusbar)

        self.retranslateUi(TransactionInterfaceNew)
        QtCore.QMetaObject.connectSlotsByName(TransactionInterfaceNew)

    def retranslateUi(self, TransactionInterfaceNew):
        _translate = QtCore.QCoreApplication.translate
        TransactionInterfaceNew.setWindowTitle(_translate("TransactionInterfaceNew", "Transacciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransactionInterfaceNew = QtWidgets.QMainWindow()
    ui = Ui_TransactionInterfaceNew()
    ui.setupUi(TransactionInterfaceNew)
    TransactionInterfaceNew.show()
    sys.exit(app.exec_())
