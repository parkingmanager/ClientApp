import requests
from Models.Usuario import *
import json


class ParkingApi:
    base_api = "http://127.0.0.1/ParkingApi/api/"

    def get_user(self, userid) -> Usuario:
        """
        Consulta un usuario especifico en el api
        :param userid:
        :return: Usuario
        """

        try:
            r = requests.get(self.base_api + f'usuario/{userid}')

            if r.status_code == 200:
                return Usuario(r.json())
        except:
            ex = "Error al consultar usuario -> Http_response: " + r.status_code
            raise Exception(ex)

    def create_parking(self, parking):

        try:
            headers = {'Content-type': 'application/json'}

            r = requests.post(self.base_api + f'CrearLote', data=json.dumps(parking), headers=headers)

            if r.status_code == 201:
                return r.json()
            else:
                raise Exception()
        except:
            ex = "Error al crear el lote -> Http_response: " + r.status_code
            raise Exception(ex)

    def get_parking(self, parking_id):
        try:
            r = requests.get(self.base_api + f'ConsultarLote/{parking_id}')

            if r.status_code == 200:
                return r.json()
        except:
            ex = "Error al consultar el lote -> Http_response: " + r.status_code
            raise Exception(ex)

    def get_parkings(self):
        try:
            r = requests.get(self.base_api + f'ConsultarLotes')

            if r.status_code == 200:
                return r.json()
        except:
            ex = "Error al consultar los lotes -> Http_response: " + r.status_code
            raise Exception(ex)

    def delete_parking(self, parking_id):
        try:

            print(parking_id)

            r = requests.delete(self.base_api + f'EliminarLote/{parking_id}')

            if r.status_code == 200:
                return True
            else:
                return False
        except:
            ex = "Error al eliminar el lote -> Http_response: " + r.status_code
            raise Exception(ex)

    def update_parking(self, parking):

        try:
            headers = {'Content-type': 'application/json'}

            r = requests.post(self.base_api + f'ActualizarLote', data=json.dumps(parking), headers=headers)

            if r.status_code == 200:
                return r.json()
            else:
                raise Exception()
        except:
            ex = "Error al actualizar el lote -> Http_response: " + r.status_code
            raise Exception(ex)

    def register_transaction(self, vehicle_transaction):

        try:
            headers = {'Content-type': 'application/json'}

            r = requests.post(self.base_api + f'Transaccion', data=json.dumps(vehicle_transaction), headers=headers)

            if r.status_code == 200 or r.status_code == 201:
                return r.json()
            else:
                raise Exception()
        except:
            ex = "Error registrar la transacción  -> Http_response: " + r.status_code
            raise Exception(ex)

    def register_monitoring(self, monitorings: list):

        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(self.base_api + f'GuardarMonitoreos', data=json.dumps(monitorings), headers=headers)

            if r.status_code not in [200, 201, 204]:
                raise Exception()
        except:
            ex = "Error registrar el monitoreo  -> Http_response: " + r.status_code
            raise Exception(ex)

    def get_occupations(self, parking_id, date):
        try:
            r = requests.get(self.base_api + f'estadisticas/ocupaciones/{parking_id}/{date}')

            if r.status_code == 200:
                return r.json()
        except:
            ex = "Error al consultar las ocupaciones -> Http_response: " + r.status_code
            raise Exception(ex)

    def get_transactions(self, parking_id, date):
        try:
            r = requests.get(self.base_api + f'estadisticas/transacciones/{parking_id}/{date}')

            if r.status_code == 200:
                return r.json()
        except:
            ex = "Error al consultar las transacciones -> Http_response: " + r.status_code
            raise Exception(ex)
