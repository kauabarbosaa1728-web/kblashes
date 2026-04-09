from flask import Flask
from loja import loja_bp

app = Flask(__name__)
app.secret_key = "segredo123"

app.register_blueprint(loja_bp)

# 🔥 ROTA PRA MANTER O SITE ATIVO
@app.route("/ping")
def ping():
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
