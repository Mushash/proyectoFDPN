from flask import Flask, render_template,url_for,request,redirect,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
from datetime import datetime
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

fdpnApp = Flask(__name__)
db      =MySQL(fdpnApp)
#pythonanywhere
fdpnApp.config.from_object(config['development'])
adminSession = LoginManager(fdpnApp)

@adminSession.user_loader
def agregarUsuario(id):
    return ModelUser.get_by_id(db, id)

@fdpnApp.route('/')
def home():
    return render_template('home.html')

@fdpnApp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg = datetime.datetime()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s,%s,%s,%s)",(nombre, correo, claveCifrada, fechareg))
        db.connection.commit()
        return render_template('home.html')
    return render_template('signup.html')

@fdpnApp.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == "POST":
        usuario            = User(0, None, request.form['correo'], request.form['clave'], None, None)
        usuarioAutenticado = ModelUser.signin(db, usuario)
        if usuarioAutenticado is not None:
            if usuarioAutenticado.clave:
                login_user(usuarioAutenticado)
                if usuarioAutenticado.perfil == 'A':
                    return render_template('admin.html')
                else:
                    return render_template('user.html')
            else:
                flash('Contraseña incorrecta')
                return redirect(request.url)
        else:
            flash('Usuario inexistente')
            return redirect (request.url)
    return render_template('signin.html')

@fdpnApp.route('/signout', methods = ['GET', 'POST'])
def signout():
    logout_user()
    return render_template('home.html')

@fdpnApp.route('/sUsuario', methods = ['GET', 'POST'])
def sUsuario():
    selUsuario = db.connection.cursor()
    selUsuario.execute("SELECT * FROM usuario")
    U = selUsuario.fetchall()
    selUsuario.close()
    return render_template('usuarios.html', usuarios = U)

@fdpnApp.route('/iUsuario', methods = ['GET', 'POST'])
def iUsuario():
    nombre          = request.form['nombre']
    correo          = request.form['correo']
    clave           = request.form['clave']
    claveCifrada    = generate_password_hash(clave)
    fechareg        = datetime.now()
    perfil          = request.form['perfil']
    agregarUsuario = db.connection.cursor()
    agregarUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg, perfil) VALUES(%s, %s, %s, %s, %s)", (nombre, correo, claveCifrada, fechareg, perfil))
    db.connection.commit()
    agregarUsuario.close()
    flash('Usuario agregado')
    return redirect (url_for('sUsuario'))

@fdpnApp.route('/uUsuario/<int:id>', methods = ['GET', 'POST'])
def uUsuario(id):
    nombre          = request.form['nombre']
    correo          = request.form['correo']
    clave           = request.form['clave']
    claveCifrada    = generate_password_hash(clave)
    fechareg        = datetime.now()
    perfil          = request.form['perfil']
    actUsuario = db.connection.cursor()
    actUsuario.execute("UPDATE usuario SET nombre=%s, correo=%s, clave=%s, fechareg=%s, perfil=%s WHERE id=%s", (nombre, correo, claveCifrada, fechareg, perfil))
    db.connection.commit()
    actUsuario.close()
    flash('Usuario actualizado')
    return redirect(url_for('sUsuario'))

'''if __name__=="_main_":
    fdpnApp.config.from_object('development')
    fdpnApp.run(debug=True,port=3300)'''