# controllers/usuario_controller.py — Lógica de negócio

from flask import jsonify, request
from data.banco import usuarios, gerar_id

def listar_usuarios():
    """
    GET /usuarios
    Retorna todos os usuários cadastrados.
    Status: 200 OK
    """
    return jsonify(usuarios), 200

def cadastrar_usuario():
    """
    POST /usuarios
    Cadastra um novo usuário recebido no corpo da requisição.
    Status: 201 Created
    Status: 400 Bad Request (dados inválidos)
    """
    dados = request.get_json()

    # Validação — verifica se os campos obrigatórios foram enviados
    if not dados:
        return jsonify({"erro": "Corpo da requisição ausente ou inválido."}), 400

    if "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Os campos 'nome' e 'email' são obrigatórios."}), 400

    if not dados["nome"].strip() or not dados["email"].strip():
        return jsonify({"erro": "Os campos 'nome' e 'email' não podem estar vazios."}), 400

    # Monta o novo usuário com ID gerado automaticamente
    novo_usuario = {
        "id":    gerar_id(),
        "nome":  dados["nome"].strip(),
        "email": dados["email"].strip()
    }

    # Adiciona ao banco simulado
    usuarios.append(novo_usuario)

    return jsonify(novo_usuario), 201

def buscar_usuario_por_id(id):
    """
    GET /usuarios/<id>
    Busca e retorna um único usuário pelo ID informado na URL.
    Status: 200 OK         (usuário encontrado)
    Status: 404 Not Found  (usuário não existe)
    """

    # Percorre o array procurando um usuário com o ID informado
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario_encontrado = usuario
            break  # encerra o loop assim que encontrar

    # Se não encontrou nenhum usuário com esse ID
    if usuario_encontrado is None:
        return jsonify({
            "erro": f"Usuário com ID {id} não encontrado."
        }), 404

    # Usuário encontrado — retorna os dados com status 200
    return jsonify(usuario_encontrado), 200

def atualizar_usuario(id):
    """
    PUT /usuarios/<id>
    Atualiza os dados de um usuário existente pelo ID informado na URL.
    Status: 200 OK         (atualizado com sucesso)
    Status: 400 Bad Request (dados inválidos ou ausentes)
    Status: 404 Not Found  (usuário não existe)
    """
    dados = request.get_json()

    # Validação — verifica se o corpo da requisição foi enviado
    if not dados:
        return jsonify({
            "erro": "Corpo da requisição ausente ou inválido."
        }), 400

    # Validação — exige ao menos um campo válido para atualizar
    if "nome" not in dados and "email" not in dados:
        return jsonify({
            "erro": "Informe ao menos um campo para atualizar: 'nome' ou 'email'."
        }), 400

    # Busca o índice do usuário no array pelo ID
    indice_encontrado = None

    for indice, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            indice_encontrado = indice
            break

    # ID não encontrado no array
    if indice_encontrado is None:
        return jsonify({
            "erro": f"Usuário com ID {id} não encontrado."
        }), 404

    # Atualiza apenas os campos enviados (preserva os não enviados)
    if "nome" in dados and dados["nome"].strip():
        usuarios[indice_encontrado]["nome"] = dados["nome"].strip()

    if "email" in dados and dados["email"].strip():
        usuarios[indice_encontrado]["email"] = dados["email"].strip()

    # Retorna o usuário atualizado
    return jsonify(usuarios[indice_encontrado]), 200


def remover_usuario(id):
    """
    DELETE /usuarios/<id>
    Remove um usuário existente pelo ID informado na URL.
    Status: 200 OK        (removido com sucesso)
    Status: 404 Not Found (usuário não existe)
    """

    # Busca o índice do usuário no array pelo ID
    indice_encontrado = None

    for indice, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            indice_encontrado = indice
            break

    # ID não encontrado no array
    if indice_encontrado is None:
        return jsonify({
            "erro": f"Usuário com ID {id} não encontrado."
        }), 404

    # Remove o usuário do array pelo índice
    usuario_removido = usuarios.pop(indice_encontrado)

    # Retorna confirmação com os dados do usuário removido
    return jsonify({
        "mensagem": f"Usuário '{usuario_removido['nome']}' removido com sucesso.",
        "usuario":  usuario_removido
    }), 200