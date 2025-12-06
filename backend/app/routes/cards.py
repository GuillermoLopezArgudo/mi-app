from flask import Blueprint, request, jsonify
from app.models.cards import Card
from app.models.user import User
from werkzeug.utils import secure_filename
import jwt
import os

SECRET_KEY = "tu_clave_secreta_aqui"
UPLOAD_FOLDER = 'app/static/images/'
cards_bp = Blueprint("cards", __name__)

# Asegurarse de que la carpeta de imágenes exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Crear una nueva card
@cards_bp.post("/cards")
def create_card():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Token no proporcionado"}), 401

    try:
        token = auth_header.split()[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = User.get_by_id(payload["user_id"])
    except User.DoesNotExist:
        return jsonify({"error": "Usuario no encontrado"}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401

    # Obtener datos desde FormData
    title = request.form.get("title")
    description = request.form.get("description")
    file = request.files.get("image")

    if not title or not description:
        return jsonify({"error": "Faltan datos"}), 400

    urlimage = None
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        urlimage = f"/static/images/{filename}"

    try:
        card = Card.create(
            title=title,
            description=description,
            urlimage=urlimage,
            user=user
        )
        return jsonify({
            "ok": True,
            "message": "Card creada",
            "card": {
                "id": card.id,
                "title": card.title,
                "description": card.description,
                "urlimage": card.urlimage
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener todas las cards del usuario autenticado
@cards_bp.get("/cards")
def get_cards():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Token no proporcionado"}), 401

    try:
        token = auth_header.split()[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = User.get_by_id(payload["user_id"])
    except User.DoesNotExist:
        return jsonify({"error": "Usuario no encontrado"}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401

    cards = Card.select().where(Card.user == user)
    cards_list = [
        {"id":c.id,"title": c.title, "description": c.description, "urlimage": c.urlimage}
        for c in cards
    ]
    return jsonify({"cards": cards_list}), 200

# Eliminar una card por su ID
@cards_bp.delete("/cards/<int:card_id>")
def delete_card(card_id):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Token no proporcionado"}), 401

    try:
        token = auth_header.split()[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = User.get_by_id(payload["user_id"])
    except User.DoesNotExist:
        return jsonify({"error": "Usuario no encontrado"}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Token inválido"}), 401

    try:
        card = Card.get_by_id(card_id)
        if card.user.id != user.id:
            return jsonify({"error": "No autorizado para eliminar esta card"}), 403
        card.delete_instance()
        return jsonify({"ok": True, "message": "Card eliminada"}), 200
    except Card.DoesNotExist:
        return jsonify({"error": "Card no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
