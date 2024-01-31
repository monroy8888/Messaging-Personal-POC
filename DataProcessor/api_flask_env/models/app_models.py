from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from app.config.db import db
from apiflask.fields import File
from sqlalchemy.orm import relationship

Base = db.Model


class Usuario(Base):
    __tablename__ = 'Usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    telefono = Column(String(15))
    email = Column(String(100))
    ciudad = Column(String(50))

    def __init__(self, nombre, apellido, telefono, email, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.ciudad = ciudad

    def to_json(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'email': self.email,
            'ciudad': self.ciudad,
        }


class Eventos(Base):
    __tablename__ = 'Eventos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_evento = Column(String(100))
    fecha_creacion = Column(Date)
    lugar = Column(String(100))

    def __init__(self, nombre_evento, fecha_creacion, lugar):
        self.nombre_evento = nombre_evento
        self.fecha_creacion = fecha_creacion
        self.lugar = lugar

    def to_json(self):
        return {
            'nombre_evento': self.nombre_evento,
            'fecha_creacion': self.fecha_creacion,
            'lugar': self.lugar,
        }


class Tarifas(Base):
    __tablename__ = 'Tarifas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    evento_id = Column(Integer, ForeignKey('Eventos.id'))
    tarifa = Column(Float(10, 2))

    def __init__(self, usuario_id, evento_id, tarifa):
        self.usuario_id = usuario_id
        self.evento_id = evento_id
        self.tarifa = tarifa

    def to_json(self):
        return {
            'usuario_id': self.usuario_id,
            'evento_id': self.evento_id,
            'tarifa': self.tarifa
        }


class Registro(Base):
    __tablename__ = 'Registro'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(String(100))
    resumen = Column(String(100))
    files = File()
    urls = Column(String(100))
    eventos_id = Column(Integer, ForeignKey('Eventos.id'))
    eventos_relacion = relationship('Eventos', backref='registros')

    def __init__(self, nombre, descripcion, resumen, files, urls, eventos_id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.resumen = resumen
        self.files = files
        self.urls = urls
        self.eventos_id = eventos_id

    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'resumen': self.resumen,
            'files': self.files,
            'urls': self.urls,
            'eventos_id': self.eventos_id,
        }

################
