from flask_marshmallow import Marshmallow
from marshmallow import fields
from model.model import Recurso

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class RecursoSchema(ma.SQLAlchemyAutoSchema):
#class RecursoSchema(ma.Schema):
    class Meta:
        model = Recurso
        load_instance = True
