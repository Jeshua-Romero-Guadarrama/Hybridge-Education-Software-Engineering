# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Departamento(db.Model):
    __tablename__ = 'departamentos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    usuarios = db.relationship('Usuario', backref='departamento', lazy=True)

    def __repr__(self):
        return f'<Departamento {self.nombre}>'

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'
