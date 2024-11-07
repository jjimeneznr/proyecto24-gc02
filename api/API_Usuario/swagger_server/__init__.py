from flask import Blueprint

usuarios_blueprint = Blueprint('Usuario', __name__)

@usuarios_blueprint.route('/some_endpoint', methods=['GET'])
def example_endpoint():
    return {"message": "Este es un ejemplo de endpoint de Usuarios"}
