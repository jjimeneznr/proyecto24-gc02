import connexion
import six

from swagger_server.models.temporada import Temporada  # noqa: E501
from swagger_server import util


def series_id_temporadas_get(id):  # noqa: E501
    """Obtener todas las temporadas de una serie

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Temporada]
    """
    return 'do some magic!'
