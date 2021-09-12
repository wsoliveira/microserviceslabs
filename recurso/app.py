#https://livecodestream.dev/post/python-flask-api-starter-kit-and-project-layout/
#https://github.com/dunossauro/crudzin
#from re import DEBUG
from flask import Flask
from flask_migrate import Migrate
import os

from model.model import configure as config_db
from schema.schema import configure as config_ma
from tasks.tasks import configure as configure_celery


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db_recurso.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config['MONGODB_SETTINGS'] = {
    #    'db': 'apprecurso_labs',
    #    'host': os.environ.get("MONGO_HOST","127.0.0.1"),
    #    'port': 27017,
    #    'username':'root',
    #    'password':'123mudar'        
    #}      
    config_db(app)
    config_ma(app)
    configure_celery(app)
    Migrate(app, app.db)

    from api.v1.endpoints.recurso import bp_recurso
    app.register_blueprint(bp_recurso)

    return app


#TODO: Alterar para MongoDB
#TODO: Criar Celery
#TODO: Criar funcao para ler rabbit e inserir no banco (como daemon)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8020)