# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTGraphicInterfaces/Maqueta.ui'
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
        self.ly_central_frame = QtWidgets.QVBoxLayout(self.central_frame)
        self.ly_central_frame.setContentsMargins(0, 0, 0, 0)
        self.ly_central_frame.setObjectName("ly_central_frame")
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
"    background-color :#916eff\n"
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
        icon.addPixmap(QtGui.QPixmap("Icons/window-minimize-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QtCore.QSize(20, 20))
        self.btn_minimize.setObjectName("btn_minimize")
        self.ly_top_frame.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.top_frame)
        self.btn_close.setEnabled(True)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/xmark-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.lot_frame = QtWidgets.QFrame(self.scroll_area_widget_contents)
        self.lot_frame.setMinimumSize(QtCore.QSize(100, 40))
        self.lot_frame.setStyleSheet("QFrame{\n"
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
        self.lot_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lot_frame.setObjectName("lot_frame")
        self.ly_lot = QtWidgets.QHBoxLayout(self.lot_frame)
        self.ly_lot.setObjectName("ly_lot")
        self.lbl_lot_id = QtWidgets.QLabel(self.lot_frame)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(13)
        self.lbl_lot_id.setFont(font)
        self.lbl_lot_id.setStyleSheet("border:none")
        self.lbl_lot_id.setObjectName("lbl_lot_id")
        self.ly_lot.addWidget(self.lbl_lot_id)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ly_lot.addItem(spacerItem1)
        self.lbl_lot_name = QtWidgets.QLabel(self.lot_frame)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(13)
        self.lbl_lot_name.setFont(font)
        self.lbl_lot_name.setStyleSheet("border:none")
        self.lbl_lot_name.setObjectName("lbl_lot_name")
        self.ly_lot.addWidget(self.lbl_lot_name)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ly_lot.addItem(spacerItem2)
        self.btn_car_interface = QtWidgets.QPushButton(self.lot_frame)
        self.btn_car_interface.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/car-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_car_interface.setIcon(icon2)
        self.btn_car_interface.setObjectName("btn_car_interface")
        self.ly_lot.addWidget(self.btn_car_interface)
        self.line_separator = QtWidgets.QFrame(self.lot_frame)
        self.line_separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_separator.setObjectName("line_separator")
        self.ly_lot.addWidget(self.line_separator)
        self.btn_lot_view = QtWidgets.QPushButton(self.lot_frame)
        self.btn_lot_view.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/eye-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lot_view.setIcon(icon3)
        self.btn_lot_view.setObjectName("btn_lot_view")
        self.ly_lot.addWidget(self.btn_lot_view)
        self.btn_lot_edit = QtWidgets.QPushButton(self.lot_frame)
        self.btn_lot_edit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/pen-to-square-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lot_edit.setIcon(icon4)
        self.btn_lot_edit.setObjectName("btn_lot_edit")
        self.ly_lot.addWidget(self.btn_lot_edit)
        self.btn_lot_stats = QtWidgets.QPushButton(self.lot_frame)
        self.btn_lot_stats.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/chart-line-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lot_stats.setIcon(icon5)
        self.btn_lot_stats.setObjectName("btn_lot_stats")
        self.ly_lot.addWidget(self.btn_lot_stats)
        self.btn_lot_delete = QtWidgets.QPushButton(self.lot_frame)
        self.btn_lot_delete.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/trash-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lot_delete.setIcon(icon6)
        self.btn_lot_delete.setObjectName("btn_lot_delete")
        self.ly_lot.addWidget(self.btn_lot_delete)
        self.ly_lots.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.lot_frame)
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.ly_main_frame.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.ly_base_frame.addWidget(self.main_frame)
        self.ly_central_frame.addWidget(self.base_frame)
        Manager.setCentralWidget(self.central_frame)

        self.retranslateUi(Manager)
        self.btn_minimize.clicked.connect(Manager.showMinimized)
        self.btn_close.clicked.connect(Manager.close)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        _translate = QtCore.QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "MainWindow"))
        self.lbl_title.setText(_translate("Manager", "Parking Manager"))
        self.lbl_lot_id.setText(_translate("Manager", "1256"))
        self.lbl_lot_name.setText(_translate("Manager", "Parkway calle 35 City Parking"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Manager = QtWidgets.QMainWindow()
    ui = Ui_Manager()
    ui.setupUi(Manager)
    Manager.show()
    sys.exit(app.exec_())
