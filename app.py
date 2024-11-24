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


# Registrar cada API con un prefijo de URL
app.register_blueprint(contenidos_blueprint, url_prefix='/api/contenidos')
app.register_blueprint(visualizaciones_blueprint, url_prefix='/api/visualizaciones')

@app.route('/') #Al hacer python app.py hay que poner en la ruta /Inicio
def index():
    return render_template('login.html')


@app.route('/registro_post', methods=['POST'])
def registro_post():
    nombre = request.form.get('nombre')
    apellidos=request.form.get('apellidos')
    correo=request.form.get('email')
    password1=request.form.get('password')
    password2=request.form.get('confirm-password')
    
    if password1 == password2:
        body = {
            "firstname": nombre,
            "secondname": apellidos,
            "correo": correo,
            "password1": password1,
            "password2": password2
            }
    else:
        return redirect(url_for('registro'))
    
    try:
            response = usuarios_controller.usuarios_post(body)
            return redirect(url_for('index')) 
    except Exception as e:
            return redirect(url_for('registro')) 
      
    
@app.route('/registro', methods=['GET'])
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
