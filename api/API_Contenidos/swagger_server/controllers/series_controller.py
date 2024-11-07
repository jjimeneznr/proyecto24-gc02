import connexion
import six

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.director import Director  # noqa: E501
from swagger_server.models.serie import Serie  # noqa: E501
from swagger_server import util


def series_genero_genero_get(genero):  # noqa: E501
    """Obtener una serie por genero

     # noqa: E501

    :param genero: Series con el genero a buscar
    :type genero: str

    :rtype: List[Serie]
    """
    return 'do some magic!'


def series_get():  # noqa: E501
    """Obtener todas las series

     # noqa: E501


    :rtype: List[Serie]
    """
    return 'do some magic!'


def series_id_actores_get(id):  # noqa: E501
    """Obtener actores de una serie específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Actor]
    """
    return 'do some magic!'


def series_id_directores_get(id):  # noqa: E501
    """Obtener los directores de una serie específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Director]
    """
    return 'do some magic!'


def series_id_get(id):  # noqa: E501
    """Obtener una serie por ID

     # noqa: E501

    :param id: ID de la serie a buscar
    :type id: str

    :rtype: Serie
    """
    return 'do some magic!'


def series_titulo_titulo_get(titulo):  # noqa: E501
    """Obtener una serie por Nombre

     # noqa: E501

    :param titulo: Serie con el nombre a buscar
    :type titulo: str

    :rtype: List[Serie]
    """
    return 'do some magic!'
