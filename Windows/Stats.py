import sys
import numpy as np
import random
import pandas as pd
from QTGraphicInterfaces.Stats import Ui_StatsWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# Comunicaciones
from Integration.ParkingApi import ParkingApi as api


class Stats(QtWidgets.QMainWindow):

    def __init__(self, main_context, parking_id):

        """
            Constructor donde se inicializan parámetros de interfaz gráfica
        """
        super(Stats, self).__init__()
        self.ui = Ui_StatsWindow()
        self.ui.setupUi(self)
        self.api = api()
        self.parking_id = parking_id
        self.main_context = main_context

        self.ui.txb_date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.btn_query.clicked.connect(lambda callback: self.plot_stat(self.ui.cbx_statistics.currentIndex(), self.ui.txb_date.date()))

        self.build_table()
        self.build_plot()

    def plot_stat(self, stat_id, date):

        if stat_id == 0:

            data = self.get_occupations(date.toString("yyyy-MM-dd"))

            x_axis = []
            y_axis = []

            for d in data:
                x_axis.append(d["Hora"])
                y_axis.append(d["Ocupaciones"])

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.bar(x_axis, y_axis)
            plt.xlim([0, 23])
            plt.xticks(np.arange(min(x_axis), max(x_axis) + 1, 1))
            self.canvas.draw()

            self.vlw_table.hide()
            self.vl_widget_plot.show()

        elif stat_id == 1:

            data = self.get_transactions(date.toString("yyyy-MM-dd"))
            self.tbl_transactions.setRowCount(len(data))
            row = 0

            for d in data:
                print(d)
                self.tbl_transactions.setItem(row, 0, QtWidgets.QTableWidgetItem(d["Placa"]))
                self.tbl_transactions.setItem(row, 1, QtWidgets.QTableWidgetItem(d["Clase"]))
                self.tbl_transactions.setItem(row, 2, QtWidgets.QTableWidgetItem(d["FechaEntrada"]))
                self.tbl_transactions.setItem(row, 3, QtWidgets.QTableWidgetItem(d["FechaSalida"]))
                self.tbl_transactions.setItem(row, 4, QtWidgets.QTableWidgetItem(str(d["Tiempo"])))
                self.tbl_transactions.setItem(row, 5, QtWidgets.QTableWidgetItem(str(d["Valor"])))
                self.tbl_transactions.setItem(row, 6, QtWidgets.QTableWidgetItem(d["Guid"]))

                row += 1

            self.tbl_transactions.repaint()

            self.vlw_table.show()
            self.vl_widget_plot.hide()

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

    def build_table(self):
        self.vlw_table = QtWidgets.QWidget(self.ui.plot_frame)
        self.vlw_table.setGeometry(QtCore.QRect(10, 10, 691, 421))
        self.vlw_table.setObjectName("vlw_table")

        self.vl_table = QtWidgets.QVBoxLayout(self.vlw_table)
        self.vl_table.setContentsMargins(0, 0, 0, 0)
        self.vl_table.setObjectName("vl_table")

        self.tbl_transactions = QtWidgets.QTableWidget(self.vlw_table)
        self.tbl_transactions.setObjectName("tbl_transactions")
        self.tbl_transactions.setColumnCount(7)

        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_transactions.setHorizontalHeaderItem(6, item)

        self.vl_table.addWidget(self.tbl_transactions)

        item = self.tbl_transactions.horizontalHeaderItem(0)
        item.setText("Placa")

        item = self.tbl_transactions.horizontalHeaderItem(1)
        item.setText("Clase")

        item = self.tbl_transactions.horizontalHeaderItem(2)
        item.setText("Entrada")

        item = self.tbl_transactions.horizontalHeaderItem(3)
        item.setText("Salida")

        item = self.tbl_transactions.horizontalHeaderItem(4)
        item.setText("Tiempo (min)")

        item = self.tbl_transactions.horizontalHeaderItem(5)
        item.setText("Valor ($)")

        item = self.tbl_transactions.horizontalHeaderItem(6)
        item.setText("Identificador")

        self.vlw_table.hide()

    def build_plot(self):

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.vl_widget_plot = QtWidgets.QWidget(self.ui.plot_frame)
        self.vl_widget_plot.setGeometry(QtCore.QRect(10, 10, 691, 421))
        self.vl_widget_plot.setObjectName("vl_widget_plot")

        self.vl_plot = QtWidgets.QVBoxLayout(self.vl_widget_plot)
        self.vl_plot.setContentsMargins(0, 0, 0, 0)
        self.vl_plot.setObjectName("vl_plot")

        self.toolbar = NavigationToolbar(self.canvas, self.vl_widget_plot)
        self.vl_plot.addWidget(self.toolbar)
        self.vl_plot.addWidget(self.canvas)

        self.vl_widget_plot.hide()

    def get_occupations(self, date):
        return self.api.get_occupations(self.parking_id, date)

    def get_transactions(self, date):
        return self.api.get_transactions(self.parking_id, date)








