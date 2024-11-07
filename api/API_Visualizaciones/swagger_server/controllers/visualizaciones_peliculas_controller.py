import connexion
import six

from swagger_server.models.visualizaciones_peliculas import VisualizacionesPeliculas  # noqa: E501
from swagger_server import util


def visualizaciones_peliculas_id_get(id):  # noqa: E501
    """las visualizaciones de una pelicula

     # noqa: E501

    :param id: ID de las visualizaciones de una película
    :type id: str

    :rtype: VisualizacionesPeliculas
    """
    return 'do some magic!'
