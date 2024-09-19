from flask import Flask, render_template,url_for 
from werkzeug.security import generate_password_hash
import datetime
from config import config

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
        fechare = datetime.datetime()
        regUsuario = db.conection.cursor()
    return render_template('signup.html')

@fdpnApp.router('/signin')
def signin():
    return render_template('signin.html')

if __name__=="_main_":
    fdpnApp.run(debug=True,port=3300)