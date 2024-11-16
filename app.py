from flask import Flask, render_template
from flask import Flask, Blueprint
import connexion
from api.API_Contenidos.swagger_server import contenidos_blueprint
from api.API_Usuario.swagger_server import usuarios_blueprint
from api.API_Visualizaciones.swagger_server import visualizaciones_blueprint


app = Flask(__name__)


# Registrar cada API con un prefijo de URL
app.register_blueprint(contenidos_blueprint, url_prefix='/api/contenidos')
app.register_blueprint(usuarios_blueprint, url_prefix='/api/usuarios')
app.register_blueprint(visualizaciones_blueprint, url_prefix='/api/visualizaciones')

@app.route('/') #Al hacer python app.py hay que poner en la ruta /Inicio
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
