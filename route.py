from flask import Blueprint, request, jsonify
from models import db, Cliente 
from schemas import ClienteSchema
from marshmallow import ValidationError

route = Blueprint("route", __name__)
cliente_schema = ClienteSchema()

@route.route("/clientes", methods=["GET"])

def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes]), 200

@route.route("/clientes", methods=["POST"])

def inserir_clientes():
    try:
        data = request.json
        dataValidate = cliente_schema.load(data)
        novo = Cliente(nome=dataValidate["nome"], email=dataValidate["email"], telefone=dataValidate["telefone"] )
        db.session.add(novo)
        db.session.commit()
        return jsonify({"mensagem": "Cliente criado!", "cliente": novo.to_dict()}), 201
    except ValidationError as err:
        return jsonify({"error" : err.messages}), 400

@route.route("/clientes/<int:cliente_id>", methods=["GET"])

def buscar_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    return jsonify(cliente.to_dict())

@route.route("/clientes/<int:cliente_id>", methods=["PUT"])

def atualizar_cliente(cliente_id):
    try:
        cliente = Cliente.query.get_or_404(cliente_id)
        data = request.json
        dataValidate = cliente_schema.load(data)
        cliente.nome = dataValidate.get("nome", cliente.nome)
        cliente.email = dataValidate.get("email", cliente.email)
        cliente.telefone = dataValidate.get("telefone", cliente.telefone)
        db.session.commit()
        return jsonify({"mensagem": "Cliente atualizado!", "cliente": cliente.to_dict()}), 200
    except ValidationError as err:
        return jsonify({"error" : err.messages}), 400

@route.route("/clientes/<int:cliente_id>", methods=["DELETE"])

def deletar_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"mensagem": "Cliente deletado!"})