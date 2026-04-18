from flask import Flask
from loja import loja_bp
from servicos import servicos_bp
from valores import valores_bp  # 🔥 NOVA IMPORTAÇÃO

app = Flask(__name__)
app.secret_key = "segredo123"

# 🔥 BLUEPRINTS
app.register_blueprint(loja_bp)
app.register_blueprint(servicos_bp)
app.register_blueprint(valores_bp)  # 🔥 REGISTRO DA PÁGINA DE VALORES

# 🔥 ROTA PRA MANTER O SITE ATIVO
@app.route("/ping")
def ping():
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
