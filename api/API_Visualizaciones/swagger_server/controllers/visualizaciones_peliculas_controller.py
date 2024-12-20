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


def visualizaciones_peliculas_id_put(body, id):  # noqa: E501
    """Actualizar las visualizaciones de una película

     # noqa: E501

    :param body: Datos para actualizar las visualizaciones de la película
    :type body: dict | bytes
    :param id: ID de las visualizaciones de una película
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = VisualizacionesPeliculas.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
