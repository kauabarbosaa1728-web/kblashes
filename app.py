from flask import Flask
from loja import loja_bp
from servicos import servicos_bp  # 🔥 NOVA IMPORTAÇÃO

app = Flask(__name__)
app.secret_key = "segredo123"

# 🔥 BLUEPRINTS
app.register_blueprint(loja_bp)
app.register_blueprint(servicos_bp)  # 🔥 REGISTRO DA NOVA PÁGINA

# 🔥 ROTA PRA MANTER O SITE ATIVO
@app.route("/ping")
def ping():
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
