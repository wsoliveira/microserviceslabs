from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine


db = SQLAlchemy()
#db = MongoEngine()

def configure(app):  
    db.init_app(app)
    app.db = db

class Recurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    processo_id = db.Column(db.Integer)
    tipo_recurso = db.Column(db.String(255))
    peso = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.id}"    