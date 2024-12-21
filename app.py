from flask import Flask, render_template
from flask import Flask, Blueprint
from flask import redirect, url_for
from flask import request, session,jsonify
import requests

from api.API_Contenidos.swagger_server.controllers import peliculas_controller, series_controller
from api.API_Usuarios.swagger_server.controllers import usuarios_controller



from api.API_Usuarios import dbconnection_usuarios

app = Flask(__name__)



@app.route('/registro_post/', methods=['POST'])
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
      
    
@app.route('/registro/', methods=['GET'])
def registro():
    return render_template('registro.html')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
