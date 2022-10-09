import json

from Bussiness.Models import VehicleTransaction
from QTGraphicInterfaces.VehicleForm import Ui_VehicleForm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# Comunicaciones
from Integration.ParkingApi import ParkingApi as api


class TransactionsForm(QtWidgets.QMainWindow):

    def __init__(self, transaction_context, info: VehicleTransaction, parking_id: int):

        """
            Constructor donde se inicializan parámetros de interfaz gráfica
        """
        super(TransactionsForm, self).__init__()
        self.ui = Ui_VehicleForm()
        self.ui.setupUi(self)
        self.api = api()
        self.vehicle_info = VehicleTransaction.VehicleTransaction()
        self.vehicle_info.IdLote = parking_id
        self.transaction_context = transaction_context
        self.ui.btn_ok.clicked.connect(lambda callback: self.save())
        self.ui.btn_cancel.clicked.connect(lambda callback: self.close())

        # Parámetros iniciales
        if info is not None:

            self.vehicle_info: VehicleTransaction = info
            self.ui.txb_plate.setText(TransactionsForm.check_if_valid_param(info.Placa))
            self.ui.txb_class.setText(TransactionsForm.check_if_valid_param(info.Clase))
            self.ui.txb_brand.setText(TransactionsForm.check_if_valid_param(info.Marca))
            self.ui.txb_line.setText(TransactionsForm.check_if_valid_param(info.Linea))
            self.ui.txb_model.setText(TransactionsForm.check_if_valid_param(info.Modelo))
            self.ui.txb_color.setText(TransactionsForm.check_if_valid_param(info.Color))

    def save(self):
        self.vehicle_info.Placa = self.ui.txb_plate.text()
        self.vehicle_info.Clase = self.ui.txb_class.text()
        self.vehicle_info.Marca = self.ui.txb_brand.text()
        self.vehicle_info.Linea = self.ui.txb_line.text()
        self.vehicle_info.Modelo = self.ui.txb_model.text()
        self.vehicle_info.Color = self.ui.txb_color.text()

        # Validación de placa
        if self.vehicle_info.Placa is None or not self.vehicle_info.Placa:
            self.show_dialog("Error", "El campo placa es requerido")
        else:
            self.register_transaction(self.vehicle_info)

    def show_dialog(self, title, message):
        QMessageBox.about(self, title, message)

    def register_transaction(self, data):

        resume = self.api.register_transaction(data.get_dict())

        if resume["FechaSalida"] is None:
            text = \
    f"""
-------------------------------
    {resume["NombreLote"]}
    {resume["DireccionLote"]}
-------------------------------
    Comprobante de entrada
{resume["Guid"][0:30]}	

  Entrada: {resume["FechaEntrada"]} 
  Placa: {resume["Placa"]}
  Tarifa por fracción: ${resume["TarifaFraccion"]}  
-------------------------------
    Tarifa especial {resume["FraccionMinimaPrecioFijo"]} min
           $ {resume["TarifaFija"]} 
-------------------------------
        """
        else:
            text = \
        f"""
-------------------------------
    {resume["NombreLote"]}
    {resume["DireccionLote"]}
-------------------------------
          Transacción
{resume["Guid"][0:30]}	

  Entrada: {resume["FechaEntrada"]}
  Salida: {resume["FechaSalida"]}
  Placa: {resume["Placa"]}
  Tarifa por fracción: ${resume["TarifaFraccion"]}
  Permanencia : {resume["Tiempo"]} minutos
  Valor: ${resume["Valor"]}
-------------------------------
    Tarifa especial {resume["FraccionMinimaPrecioFijo"]} min
           $ {resume["TarifaFija"]}
  Tiene 15 minutos para salir
El tiempo excedido genera cobro
    
    Gracias por su Visita!
-------------------------------
        """
        self.transaction_context.print_transaction(text)
        self.close()

    @staticmethod
    def check_if_valid_param(value):
        if value:
            return value
        else:
            return ""