import os
from apiflask import Schema
from apiflask.fields import Integer, String, Date, Float
from apiflask.validators import Length, OneOf

from apiflask.fields import File


# from marshmallow import Schema, fields, validate


class Usuario(Schema):
    id = Integer()
    nombre = String(required=True, validate=Length(0, 20))
    apellido = String(required=True, validate=Length(0, 20))
    telefono = String(required=False, validate=Length(0, 20))
    email = String(required=False, validate=Length(0, 20))
    ciudad = String(required=False, validate=Length(0, 20))


class Eventos(Schema):
    nombre_evento = String()
    fecha_creacion = Date()
    lugar = String()


class Tarifas(Schema):
    usuario_id = Integer()
    evento_id = Integer()
    tarifa = Float()


class RegistroIn(Schema):
    nombre = String(required=True, validate=[Length(min=1, max=200)])
    descripcion = String(required=True, validate=[Length(min=1, max=320)])
    resumen = String(required=True, validate=[Length(min=1, max=320)])
    files = File()
    urls = String()

    @staticmethod
    def files_validator(value):
        allowed_extensions = {'.doc', '.docx', '.ppt', '.pptx', '.pdf', '.epub', '.html', '.xls', '.xlsx', '.csv'}
        file_extension = os.path.splitext(value.filename)[1].lower()

        if file_extension not in allowed_extensions:
            raise ValueError("Invalid file type.")
