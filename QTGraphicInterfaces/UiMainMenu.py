# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/UiMainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.setWindowModality(QtCore.Qt.NonModal)
        Manager.resize(714, 640)
        Manager.setDocumentMode(False)
        self.central_frame = QtWidgets.QWidget(Manager)
        self.central_frame.setObjectName("central_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.base_frame = QtWidgets.QFrame(self.central_frame)
        self.base_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.base_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base_frame.setObjectName("base_frame")
        self.ly_base_frame = QtWidgets.QVBoxLayout(self.base_frame)
        self.ly_base_frame.setContentsMargins(0, 0, 0, 0)
        self.ly_base_frame.setSpacing(0)
        self.ly_base_frame.setObjectName("ly_base_frame")
        self.top_frame = QtWidgets.QFrame(self.base_frame)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(74, 38, 253);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #4a26fd;\n"
"    border-radius:5px;\n"
"    border: 1px solid  #4a26fd\n"
"\n"
"}\n"
"\n"
"QPushButton:Hover{    \n"
"    background-color :#021aee\n"
"}")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.ly_top_frame = QtWidgets.QHBoxLayout(self.top_frame)
        self.ly_top_frame.setContentsMargins(-1, -1, -1, 2)
        self.ly_top_frame.setSpacing(9)
        self.ly_top_frame.setObjectName("ly_top_frame")
        self.lbl_title = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(18)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_title.setObjectName("lbl_title")
        self.ly_top_frame.addWidget(self.lbl_title)
        spacerItem = QtWidgets.QSpacerItem(573, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ly_top_frame.addItem(spacerItem)
        self.btn_minimize = QtWidgets.QPushButton(self.top_frame)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/window-minimize-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QtCore.QSize(20, 20))
        self.btn_minimize.setObjectName("btn_minimize")
        self.ly_top_frame.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.top_frame)
        self.btn_close.setEnabled(True)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/xmark-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(20, 20))
        self.btn_close.setObjectName("btn_close")
        self.ly_top_frame.addWidget(self.btn_close)
        self.ly_base_frame.addWidget(self.top_frame)
        self.main_frame = QtWidgets.QFrame(self.base_frame)
        self.main_frame.setEnabled(True)
        self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.ly_main_frame = QtWidgets.QGridLayout(self.main_frame)
        self.ly_main_frame.setObjectName("ly_main_frame")
        self.scroll_area = QtWidgets.QScrollArea(self.main_frame)
        self.scroll_area.setMinimumSize(QtCore.QSize(681, 531))
        self.scroll_area.setMaximumSize(QtCore.QSize(681, 531))
        self.scroll_area.setStyleSheet("")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 679, 529))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.ly_lots = QtWidgets.QFormLayout(self.scroll_area_widget_contents)
        self.ly_lots.setObjectName("ly_lots")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.ly_main_frame.addWidget(self.scroll_area, 1, 0, 1, 1)
        self.tool_frame = QtWidgets.QFrame(self.main_frame)
        self.tool_frame.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: #4a26fd;\n"
"    border-radius:5px;\n"
"    border: 1px solid  #4a26fd;\n"
"    font:  12pt \"FontAwesome\" ; \n"
"    color: #ffffff\n"
"\n"
"}\n"
"\n"
"QPushButton:Hover{    \n"
"    background-color :#021aee\n"
"}")
        self.tool_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tool_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tool_frame.setObjectName("tool_frame")
        self.btn_create = QtWidgets.QPushButton(self.tool_frame)
        self.btn_create.setGeometry(QtCore.QRect(0, 0, 91, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("QTGraphicInterfaces/Icons/plus-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_create.setIcon(icon2)
        self.btn_create.setObjectName("btn_create")
        self.ly_main_frame.addWidget(self.tool_frame, 0, 0, 1, 1)
        self.ly_base_frame.addWidget(self.main_frame)
        self.horizontalLayout.addWidget(self.base_frame)
        Manager.setCentralWidget(self.central_frame)

        self.retranslateUi(Manager)
        self.btn_minimize.clicked.connect(Manager.showMinimized)
        self.btn_close.clicked.connect(Manager.close)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        _translate = QtCore.QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "MainWindow"))
        self.lbl_title.setText(_translate("Manager", "Parking Manager"))
        self.btn_create.setText(_translate("Manager", "Nuevo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Manager = QtWidgets.QMainWindow()
    ui = Ui_Manager()
    ui.setupUi(Manager)
    Manager.show()
    sys.exit(app.exec_())
