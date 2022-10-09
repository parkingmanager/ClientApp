class Usuario:

    IdUsuario = ''
    Nombres = ''
    Apellidos = ''
    Identificacion = ''
    Email = ''
    Contrasena = ''
    IdRol = ''
    FechaCreacion = ''
    Eliminado = ''

    def __init__(self, data):
        self.IdUsuario = 0

        for key in data:
            if data[key] is not None:
                setattr(self, key, data[key])
