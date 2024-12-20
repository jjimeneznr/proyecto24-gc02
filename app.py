from flask import Flask, render_template
from flask import Flask, Blueprint
from flask import redirect, url_for
from flask import request, session,jsonify
import requests
import connexion
from api.API_Contenidos.swagger_server import contenidos_blueprint
from api.API_Usuario.swagger_server.controllers import usuarios_controller
from api.API_Visualizaciones.swagger_server import visualizaciones_blueprint

app = Flask(__name__)




if __name__ == '__main__':
    app.run(debug=True)
