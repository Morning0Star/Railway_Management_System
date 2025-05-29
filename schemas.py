from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class TrainSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    source = fields.Str(required=True)
    destination = fields.Str(required=True)
    totalSeats = fields.Int(required=True, validate=validate.Range(min=1))

class BookingSchema(Schema):
    trainId = fields.Str(required=True) 