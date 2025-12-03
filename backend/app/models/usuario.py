from peewee import Model, CharField
from app.extensions import db

# Modelo base para todos los modelos de la aplicacion
class BaseModel(Model):
    class Meta:
        database = db.db

# Modelo de usuario
class Usuario(BaseModel):
    email = CharField(unique=True)
    password = CharField()
