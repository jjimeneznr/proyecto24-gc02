import connexion
import six

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server import util


def actores_get():  # noqa: E501
    """Obtener todos los actores

     # noqa: E501


    :rtype: List[Actor]
    """
    return 'do some magic!'


def actores_id_get(id):  # noqa: E501
    """Obtener actor por id

     # noqa: E501

    :param id: Actor Correspondiente a ese id
    :type id: str

    :rtype: Actor
    """
    return 'do some magic!'
