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
      
@app.route('/perfil')
def perfil():
    if 'id' not in session:
        return redirect(url_for('login'))  # Redirige al login si no hay sesión activa

    # Extrae los datos desde la sesión
    user_data = {
        "nombre_completo": session['nombre_completo'],
        "email": session['email'],
        "genero_favorito": session['genero_favorito']
    }
    return render_template('user-profile.html', user_data=user_data)

@app.route('/edit_perfil', methods=['GET', 'POST'])
def edit_perfil():
    if request.method == 'GET':
        id_usuario = session['id']
        nombre_completo = session['nombre_completo']
        email = session['email']
        password = session['password']
        genero_favorito = session['genero_favorito']
        return render_template('edit-profile.html', id_usuario=id_usuario,
                               nombre_completo=nombre_completo,
                               email=email,
                               genero_favorito=genero_favorito)
        
    if request.method == 'POST':
        # Aquí procesas los datos del formulario solo si se hizo clic en "Guardar"
        new_name= request.form['nombre_completo']
        new_email= request.form['email']
        new_password= request.form['password1']
        new_password2= request.form['password2']
        new_genero= request.form['genero_favorito']
        
        if new_password != new_password2:
            error_message = "Las contraseñas no coinciden. Por favor, intente de nuevo."
            return render_template('edit_profile.html', 
                                   nombre_completo=session['nombre_completo'], 
                                   email=session['email'] ,
                                   genero_favorito=session['genero_favorito'],
                                   error_message=error_message)
            
        if 'guardar' in request.form:
            try:
                if new_name != session['nombre_completo']:
                    # Llamar al controlador para actualizar el nombre
                    bodyname = {
                        "nombre_completo": new_name
                    }
                    usuarios_controller.usuarios_id_put(bodyname, session['id'])
                    
                    session['nombre_completo'] = new_name  # Actualizamos la sesión con el nuevo nombre

                if new_email != session['email']:
                    # Llamar al controlador para actualizar el email
                    bodycorreo = {
                        "correo": new_email
                    }
                    usuarios_controller.usuarios_id_correo_put(bodycorreo, id)
                    session['email'] = new_email  # Actualizamos la sesión con el nuevo email

                if new_password != '' and new_password != session['password']:
                    # Si la contraseña cambia, llamamos al controlador para actualizarla
                    bodypassword = {
                        "contrasea": new_password
                    }
                    usuarios_controller.usuarios_id_contrasea_put(bodypassword, id)
                    session['password'] = new_password  # Actualizamos la sesión con la nueva contraseña

                if new_genero != session['genero_favorito']:
                    # Llamar al controlador para actualizar el género favorito
                    bodygenero = {
                        "genero_favorito": new_genero
                    }
                    usuarios_controller.usuarios_id_genero_favorito_put(bodygenero,id)
                    session['genero_favorito'] = new_genero  # Actualizamos la sesión con el nuevo género

                # Redirigir a la página de perfil con los datos actualizados
                return redirect(url_for('perfil'))
        
            except Exception as e:
            # Si ocurre un error, podemos mostrar un mensaje de error
                error_message = f"Hubo un error al actualizar los datos: {str(e)}"
                return render_template('edit-profile.html', 
                                    nombre_completo=session['nombre_completo'], 
                                    email=session['email'],
                                    genero_favorito=session['genero_favorito'],
                                    error_message=error_message)
        
        # Redirige al perfil después de guardar o cancelar
        return redirect(url_for('perfil'))
    
@app.route('/registro', methods=['GET'])
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
