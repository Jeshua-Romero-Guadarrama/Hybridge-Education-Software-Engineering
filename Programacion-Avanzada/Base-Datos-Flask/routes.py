# routes.py
from app import app, db
from models import Usuario, Departamento
from flask import render_template, redirect, url_for, request

@app.route('/')
def home():
    # Redirigir a la página de usuarios
    return redirect(url_for('usuarios'))

@app.route('/add_user/<nombre>/<email>/<id_departamento>')
def add_user(nombre, email, id_departamento):
    departamento = Departamento.query.get(id_departamento)
    if not departamento:
        return f'Departamento con ID {id_departamento} no existe.', 404
    usuario = Usuario(nombre=nombre, email=email, id_departamento=id_departamento)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuarios'))

@app.route('/add_user_form', methods=['POST'])
def add_user_form():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    id_departamento = request.form.get('departamento')
    
    if not nombre or not email or not id_departamento:
        return "Todos los campos son obligatorios.", 400
    
    departamento = Departamento.query.get(id_departamento)
    if not departamento:
        return f'Departamento con ID {id_departamento} no existe.', 404
    
    if Usuario.query.filter_by(email=email).first():
        return "El email ya está registrado.", 400
    
    usuario = Usuario(nombre=nombre, email=email, id_departamento=id_departamento)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuarios'))

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    departamentos = Departamento.query.all()
    return render_template('usuarios.html', usuarios=usuarios, departamentos=departamentos)