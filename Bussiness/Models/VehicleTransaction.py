import json


class VehicleTransaction:

    def __init__(self):
        self.IdLote: int = 0
        self.Placa: str = ""
        self.Marca: str = None
        self.Linea: str = None
        self.Modelo: str = None
        self.Clase: str = None
        self.Color: str = None
        self.NumeroMotor: str = None
        self.Vin: str = None
        self.TipoTransaccion: str = None

    def get_dict(self):

        dict = {
            "IdLote": self.IdLote,
            "Placa": self.Placa,
            "Marca": self.Marca,
            "Linea": self.Linea,
            "Modelo": self.Modelo,
            "Clase": self.Clase,
            "Color": self.Color,
            "NumeroMotor": self.NumeroMotor,
            "Vin": self.Vin,
            "TipoTransaccion": self.TipoTransaccion,
        }

        return dict

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



