import connexion
import six

from swagger_server.models.id_contrasea_body import IdContraseaBody  # noqa: E501
from swagger_server.models.id_correo_body import IdCorreoBody  # noqa: E501
from swagger_server.models.id_generofavorito_body import IdGenerofavoritoBody  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server.models.usuarios_body import UsuariosBody  # noqa: E501
from swagger_server.models.usuarios_id_body import UsuariosIdBody  # noqa: E501
from swagger_server import util


def usuarios_id_contrasea_put(body, id):  # noqa: E501
    """Actualizar la contraseña del usuario

     # noqa: E501

    :param body: Nueva contraseña del usuario
    :type body: dict | bytes
    :param id: ID del usuario
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = IdContraseaBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_id_correo_put(body, id):  # noqa: E501
    """Actualizar el correo del usuario

     # noqa: E501

    :param body: Nuevo correo electrónico del usuario
    :type body: dict | bytes
    :param id: ID del usuario
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = IdCorreoBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_id_delete(id, contrasea):  # noqa: E501
    """Eliminar un usuario

    Elimina un usuario existente identificado por su ID y su contraseña. # noqa: E501

    :param id: ID del usuario a eliminar
    :type id: str
    :param contrasea: Contraseña del usuario para confirmar la eliminación
    :type contrasea: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def usuarios_id_genero_favorito_put(body, id):  # noqa: E501
    """Actualizar el género favorito de un usuario

     # noqa: E501

    :param body: Nuevo género favorito
    :type body: dict | bytes
    :param id: ID del usuario a actualizar
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = IdGenerofavoritoBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_id_get(id):  # noqa: E501
    """Obtener un usuario por ID

     # noqa: E501

    :param id: ID del usuario a obtener
    :type id: str

    :rtype: Usuario
    """
    return 'do some magic!'


def usuarios_id_put(body, id):  # noqa: E501
    """Actualizar el nombre de usuario

     # noqa: E501

    :param body: Nuevo nombre completo del usuario
    :type body: dict | bytes
    :param id: ID del usuario
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = UsuariosIdBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_post(body):  # noqa: E501
    """Crear un nuevo usuario

     # noqa: E501

    :param body: Datos necesarios para crear un nuevo usuario
    :type body: dict | bytes

    :rtype: Usuario
    """
    if connexion.request.is_json:
        body = UsuariosBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
