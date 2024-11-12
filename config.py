class Config:
    SECRET_KEY = "PNE"
    DEBUG      = True

class DevelopmentConfig(Config):
    #localhost
    '''MYSQL_HOST      ='localhost'
    MYSQL_USER      ='root'
    MYSQL_PASSWORD  ='mysql'
    MYSQL_DB        ='fdpn' '''

    #pythonanywhere
    MYSQL_HOST      ='fdpn.mysql.pythonanywhere-services.com'
    MYSQL_USER      ='fdpn'
    MYSQL_PASSWORD  ='contras1'
    MYSQL_DB        ='fdpn'


config = {
    'development' : DevelopmentConfig 
}   