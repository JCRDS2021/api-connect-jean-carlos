# app.py — Ponto de entrada da aplicação

from flask import Flask, jsonify
from routes.usuarios import usuarios_bp

# Instancia a aplicação Flask
app = Flask(__name__)

# Configuração JSON
app.config["JSON_SORT_KEYS"] = False

# Registra o blueprint de usuários
app.register_blueprint(usuarios_bp)

# Rota de verificação de status do servidor
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "mensagem": "API de Gerenciamento de Usuários",
        "status":   "online",
        "versao":   "1.0.0"
    }), 200

# Inicializa o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)