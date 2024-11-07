import connexion
import six

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.director import Director  # noqa: E501
from swagger_server.models.pelicula import Pelicula  # noqa: E501
from swagger_server import util


def peliculas_genero_genero_get(genero):  # noqa: E501
    """Obtener todas las películas

     # noqa: E501

    :param genero: ID de la pelicula a buscar
    :type genero: str

    :rtype: List[Pelicula]
    """
    return 'do some magic!'


def peliculas_get():  # noqa: E501
    """Obtener todas las películas

     # noqa: E501


    :rtype: List[Pelicula]
    """
    return 'do some magic!'


def peliculas_id_actores_get(id):  # noqa: E501
    """Obtener los actores de una película específica

     # noqa: E501

    :param id: ID de la película
    :type id: str

    :rtype: List[Actor]
    """
    return 'do some magic!'


def peliculas_id_directores_get(id):  # noqa: E501
    """Obtener los directores de una película específica

     # noqa: E501

    :param id: ID de la película
    :type id: str

    :rtype: List[Director]
    """
    return 'do some magic!'


def peliculas_id_get(id):  # noqa: E501
    """Obtener una pelicula por id

     # noqa: E501

    :param id: ID de la pelicula a buscar
    :type id: str

    :rtype: Pelicula
    """
    return 'do some magic!'


def peliculas_titulo_titulo_get(titulo):  # noqa: E501
    """Obtener todas las películas que contengan el título

     # noqa: E501

    :param titulo: Título parcial de la película a buscar
    :type titulo: str

    :rtype: List[Pelicula]
    """
    return 'do some magic!'
