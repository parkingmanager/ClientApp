from Filters.Filter import FilterTypes
from QTGraphicInterfaces.DynamicMainInterfaceForm import Ui_MainWindow as Ui
from Models.Picture import Picture as Pic
from Filters.Color import Color as Col
from Filters.Delimite import Delimite as De
from Filters.Transform import Transform as Tr
from Filters.TPerspective import TPerspective as Tp
from Filters.SpaceConfig import SpaceConfig as Sc


class FactoryFilter:
    ui: Ui
    picture: Pic

    def __init__(self, picture, ui):
        self.ui = ui
        self.picture = picture

    def create_filter(self, filter_id, row, col, widget_id, last_filter, coordinates, context):
        """
        Construye instancias de filtros
        :param filter_id:
        :param row:
        :param col:
        :param widget_id:
        :param last_filter:
        :param coordinates:
        :param context:
        :return:
        """

        if filter_id == FilterTypes.Color:
            return Col(self.picture.content, self.ui, row, col, widget_id)
        elif filter_id == FilterTypes.Delimite:
            return De(self.picture.content, self.ui, row, col, widget_id)
        elif filter_id == FilterTypes.Transformation:
            return Tr(self.picture.content, self.ui, row, col, widget_id)
        elif filter_id == FilterTypes.PerspectiveTransformation:
            return Tp(self.picture.content, self.ui, row, col, widget_id, coordinates)
        elif filter_id == FilterTypes.SpaceConfig:
            return Sc(self.picture.content, self.ui, row, col, widget_id, context)
        else:
            raise Exception('No se pudo crear el filtro solicitado porque no existe en la enumeración')


