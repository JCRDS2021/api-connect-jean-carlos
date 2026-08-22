# data/banco.py — Camada de persistência simulada

# Banco de dados simulado em memória
# Cada usuário possui: id, nome e email
usuarios = [
    {"id": 1, "nome": "Ana Lima", "email": "ana.lima@email.com"},
    {"id": 2, "nome": "Bruno Costa", "email": "bruno.costa@email.com"},
    {"id": 3, "nome": "Carla Souza", "email": "carla.souza@email.com"},
]

# Controle de ID incremental
# Garante que cada novo usuário receba um ID único e crescente
proximo_id = 4


def gerar_id():
    """
    Gera um novo ID único e incrementa o contador global.
    Retorna o ID gerado.
    """
    global proximo_id
    id_gerado = proximo_id
    proximo_id += 1
    return id_gerado