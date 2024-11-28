from flask import Flask, render_template,url_for,request,redirect,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash
from datetime import datetime
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

fdpnApp = Flask(__name__)

#pythonanywhere
fdpnApp.config.from_object(config['development'])
fdpnApp.config.from_object(config['mail'])
db           =  MySQL(fdpnApp)
mail         =  Mail(fdpnApp)
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
        fechareg = datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s,%s,%s,%s)",(nombre, correo, claveCifrada, fechareg))
        db.connection.commit()
        msg = Message(subject='Gracias por venderle tu alma a Panda shop',recipients=[correo])
        msg.html =  render_template('mail.html',nombre=nombre)
        mail.send(msg)
        return render_template('home.html')
    return render_template('signup.html')

@fdpnApp.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == "POST":
        usuario =User(None,None,request.form['correo'],request.form['clave'],None,None)
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
    u          = selUsuario.fetchall()
    selUsuario.close()
    return render_template('usuarios.html', usuarios = u)

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
    flash('Usuario Agregado')
    return redirect(url_for('sUsuario'))

@fdpnApp.route('/uUsuario/<int:id>', methods = ['GET', 'POST'])
def uUsuario(id):
    nombre          = request.form['nombre']
    correo          = request.form['correo']
    clave           = request.form['clave']
    claveCifrada    = generate_password_hash(clave)
    fechareg        = datetime.now()
    perfil          = request.form['perfil']
    actUsuario = db.connection.cursor()
    actUsuario.execute("UPDATE usuario SET nombre=%s, correo=%s, clave=%s, fechareg=%s, perfil=%s WHERE id=%s", (nombre, correo, claveCifrada, fechareg, perfil, id))
    db.connection.commit()
    actUsuario.close()
    flash('Usuario Actualizado')
    return redirect(url_for('sUsuario'))

@fdpnApp.route('/dUsuario/<int:id>', methods = ['GET', 'POST'])
def dUsuario(id):
    delUsuario = db.connection.cursor()
    delUsuario.execute("DELETE FROM usuario WHERE id=%s", (id,))
    db.connection.commit()
    delUsuario.close
    flash("Usuario eliminado")
    return redirect(url_for('sUsuario'))

#Productos
@fdpnApp.route('/sProducto', methods = ['GET','POST'])
def sProducto():
    selProducto = db.connection.cursor()
    selProducto.execute("SELECT * FROM producto")
    p           = selProducto.fetchall()
    selProducto.close()
    return render_template('productos.html', producto = p)

@fdpnApp.route('/iProducto',  methods = ['GET','POST'])
def iProducto():
    nombrep     = request.form ['nombrep']
    ocupacion       = request.form ['ocupacion']
    descripcion = request.form ['descripcion']
    precio      = request.form ['precio']
    regProducto = db.connection.cursor()
    regProducto.execute("INSERT INTO producto (nombrep, ocupacion, descripcion, precio) VALUES (%s, %s, %s, %s)", (nombrep, ocupacion, descripcion, precio))
    db.connection.commit()
    regProducto.close()
    flash("Producto Agregado")
    return redirect(url_for('sProducto'))

@fdpnApp.route('/uProducto/<int:idp>' , methods =  ['GET', 'POST'])
def uProducto(idp):
    nombrep     = request.form ['nombrep']
    ocupacion       = request.form ['ocupacion']
    descripcion = request.form ['descripcion']
    precio      = request.form ['precio']
    actProducto = db.connection.cursor()
    actProducto.execute("UPDATE producto SET nombrep=%s, ocupacion=%s, descripcion=%s, precio=%s WHERE idp=%s", (nombrep, ocupacion, descripcion, precio, idp))
    db.connection.commit()
    actProducto.close()
    flash ("Producto actualizado con exito")
    return redirect(url_for('sProducto'))

@fdpnApp.route('/dProducto/<int:idp>' , methods =  ['GET', 'POST'])
def dProducto(idp):
    delProducto = db.connection.cursor()
    delProducto.execute("DELETE FROM producto WHERE idp = %s", (idp,))
    db.connection.commit()
    delProducto.close()
    flash ("Producto Eliminado")
    return redirect(url_for('sProducto'))

if __name__ == "__main__":
    fdpnApp.run(debug=True,port=3300)