DEBUG = True

USERNAME = 'postgres'
PASSWORD = '1234'
SERVER = '127.0.0.1:5432'
DB = 'flask_api'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=USERNAME,pw=PASSWORD,url=SERVER,db=DB)
#'postgresql+psycopg2://postgres:1234@localhost:5432/flask_api'

#Identificar as modeificações nos models
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'aplicacao-projetos'

