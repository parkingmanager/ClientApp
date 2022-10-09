import json
import datetime
from Bussiness.Models.DefinedSpace import DefinedSpace as DefinedSpace


class Monitoring:

    def __init__(self, id_defined_space, state, date):
        self.IdEspacioDelimitado: int = id_defined_space
        self.Estado: bool = state
        self.Fecha: str = date

    def get_dict(self):

        dict = {
            "IdEspacioDelimitado": self.IdEspacioDelimitado,
            "Estado": self.Estado,
            "Fecha": self.Fecha
        }

        return dict
