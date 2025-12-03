from flask import Blueprint, request, jsonify
from app.models.usuario import Usuario
import logging

auth_bp = Blueprint("auth", __name__)

# Registro de usuario
@auth_bp.post("/register")
def register_user():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    # Validar datos de entrada
    if not email or not password:
        return jsonify({"error": "Faltan datos. Proporciona email y contraseña."}), 400

    # Verificar si el usuario ya existe
    if Usuario.select().where(Usuario.email == email).exists():
        return jsonify({"error": "El usuario ya existe."}), 400

    try:
        usuario = Usuario.create(email=email, password=password)
        return jsonify({
            "ok": True,
            "message": "Usuario registrado exitosamente",
            "usuario": {"email": usuario.email},
        }), 201
    except Exception as e:
        logging.error(f"Error al registrar usuario: {e}")
        return jsonify({"error": "Error al registrar usuario"}), 500

# Inicio de sesión
@auth_bp.post("/login")
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    
    # Validar datos de entrada
    if Usuario.select().where((Usuario.email == email) & (Usuario.password == password)).exists():
        return jsonify({"ok": True, "message": "Login successful", "token": "demo-token"}), 200

    return jsonify({"ok": False, "message": "Credenciales inválidas"}), 401
