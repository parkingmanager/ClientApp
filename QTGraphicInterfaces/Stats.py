# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/Stats.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):
        StatsWindow.setObjectName("StatsWindow")
        StatsWindow.resize(785, 654)
        StatsWindow.setStyleSheet("QPushButton{\n"
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
        self.centralwidget = QtWidgets.QWidget(StatsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(20, 10, 751, 611))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 731, 115))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vertical_layout_tools = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vertical_layout_tools.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_tools.setObjectName("vertical_layout_tools")
        self.lbl_statistics = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_statistics.setObjectName("lbl_statistics")
        self.vertical_layout_tools.addWidget(self.lbl_statistics)
        self.cbx_statistics = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cbx_statistics.setObjectName("cbx_statistics")
        self.cbx_statistics.addItem("")
        self.cbx_statistics.addItem("")
        self.vertical_layout_tools.addWidget(self.cbx_statistics)
        self.lbl_date = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbl_date.setObjectName("lbl_date")
        self.vertical_layout_tools.addWidget(self.lbl_date)
        self.txb_date = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.txb_date.setCalendarPopup(True)
        self.txb_date.setCurrentSectionIndex(0)
        self.txb_date.setObjectName("txb_date")
        self.vertical_layout_tools.addWidget(self.txb_date)
        self.btn_query = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_query.setObjectName("btn_query")
        self.vertical_layout_tools.addWidget(self.btn_query)
        self.scrollArea = QtWidgets.QScrollArea(self.main_frame)
        self.scrollArea.setGeometry(QtCore.QRect(9, 139, 731, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plot_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.plot_frame.setGeometry(QtCore.QRect(10, 10, 711, 451))
        self.plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plot_frame.setObjectName("plot_frame")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        StatsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StatsWindow)
        self.statusbar.setObjectName("statusbar")
        StatsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatsWindow)

    def retranslateUi(self, StatsWindow):
        _translate = QtCore.QCoreApplication.translate
        StatsWindow.setWindowTitle(_translate("StatsWindow", "Estadísticas"))
        self.lbl_statistics.setText(_translate("StatsWindow", "Tipo de estadística"))
        self.cbx_statistics.setItemText(0, _translate("StatsWindow", "Ocupaciones por dia"))
        self.cbx_statistics.setItemText(1, _translate("StatsWindow", "Transacciones por dia"))
        self.lbl_date.setText(_translate("StatsWindow", "Fecha"))
        self.txb_date.setDisplayFormat(_translate("StatsWindow", "dd/MM/yyyy"))
        self.btn_query.setText(_translate("StatsWindow", "Consultar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatsWindow = QtWidgets.QMainWindow()
    ui = Ui_StatsWindow()
    ui.setupUi(StatsWindow)
    StatsWindow.show()
    sys.exit(app.exec_())
