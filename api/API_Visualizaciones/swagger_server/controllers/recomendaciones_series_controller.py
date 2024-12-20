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


def recomendaciones_series_id_put(body, id):  # noqa: E501
    """Actualizar las recomendaciones de series

     # noqa: E501

    :param body: Datos para actualizar las recomendaciones de series
    :type body: dict | bytes
    :param id: ID de las recomendaciones de series
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = RecomendacionesSeries.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
