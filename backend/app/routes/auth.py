from flask import Blueprint, request, jsonify
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import logging
import jwt

SECRET_KEY = "tu_clave_secreta_aqui"

auth_bp = Blueprint("auth", __name__)

# Registro de usuario
@auth_bp.post("/register")
def register_user():
    data = request.get_json() or {}
    email = data.get("email")
    password_plain =  data.get("password")

    # Validar datos de entrada
    if not email or not password_plain:
        return jsonify({"error": "Faltan datos. Proporciona email y contraseña."}), 400

    # Verificar si el usuario ya existe
    if User.select().where(User.email == email).exists():
        return jsonify({"error": "El usuario ya existe."}), 400

    try:
        # Cifrar la contraseña
        password_hashed = generate_password_hash(password_plain, method='pbkdf2:sha256', salt_length=8)
        
        # Crear el usuario en la base de datos
        user = User.create(email=email, password=password_hashed)
        
        # Generar token JWT
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "ok": True,
            "message": "Usuario registrado exitosamente",
            "usuario": {"email": user.email},
            "token": token
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
    
 # Buscar usuario por email
    try:
        user = User.get(User.email == email)
    except User.DoesNotExist:
        return jsonify({"ok": False, "message": "Credenciales inválidas"}), 401

    # Verificar contraseña
    if check_password_hash(user.password, password):
        
        # Generar token JWT
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        
        return jsonify({"ok": True, "message": "Login successful", "token": token}), 200
    else:
        return jsonify({"ok": False, "message": "Credenciales inválidas"}), 401
