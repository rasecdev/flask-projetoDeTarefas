from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flasgger import Swagger

#A ORDEM IMPORTA
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
JWTManager(app)

api = Api(app)
swagger = Swagger(app)

from .views import tarefa_view, projeto_view, funcionario_view, usuario_view, login_view
from .models import tarefa_model, projeto_model, funcionario_model, usuario_model