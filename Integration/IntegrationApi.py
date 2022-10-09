import requests
import json


class IntegrationApi:

    def __init__(self):
        self.base_api = "http://127.0.0.1/ParkingApi/api/"
        self.headers = {'Content-Type': 'application/json'}

    def set_header(self, key, value):
        """
        Añade un header al request
        :param key:
        :param value:
        :return:
        """
        self.headers[key] = value

    def get(self, path):
        """
        Request GET genérico.
        :param path:
        :return:
        """
        try:
            r = requests.get(self.base_api + path, headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                ex = f"Error en petición GET: {r.status_code} - {r.reason}"
                raise Exception(ex)
        except Exception as e:
            raise Exception(e)

    def post(self, path, data: object):
        """
        Request POST genérico
        :param path:
        :param data:
        :return:
        """
        try:
            r = requests.post(self.base_api + path, json=data)
            if r.status_code == 200:
                return r.json()
            else:
                ex = f"Error en petición GET: {r.status_code} - {r.reason}"
                raise Exception(ex)
        except Exception as e:
            raise Exception(e)

    # def request_get(self, atributeid) -> Atributo:
    #     """
    #     Consulta  especifica en el api
    #     :param userid:
    #     """
    #     try:
    #         r = requests.get(self.base_api + self.Atributo.base_atribute+f'{atributeid}')
    #         if r.status_code == 200:
    #             EXT=r.json()
    #             print(EXT)
    #             return Atributo(r.json())
    #     except:
    #         ex = "Error al consultar-> HttpResponsed: " + r.status_code
    #         raise Exception(ex)

    # def request_post(self, package_json) -> Atributo:
    #     """
    #     Enviar datos
    #     :param package_json: Paquete de datos enviado al API
    #     """
    #     try:
    #         r = requests.post(self.base_api + self.Atributo.base_atribute,package_json)
    #         if r.status_code == 200:
    #             EXT=r.json()
    #             print(EXT)
    #             return Atributo(r.json())
    #     except:
    #         ex = "Error al ingresar datos -> HttpResponsed: " + r.status_code
    #         raise Exception(ex)
    #
    # def request_delete(self, atribute_id) -> Atributo:
    #     """
    #     Elimina ID especifico
    #     """
    #     try:
    #         r = requests.delete(self.base_api + self.Atributo.base_atribute+f'{atribute_id}')
    #         if r.status_code == 200:
    #             EXT=r.json()
    #             print(EXT)
    #             return Atributo(r.json())
    #     except:
    #         ex = "Error al eliminar-> HttpResponsed: " + r.status_code
    #         raise Exception(ex)
