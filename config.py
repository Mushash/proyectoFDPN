class Config:
    SECRET_KEY = "PNE"
    DEBUG      = True

class DevelopmentConfig(Config):
    MYSQL_HOST      ='localhost'
    MYSQL_USER      ='root'
    MYSQL_PASSWORD  ='mysql'
    MYSQL_DB        ='fdpn'

config = {
    'development' : DevelopmentConfig 
}   