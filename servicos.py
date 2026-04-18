from flask import Blueprint
from layout import container

servicos_bp = Blueprint("servicos_bp", __name__)

@servicos_bp.route("/servicos")
def servicos():
    return container("""

    <h2 style="text-align:center;">✨ Nossos Trabalhos</h2>
    <p style="text-align:center;">Veja alguns resultados reais 💖</p>

    <div class="galeria">

        <img src="/static/cilios1.png">
        <img src="/static/cilios2.png">
        <img src="/static/cilios3.png">
        <img src="/static/cilios4.png">

    </div>

    <a href="https://wa.me/55SEUNUMERO" class="botao">
        💬 AGENDAR PELO WHATSAPP
    </a>

    <style>
    .galeria {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        padding: 20px;
    }

    .galeria img {
        width: 100%;
        border-radius: 15px;
        transition: 0.3s;
        cursor: pointer;
    }

    .galeria img:hover {
        transform: scale(1.05);
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
