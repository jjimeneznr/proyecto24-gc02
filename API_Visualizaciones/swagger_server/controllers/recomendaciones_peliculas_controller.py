import connexion
import six

from swagger_server.models.recomendaciones_peliculas import RecomendacionesPeliculas  # noqa: E501
from swagger_server import util


def recomendaciones_peliculas_id_get(id):  # noqa: E501
    """Obtener las recomendaciones para un usario de películas

     # noqa: E501

    :param id: ID de las recomendaciones de peliculas
    :type id: str

    :rtype: RecomendacionesPeliculas
    """
    return 'do some magic!'
