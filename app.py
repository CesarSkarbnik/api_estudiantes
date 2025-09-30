import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cesar:X7P9euvwF38qM6VHdJDnUclGRyDpfSvv@dpg-d2vp9dali9vc7389018g-a.oregon-postgres.render.com/db_tec_8zu4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo de la base de datos
class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

#endpoint para insertar estudiante
@app.route('/estudiantes', methods=['POST'])
def insert_estudiante():
    data = request.get_json()
    nuevo_estudiante = Estudiante(
        no_control=data['no_control'],
        nombre=data['nombre'],
        ap_paterno=data['ap_paterno'],
        ap_materno=data['ap_materno'],
        semestre=data['semestre'],
    )
    db.session.add(nuevo_estudiante)
    db.session.commit()
    return jsonify({'msg': 'Estudiante agregado correctamente'})    

