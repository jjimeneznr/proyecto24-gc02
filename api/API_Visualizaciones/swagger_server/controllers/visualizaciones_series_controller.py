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
