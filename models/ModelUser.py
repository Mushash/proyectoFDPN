from models.entities.User import User

class ModelUser:
    @classmethod
    def signin(self, db, usuario):
        try:
            selUsuario = db.connection.cursor()
            selUsuario.execute("SELECT * FROM usuario WHERE correo=%s",(usuario.correo,))
            u=selUsuario.fetchone()
            if u is not None:
                return User(u[0],u[1],u[2],u[3],u[4],u[5])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            selUsuario = db.connection.cursor()
            selUsuario.execute("SELECT * FROM usuario WHERE  id=%s",(id))
            u=selUsuario.fetchone()
            if u is not None:
                return User(u[0],u[1],u[2],u[3],u[4],u[5])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        