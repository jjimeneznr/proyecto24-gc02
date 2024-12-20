import connexion
import six

from swagger_server.models.capitulo import Capitulo  # noqa: E501
from swagger_server import util


def series_id_temporadas_temporada_id_capitulos_get(id, temporada_id):  # noqa: E501
    """Obtener todos los capítulos de una temporada específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str
    :param temporada_id: ID de la temporada
    :type temporada_id: str

    :rtype: List[Capitulo]
    """
    return 'do some magic!'
