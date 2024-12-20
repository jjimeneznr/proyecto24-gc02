# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Usuario(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, nombre: str=None, apellidos: str=None, correo: str=None, contrasea: str=None, imagen_perfil: str=None, metodo_pago: str=None, idioma: str=None, genero_favorito: str=None):  # noqa: E501
        """Usuario - a model defined in Swagger

        :param id: The id of this Usuario.  # noqa: E501
        :type id: str
        :param nombre: The nombre of this Usuario.  # noqa: E501
        :type nombre: str
        :param apellidos: The apellidos of this Usuario.  # noqa: E501
        :type apellidos: str
        :param correo: The correo of this Usuario.  # noqa: E501
        :type correo: str
        :param contrasea: The contrasea of this Usuario.  # noqa: E501
        :type contrasea: str
        :param imagen_perfil: The imagen_perfil of this Usuario.  # noqa: E501
        :type imagen_perfil: str
        :param metodo_pago: The metodo_pago of this Usuario.  # noqa: E501
        :type metodo_pago: str
        :param idioma: The idioma of this Usuario.  # noqa: E501
        :type idioma: str
        :param genero_favorito: The genero_favorito of this Usuario.  # noqa: E501
        :type genero_favorito: str
        """
        self.swagger_types = {
            'id': str,
            'nombre': str,
            'apellidos': str,
            'correo': str,
            'contrasea': str,
            'imagen_perfil': str,
            'metodo_pago': str,
            'idioma': str,
            'genero_favorito': str
        }

        self.attribute_map = {
            'id': 'id',
            'nombre': 'nombre',
            'apellidos': 'apellidos',
            'correo': 'correo',
            'contrasea': 'contraseña',
            'imagen_perfil': 'imagen_perfil',
            'metodo_pago': 'metodo_pago',
            'idioma': 'idioma',
            'genero_favorito': 'genero_favorito'
        }
        self._id = id
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._contrasea = contrasea
        self._imagen_perfil = imagen_perfil
        self._metodo_pago = metodo_pago
        self._idioma = idioma
        self._genero_favorito = genero_favorito

    @classmethod
    def from_dict(cls, dikt) -> 'Usuario':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Usuario of this Usuario.  # noqa: E501
        :rtype: Usuario
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Usuario.


        :return: The id of this Usuario.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Usuario.


        :param id: The id of this Usuario.
        :type id: str
        """

        self._id = id

    @property
    def nombre(self) -> str:
        """Gets the nombre of this Usuario.


        :return: The nombre of this Usuario.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this Usuario.


        :param nombre: The nombre of this Usuario.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def apellidos(self) -> str:
        """Gets the apellidos of this Usuario.


        :return: The apellidos of this Usuario.
        :rtype: str
        """
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos: str):
        """Sets the apellidos of this Usuario.


        :param apellidos: The apellidos of this Usuario.
        :type apellidos: str
        """

        self._apellidos = apellidos

    @property
    def correo(self) -> str:
        """Gets the correo of this Usuario.


        :return: The correo of this Usuario.
        :rtype: str
        """
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        """Sets the correo of this Usuario.


        :param correo: The correo of this Usuario.
        :type correo: str
        """

        self._correo = correo

    @property
    def contrasea(self) -> str:
        """Gets the contrasea of this Usuario.


        :return: The contrasea of this Usuario.
        :rtype: str
        """
        return self._contrasea

    @contrasea.setter
    def contrasea(self, contrasea: str):
        """Sets the contrasea of this Usuario.


        :param contrasea: The contrasea of this Usuario.
        :type contrasea: str
        """

        self._contrasea = contrasea

    @property
    def imagen_perfil(self) -> str:
        """Gets the imagen_perfil of this Usuario.

        URL de la imagen de perfil  # noqa: E501

        :return: The imagen_perfil of this Usuario.
        :rtype: str
        """
        return self._imagen_perfil

    @imagen_perfil.setter
    def imagen_perfil(self, imagen_perfil: str):
        """Sets the imagen_perfil of this Usuario.

        URL de la imagen de perfil  # noqa: E501

        :param imagen_perfil: The imagen_perfil of this Usuario.
        :type imagen_perfil: str
        """

        self._imagen_perfil = imagen_perfil

    @property
    def metodo_pago(self) -> str:
        """Gets the metodo_pago of this Usuario.

        Método de pago del usuario (tarjeta de crédito, PayPal...)  # noqa: E501

        :return: The metodo_pago of this Usuario.
        :rtype: str
        """
        return self._metodo_pago

    @metodo_pago.setter
    def metodo_pago(self, metodo_pago: str):
        """Sets the metodo_pago of this Usuario.

        Método de pago del usuario (tarjeta de crédito, PayPal...)  # noqa: E501

        :param metodo_pago: The metodo_pago of this Usuario.
        :type metodo_pago: str
        """

        self._metodo_pago = metodo_pago

    @property
    def idioma(self) -> str:
        """Gets the idioma of this Usuario.

        Idioma preferido del usuario (\"español\", \"inglés\", \"portugués\"...)  # noqa: E501

        :return: The idioma of this Usuario.
        :rtype: str
        """
        return self._idioma

    @idioma.setter
    def idioma(self, idioma: str):
        """Sets the idioma of this Usuario.

        Idioma preferido del usuario (\"español\", \"inglés\", \"portugués\"...)  # noqa: E501

        :param idioma: The idioma of this Usuario.
        :type idioma: str
        """

        self._idioma = idioma

    @property
    def genero_favorito(self) -> str:
        """Gets the genero_favorito of this Usuario.

        Género favorito del usuario  # noqa: E501

        :return: The genero_favorito of this Usuario.
        :rtype: str
        """
        return self._genero_favorito

    @genero_favorito.setter
    def genero_favorito(self, genero_favorito: str):
        """Sets the genero_favorito of this Usuario.

        Género favorito del usuario  # noqa: E501

        :param genero_favorito: The genero_favorito of this Usuario.
        :type genero_favorito: str
        """

        self._genero_favorito = genero_favorito
