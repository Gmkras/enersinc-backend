from flask import Blueprint, request, jsonify, redirect, url_for

from ..controller import personas_controller
from ..models.models import Persona


api_scope = Blueprint("api", __name__)


@api_scope.route('/personas', methods=['GET'])
def get_list():
    personas_list = personas_controller.lists()

    personas_dict = [persona._asdict() for persona in personas_list]

    return jsonify(personas_dict)

@api_scope.route('/personas/<id_>', methods=['GET'])
def get_details(id_):
    persona = Persona(id=id_)

    persona_new = personas_controller.details(persona)

    return jsonify(persona_new._asdict())

@api_scope.route('/personas', methods=['POST'])
def create():
    data = request.form
    persona = Persona(nombres=data["firstName"], apellidos=data["lastName"],
                      tipo_documento=data["tipo_documento"], documento=data["documento"], email=data["email"], hobbie=data["hobbie"])

    personas_controller.create(persona)

    return redirect(url_for('views.home'))

@api_scope.route('/personas/<id_>', methods=['PUT'])
def update(id_):
    data = request.data

    persona = Persona(id=id_, nombres=data["firstName"], apellidos=data["lastName"],
                      tipo_documento=data["tipo_documento"], documento=data["documento"], email=data["email"], hobbie=data["hobbie"])

    persona_new = personas_controller.update(persona)

    return jsonify(persona_new._asdict())

@api_scope.route('/personas/<id_>', methods=['DELETE'])
def delete(id_):
    persona = Persona(id=id_)

    persona_new = personas_controller.delete(persona)

    return jsonify(persona_new._asdict())