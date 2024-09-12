class Config:
    SECRET_KEY = "PNE"
    DEBUG      = True

class DevelopmentConfig(Config):
    MYSQL_HOST      ="localhost"
    MYSQL_USER      ="root"
    MYSQL_PASSWORD  =""

config = {
    "development" : DevelopmentConfig 
}   