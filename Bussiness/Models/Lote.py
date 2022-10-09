import json
import datetime
from Bussiness.Models.DefinedSpace import DefinedSpace as DefinedSpace


class Lote:

    def __init__(self):
        self.IdLote = None
        self.Nombre = ""
        self.Identificador = ""
        self.Token = ""
        self.Direccion = ""
        self.FuenteVideo = ""
        self.RutaModelo = ""
        self.EspaciosDelimitados: list = []

    def add_defined_space(self, defined_space: DefinedSpace):
        """
        Agrega un espacio delimitado a la calibración
        :param defined_space:
        :return:
        """
        self.EspaciosDelimitados.append(defined_space)

    def update_property(self, parameter, value):
        """
        Actualización dinámica de propiedades de la clase externamente
        :param parameter:
        :param value:
        :return:
        """
        attr = getattr(self, parameter)
        setattr(self, parameter, value)

    def get_dict(self):

        dict = {
            "IdLote": self.IdLote,
            "Nombre": self.Nombre,
            "Identificador": self.Identificador,
            "Token": self.Token,
            "Direccion": self.Direccion,
            "FuenteVideo": self.FuenteVideo,
            "RutaModelo": self.RutaModelo,
            "EspaciosDelimitados": []
        }

        for ds in self.EspaciosDelimitados:
            dict["EspaciosDelimitados"].append(ds.__dict__)

        return dict

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
