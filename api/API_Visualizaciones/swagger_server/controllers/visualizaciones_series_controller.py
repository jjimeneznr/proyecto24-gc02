import connexion
import six

from swagger_server.models.visualizaciones_series import VisualizacionesSeries  # noqa: E501
from swagger_server import util


def visualizaciones_series_id_get(id):  # noqa: E501
    """Obtener las visualizaciones de una Serie

     # noqa: E501

    :param id: ID de las visualizaciones de una serie
    :type id: str

    :rtype: VisualizacionesSeries
    """
    return 'do some magic!'


def visualizaciones_series_id_put(body, id):  # noqa: E501
    """Actualizar las visualizaciones de una serie

     # noqa: E501

    :param body: Datos para actualizar las visualizaciones de la serie
    :type body: dict | bytes
    :param id: ID de las visualizaciones de una serie
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = VisualizacionesSeries.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
