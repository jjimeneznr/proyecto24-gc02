import connexion
import six

from swagger_server.models.id_contrasea_body import IdContraseaBody  # noqa: E501
from swagger_server.models.id_correo_body import IdCorreoBody  # noqa: E501
from swagger_server.models.id_generosfavoritos_body import IdGenerosfavoritosBody  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server.models.usuarios_body import UsuariosBody  # noqa: E501
from swagger_server.models.usuarios_id_body import UsuariosIdBody  # noqa: E501
from swagger_server import util

from flask import request, jsonify
from werkzeug.security import generate_password_hash
from swagger_server.models.usuario import Usuario

from . import dbconnection




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


def usuarios_id_generos_favoritos_put(body, id):  # noqa: E501
    """Actualizar los géneros favoritos de un usuario

     # noqa: E501

    :param body: Lista de nuevos géneros favoritos (máximo 4)
    :type body: dict | bytes
    :param id: ID del usuario a actualizar
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = IdGenerosfavoritosBody.from_dict(connexion.request.get_json())  # noqa: E501
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
    data = request.get_json()
    firstname = data.get("firstname")
    secondname = data.get("secondname")
    correo = data.get("correo")
    password1 = data.get("password1")
    password2 = data.get("password2")

    # Validar los datos
    if not firstname or not secondname or not correo or not password1 or not password2:
        return jsonify({"error": "Faltan datos"}), 400

    # Crear el nuevo usuario
    nuevo_usuario = dbconnection.dbSignUp( correo=correo,firstname=firstname,secondname=secondname, password=password1,password=password2)
    



