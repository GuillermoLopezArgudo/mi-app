from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.cards import Card
import logging
import time

logging.basicConfig(level=logging.INFO)

app = create_app()

with app.app_context():
    # Intentar conectar a la base de datos con reintentos
    for _ in range(10):
        try:
            db.db.init(
                app.config["DB_NAME"],
                user=app.config["DB_USER"],
                password=app.config["DB_PASSWORD"],
                host=app.config["DB_HOST"]
            )
            db.db.connect()
            break
        except Exception:
            time.sleep(2)
    else:
        logging.error("No se pudo conectar a MySQL después de varios intentos.")
        exit(1)

    # Asignar la base de datos a los modelos
    User._meta.database = db.db
    Card._meta.database = db.db

    try:
        db.db.create_tables([User])
        db.db.create_tables([Card])
        logging.info("Tablas creadas correctamente.")
    except Exception as e:
        logging.error(f"Error al crear tablas: {e}")
    finally:
        if not db.db.is_closed():
            db.db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
