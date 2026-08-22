# routes/usuarios.py — Definição das rotas de usuários

from flask import Blueprint
from controllers.usuario_controller import (
    listar_usuarios,
    cadastrar_usuario,
    buscar_usuario_por_id,
    atualizar_usuario,        # ← adicionado
    remover_usuario           # ← adicionado
)

# Blueprint — agrupa todas as rotas de usuários
usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")

# GET /usuarios/ — lista todos os usuários
usuarios_bp.route("/", methods=["GET"])(listar_usuarios)

# POST /usuarios/ — cadastra um novo usuário
usuarios_bp.route("/", methods=["POST"])(cadastrar_usuario)

# GET /usuarios/<id> — busca um usuário pelo ID
usuarios_bp.route("/<int:id>", methods=["GET"])(buscar_usuario_por_id)

# PUT /usuarios/<id> — atualiza um usuário pelo ID
usuarios_bp.route("/<int:id>", methods=["PUT"])(atualizar_usuario)

# DELETE /usuarios/<id> — remove um usuário pelo ID
usuarios_bp.route("/<int:id>", methods=["DELETE"])(remover_usuario)