from flask import Blueprint, jsonify, current_app, request, abort, make_response
from model.model import Recurso
from schema.schema import RecursoSchema
from tasks.tasks import ola_mundo

bp_recurso = Blueprint('recurso', __name__)

@bp_recurso.route('/novo_recurso', methods=['GET'])
def novo_recurso():
    ola_mundo.delay()
    return make_response('{"detail":"Em Processamento !"}',202)

@bp_recurso.route('/recursos', methods=['GET'])
def get_recursos():
    get_recurso = Recurso.query.all()
    recurso_schema = RecursoSchema(many=True)
    result = recurso_schema.dump(get_recurso)    
    return make_response(jsonify(result), 200)    

@bp_recurso.route('/recursos/<id>', methods=['GET'])
def get_recurso(id):
    if get_recurso := Recurso.query.get(id):
        recurso_schema = RecursoSchema()
        result = recurso_schema.dump(get_recurso)
        return make_response(jsonify(result), 200)
    return make_response('{"detail":"Recurso nao encontrado"}',404)

@bp_recurso.route('/recursos', methods=['POST'])
def post_recurso():
    recurso_schema = RecursoSchema()
    recurso = recurso_schema.load(request.get_json())
    current_app.db.session.add(recurso)
    current_app.db.session.commit()
    return make_response(recurso_schema.jsonify(recurso), 201)

@bp_recurso.route('/recursos/<id>', methods=['DELETE'])
def delete_recurso(id):
    if get_recurso := Recurso.query.get(id):
        current_app.db.session.add(get_recurso)
        current_app.db.session.commit()        
        make_response("", 204)
    return make_response('{"detail":"Recurso nao encontrado"}',404)

@bp_recurso.route('/recursos/<id>', methods=['PUT'])
def put_recurso(id):    
    if tb_recurso := Recurso.query.get(id):
        recurso_schema = RecursoSchema()
        tb_recurso.peso =  request.json.get('peso', tb_recurso.peso)
        tb_recurso.tipo_recurso =  request.json.get('tipo_recurso',tb_recurso.tipo_recurso)
        current_app.db.session.add(tb_recurso)
        current_app.db.session.commit()
        return make_response(recurso_schema.jsonify(tb_recurso), 204) 
    return make_response('{"detail":"Recurso nao encontrado"}',404)
