import datetime
import sqlite3

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

#definimos la table de la base de datos
class User(db.Model):
    __tablename__ = 'users'
        
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = self.__create_pasword(password)
        
    #hash contrasena
    def __create_pasword(self, password):
        return generate_password_hash(password)

    #recibe contrasena y lo compara con la hasheada devuelve true si es igual, false si no
    def verify_password(self, password):
        return check_password_hash(self.password, password)

#creamos la base de datos 
def CreateDatabase():
    conexion = sqlite3.connect('pitsaluma.db')
    #cursor permite ejecutar la consulta
    cursor = conexion.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users (' +
    'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
    'email varchar(100) NOT NULL UNIQUE, ' +
    'password textvarchar(100) NOT NULL)')
    
    #guardamos cambios
    conexion.commit()
    conexion.close()
