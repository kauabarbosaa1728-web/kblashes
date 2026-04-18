from flask import Blueprint
from layout import container

valores_bp = Blueprint("valores_bp", __name__)

@valores_bp.route("/valores")
def valores():
    return container("""

    <h2 style="text-align:center;">💰 Nossos Valores</h2>

    <div class="card">
        <h3>✨ Cílios Fio a Fio</h3>
        <p>R$ 80,00</p>
    </div>

    <div class="card">
        <h3>🔥 Volume Brasileiro</h3>
        <p>R$ 100,00</p>
    </div>

    <div class="card">
        <h3>💖 Volume Russo</h3>
        <p>R$ 120,00</p>
    </div>

    <a href="https://wa.me/55SEUNUMERO" class="botao">
        💬 AGENDAR PELO WHATSAPP
    </a>

    <style>
    .card {
        background: #1a1a1a;
        margin: 15px;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }

    .card h3 {
        color: #ff2d7a;
    }

    .botao {
        display: block;
        margin: 20px auto;
        background: #ff2d7a;
        color: white;
        padding: 12px;
        text-align: center;
        border-radius: 10px;
        text-decoration: none;
        width: 80%;
        font-weight: bold;
    }
    </style>

    """)
