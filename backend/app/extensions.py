from peewee import MySQLDatabase
import os

# Peewee database extension
class PeeweeDB:
    def __init__(self):
        self.db = None
        
    # Inicializar la base de datos con la aplicación Flask
    def init_app(self, app):
        self.db = MySQLDatabase(
            app.config["DB_NAME"],
            user=app.config["DB_USER"],
            password=app.config["DB_PASSWORD"],
            host=app.config["DB_HOST"]
        )

        @app.before_request
        def _connect_db():
            if self.db.is_closed():
                self.db.connect()

        @app.teardown_request
        def _close_db(exc):
            if not self.db.is_closed():
                self.db.close()

db = PeeweeDB()
