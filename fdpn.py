from flask import Flask, render_template,url_for,request,redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
from datetime import datetime
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

fdpnApp = Flask(__name__)

@fdpnApp.router('/')
def home():
    return render_template('home.html')

@fdpnApp.router('/signup')
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg = datetime.datetime()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s,%s,%s,%s)",(nombre, correo, claveCifrada, fechareg))
    return render_template('signup.html')

@fdpnApp.router('/signin')
def signin():
    return render_template('signin.html')

if __name__=="_main_":
    fdpnApp.config.from_object('development')
    fdpnApp.run(debug=True,port=3300)