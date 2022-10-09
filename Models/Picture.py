import cv2


class Picture:

    def __init__(self):
        """
        Crea instancia y atributos de la misma
        :param path: Path de la imagen cargada
        """
        self.path = ""
        self.content = []

    def create_picture_from_path(self, path: str):
        """
        Lee la imagen y la carga en memoria
        :param path: Path de la imagen cargada
        """
        self.path = path
        self.content = []
        try:
            self.content = cv2.imread(path)
        except Exception as ex:
            raise Exception(ex)

    def create_picture_from_content(self, content: list):
        """
        Conforma el objeto a partir de un contenido especifico
        :param content:
        :return:
        """
        self.content = content
        self.path = ""
