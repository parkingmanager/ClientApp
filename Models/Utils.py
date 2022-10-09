import cv2
import numpy as np
import copy

# Negocio
from Bussiness.Models.DefinedSpace import DefinedSpace as DefinedSpace


class Utils:

    # Contenido de la imagen original
    content = []
    path = ""

    # Color detallado
    color = {'r': 255, 'g': 255, 'b': 255}

    def __init__(self, path):
        Utils.content = cv2.imread(path)
        Utils.Path = path

    @staticmethod
    def get_original_image_content():
        """
        Obtiene una copia de la imagen original.
        :return:
        """
        return copy.deepcopy(Utils.content)

    @staticmethod
    def set_original_image_content(content):
        """
        Obtiene una copia de la imagen original.
        :return:
        """
        Utils.content = copy.deepcopy(content)

    @staticmethod
    def get_line_color():
        """
        Retorna el color seleccionado
        :return:
        """
        return Utils.color

    @staticmethod
    def set_line_color(r, g, b):
        """
        Aplica el color seleccionado
        :param r:
        :param g:
        :param b:
        :return:
        """
        Utils.color["r"] = r
        Utils.color["g"] = g
        Utils.color["b"] = b

    @staticmethod
    def get_pixel_values(picture, x, y):
        """
            Extrae valores RGB y HSV de una imagen especificada para una coordenada
        """
        # Extrae canales de forma independiente
        b_ex, g_ex, r_ex = picture[:, :, 0], picture[:, :, 1], picture[:, :, 2]

        r_val = r_ex[y][x]
        g_val = g_ex[y][x]
        b_val = b_ex[y][x]

        # Conforma imagen rgb de 1px * 1px
        rgb = np.array([[[r_val, g_val, b_val]]])
        # Convierte el espacio de color H: 0 -> 179, S: 0 -> 255, V: -> 0 -> 255
        hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
        # Extrae valores pixel a pixel
        h_val = hsv[0][0][0]
        s_val = hsv[0][0][1]
        v_val = hsv[0][0][2]

        return r_val, g_val, b_val, h_val, s_val, v_val
