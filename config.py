class Config:
    SECRET_KEY = "PNE"
    DEBUG      = True

class DevelopmentConfig(Config):
    #localhost
    MYSQL_HOST      ='localhost'
    MYSQL_USER      ='root'
    MYSQL_PASSWORD  ='mysql'
    MYSQL_DB        ='fdpn' 

    #pythonanywhere
    '''MYSQL_HOST      ='fdpn.mysql.pythonanywhere-services.com'
    MYSQL_USER      ='fdpn'
    MYSQL_PASSWORD  ='contras1'
    MYSQL_DB        ='fdpn' '''

class MailConfig(Config):
    MAIL_SERVER     =   'smtp.gmail.com'
    MAIL_PORT       =   587
    MAIL_USE_TLS    =   True
    MAIL_USE_SSL    =   False
    MAIL_USERNAME   =   'fernando.prieto2229@alumnos.udg'
    MAIL_PASSWORD   =   'skzv acvs hmec wdzp'
    MAIL_ASCII_ATTACHMENTS  =   True


config = {
    'development' : DevelopmentConfig,
    'mail'        : MailConfig 
}   