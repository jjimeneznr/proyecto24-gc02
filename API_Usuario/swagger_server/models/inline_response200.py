# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from .. import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, mensaje: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param mensaje: The mensaje of this InlineResponse200.  # noqa: E501
        :type mensaje: str
        """
        self.swagger_types = {
            'mensaje': str
        }

        self.attribute_map = {
            'mensaje': 'mensaje'
        }
        self._mensaje = mensaje

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mensaje(self) -> str:
        """Gets the mensaje of this InlineResponse200.


        :return: The mensaje of this InlineResponse200.
        :rtype: str
        """
        return self._mensaje

    @mensaje.setter
    def mensaje(self, mensaje: str):
        """Sets the mensaje of this InlineResponse200.


        :param mensaje: The mensaje of this InlineResponse200.
        :type mensaje: str
        """

        self._mensaje = mensaje
