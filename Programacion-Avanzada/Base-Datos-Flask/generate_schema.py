# generate_schema.py (actualizado)
from models import db, Departamento, Usuario
from config import Config
from sqlalchemy.schema import CreateTable
from sqlalchemy import MetaData

def generate_schema_sql(filename='schema.sql'):
    from sqlalchemy import create_engine
    from sqlalchemy import Table
    from sqlalchemy.sql import text

    # Crear una instancia de Flask para acceder a la configuración
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        metadata = db.metadata
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        with open(filename, 'w') as f:
            for table in metadata.sorted_tables:
                f.write(str(CreateTable(table).compile(engine)) + ';\n\n')
            
            # Insertar datos iniciales en departamentos
            f.write("-- Insertar datos iniciales en departamentos\n")
            f.write("INSERT INTO departamentos (id, nombre) VALUES\n")
            departamentos = Departamento.query.all()
            valores = ",\n".join([f"({d.id}, '{d.nombre}')" for d in departamentos])
            f.write(valores + ";\n")

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        # Insertar datos iniciales si la tabla está vacía
        if Departamento.query.count() == 0:
            departamentos = [
                Departamento(id=1, nombre='Ventas'),
                Departamento(id=2, nombre='Finanzas'),
                Departamento(id=3, nombre='Recursos humanos')
            ]
            db.session.add_all(departamentos)
            db.session.commit()
    generate_schema_sql()
    print("Archivo 'schema.sql' generado exitosamente con datos iniciales.")
