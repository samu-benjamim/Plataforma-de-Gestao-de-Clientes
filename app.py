from flask import Flask, request, jsonify
from models import db, Cliente 


# inicialização do flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# rotas

@app.route("/clientes", methods=["GET"])

def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes]), 200

@app.route("/clientes", methods=["POST"])

def inserir_clientes():
    data = request.json
    novo = Cliente(nome=data["nome"], email=data["email"], telefone=data["telefone"] )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Cliente criado!", "cliente": novo.to_dict()}), 201

@app.route("/clientes/<int:cliente_id>", methods=["GET"])

def buscar_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    return jsonify(cliente.to_dict())

@app.route("/clientes/<int:cliente_id>", methods=["PUT"])

def atualizar_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    data = request.json
    cliente.nome = data.get("nome", cliente.nome)
    cliente.email = data.get("email", cliente.email)
    cliente.telefone = data.get("telefone", cliente.telefone)
    db.session.commit()
    return jsonify({"mensagem": "Cliente atualizado!", "cliente": cliente.to_dict()})

@app.route("/clientes/<int:cliente_id>", methods=["DELETE"])

def deletar_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"mensagem": "Cliente deletado!"})

if __name__ == "__main__":
    app.run(debug=True)