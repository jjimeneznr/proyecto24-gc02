# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.id_contrasea_body import IdContraseaBody  # noqa: E501
from swagger_server.models.id_correo_body import IdCorreoBody  # noqa: E501
from swagger_server.models.id_generosfavoritos_body import IdGenerosfavoritosBody  # noqa: E501
from swagger_server.models.pelicula import Pelicula  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server.models.usuarios_body import UsuariosBody  # noqa: E501
from swagger_server.models.usuarios_id_body import UsuariosIdBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsuariosController(BaseTestCase):
    """UsuariosController integration test stubs"""

    def test_usuarios_id_buscar_pelicula_get(self):
        """Test case for usuarios_id_buscar_pelicula_get

        Buscar una película por nombre
        """
        query_string = [('nombre', 'nombre_example')]
        response = self.client.open(
            '/usuarios/{id}/buscar-pelicula'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_buscar_pelicula_por_genero_get(self):
        """Test case for usuarios_id_buscar_pelicula_por_genero_get

        Buscar películas por género
        """
        query_string = [('genero', 'genero_example')]
        response = self.client.open(
            '/usuarios/{id}/buscar-pelicula-por-genero'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_contrasea_put(self):
        """Test case for usuarios_id_contrasea_put

        Actualizar la contraseña del usuario
        """
        body = IdContraseaBody()
        response = self.client.open(
            '/usuarios/{id}/contraseña'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_correo_put(self):
        """Test case for usuarios_id_correo_put

        Actualizar el correo del usuario
        """
        body = IdCorreoBody()
        response = self.client.open(
            '/usuarios/{id}/correo'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_generos_favoritos_put(self):
        """Test case for usuarios_id_generos_favoritos_put

        Actualizar los géneros favoritos de un usuario
        """
        body = IdGenerosfavoritosBody()
        response = self.client.open(
            '/usuarios/{id}/generos-favoritos'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_get(self):
        """Test case for usuarios_id_get

        Obtener un usuario por ID
        """
        response = self.client.open(
            '/usuarios/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_put(self):
        """Test case for usuarios_id_put

        Actualizar el nombre de usuario
        """
        body = UsuariosIdBody()
        response = self.client.open(
            '/usuarios/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_post(self):
        """Test case for usuarios_post

        Crear un nuevo usuario
        """
        body = UsuariosBody()
        response = self.client.open(
            '/usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
