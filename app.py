from flask import Flask, jsonify
from models import db 
from route import route
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(route)

with app.app_context():
    db.create_all()

@app.errorhandler(404)

def not_found(error):
    return jsonify({"erro": "Cliente nao encontrado"}), 404

@app.errorhandler(500)

def server_error(error):
    return jsonify({"erro": "Erro interno no servidor"}), 500

if __name__ == "__main__":
    app.run(debug=True)

