import connexion
import six

from swagger_server.models.director import Director  # noqa: E501
from swagger_server import util


def directores_get():  # noqa: E501
    """Obtener todos los directores

     # noqa: E501


    :rtype: List[Director]
    """
    return 'do some magic!'


def directores_id_get(id):  # noqa: E501
    """Obtener director por id

     # noqa: E501

    :param id: Director por ID
    :type id: str

    :rtype: Director
    """
    return 'do some magic!'
