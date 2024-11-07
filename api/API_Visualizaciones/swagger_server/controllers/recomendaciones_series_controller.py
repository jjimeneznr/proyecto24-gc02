import connexion
import six

from swagger_server.models.recomendaciones_series import RecomendacionesSeries  # noqa: E501
from swagger_server import util


def recomendaciones_series_id_get(id):  # noqa: E501
    """Obtener las recomendaciones para un usario de series

     # noqa: E501

    :param id: ID de las recomendaciones de series
    :type id: str

    :rtype: RecomendacionesSeries
    """
    return 'do some magic!'
