from peewee import Model, CharField, ForeignKeyField
from app.models.user import User
from app.extensions import db

# Modelo base para todos los modelos de la aplicacion
class BaseModel(Model):
    class Meta:
        database = db.db

# Modelo de Card
class Card(BaseModel):
    user = ForeignKeyField(User, backref='cards', on_delete='CASCADE') 
    title = CharField()
    description = CharField()
    urlimage = CharField(null=True)