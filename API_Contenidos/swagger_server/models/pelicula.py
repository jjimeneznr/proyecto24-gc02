# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from ..models.actor import Actor  # noqa: F401,E501
from ..models.director import Director  # noqa: F401,E501
from .. import util


class Pelicula(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, titulo: str=None, genero: str=None, descripcion: str=None, director: Director=None, actores: List[Actor]=None, duracion: str=None):  # noqa: E501
        """Pelicula - a model defined in Swagger

        :param id: The id of this Pelicula.  # noqa: E501
        :type id: str
        :param titulo: The titulo of this Pelicula.  # noqa: E501
        :type titulo: str
        :param genero: The genero of this Pelicula.  # noqa: E501
        :type genero: str
        :param descripcion: The descripcion of this Pelicula.  # noqa: E501
        :type descripcion: str
        :param director: The director of this Pelicula.  # noqa: E501
        :type director: Director
        :param actores: The actores of this Pelicula.  # noqa: E501
        :type actores: List[Actor]
        :param duracion: The duracion of this Pelicula.  # noqa: E501
        :type duracion: str
        """
        self.swagger_types = {
            'id': str,
            'titulo': str,
            'genero': str,
            'descripcion': str,
            'director': Director,
            'actores': List[Actor],
            'duracion': str
        }

        self.attribute_map = {
            'id': 'id',
            'titulo': 'titulo',
            'genero': 'genero',
            'descripcion': 'descripcion',
            'director': 'director',
            'actores': 'actores',
            'duracion': 'duracion'
        }
        self._id = id
        self._titulo = titulo
        self._genero = genero
        self._descripcion = descripcion
        self._director = director
        self._actores = actores
        self._duracion = duracion

    @classmethod
    def from_dict(cls, dikt) -> 'Pelicula':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pelicula of this Pelicula.  # noqa: E501
        :rtype: Pelicula
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Pelicula.


        :return: The id of this Pelicula.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Pelicula.


        :param id: The id of this Pelicula.
        :type id: str
        """

        self._id = id

    @property
    def titulo(self) -> str:
        """Gets the titulo of this Pelicula.


        :return: The titulo of this Pelicula.
        :rtype: str
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        """Sets the titulo of this Pelicula.


        :param titulo: The titulo of this Pelicula.
        :type titulo: str
        """

        self._titulo = titulo

    @property
    def genero(self) -> str:
        """Gets the genero of this Pelicula.


        :return: The genero of this Pelicula.
        :rtype: str
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """Sets the genero of this Pelicula.


        :param genero: The genero of this Pelicula.
        :type genero: str
        """

        self._genero = genero

    @property
    def descripcion(self) -> str:
        """Gets the descripcion of this Pelicula.


        :return: The descripcion of this Pelicula.
        :rtype: str
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        """Sets the descripcion of this Pelicula.


        :param descripcion: The descripcion of this Pelicula.
        :type descripcion: str
        """

        self._descripcion = descripcion

    @property
    def director(self) -> Director:
        """Gets the director of this Pelicula.


        :return: The director of this Pelicula.
        :rtype: Director
        """
        return self._director

    @director.setter
    def director(self, director: Director):
        """Sets the director of this Pelicula.


        :param director: The director of this Pelicula.
        :type director: Director
        """

        self._director = director

    @property
    def actores(self) -> List[Actor]:
        """Gets the actores of this Pelicula.


        :return: The actores of this Pelicula.
        :rtype: List[Actor]
        """
        return self._actores

    @actores.setter
    def actores(self, actores: List[Actor]):
        """Sets the actores of this Pelicula.


        :param actores: The actores of this Pelicula.
        :type actores: List[Actor]
        """

        self._actores = actores

    @property
    def duracion(self) -> str:
        """Gets the duracion of this Pelicula.


        :return: The duracion of this Pelicula.
        :rtype: str
        """
        return self._duracion

    @duracion.setter
    def duracion(self, duracion: str):
        """Sets the duracion of this Pelicula.


        :param duracion: The duracion of this Pelicula.
        :type duracion: str
        """

        self._duracion = duracion
