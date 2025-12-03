from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

# Ruta de ejemplo para verificar que el backend funciona
@main_bp.get("/")
def home():
    return jsonify({"mensaje": "Hola desde Flask + Peewee + MySQL!"})
