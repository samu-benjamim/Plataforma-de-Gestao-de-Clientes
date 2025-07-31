from marshmallow import Schema, fields, validate, ValidationError

class ClienteSchema(Schema):
    nome = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    telefone = fields.Str(required=True, validate=validate.Length(min=10))


