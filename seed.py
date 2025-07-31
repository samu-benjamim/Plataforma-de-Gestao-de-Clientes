from app import db, app
from models import Cliente

with app.app_context():
    clientes = [
        Cliente(nome="XXXXXX", email="XXXXXX", telefone=""),
    ]
    db.session.add_all(clientes)
    db.session.commit()
    print("Clientes inseridos com sucesso!")


with app.app_context():
    for cliente in Cliente.query.all():
        print(cliente.nome, cliente.email, cliente.telefone)