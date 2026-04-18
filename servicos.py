from flask import Blueprint
from layout import container

servicos_bp = Blueprint("servicos_bp", __name__)

@servicos_bp.route("/servicos")
def servicos():
    return container("""

    <h2 style="text-align:center;">✨ Nossos Trabalhos</h2>

    <div class="galeria">

        <img src="/static/cilios1.jpg">
        <img src="/static/cilios2.jpg">
        <img src="/static/cilios3.jpg">
        <img src="/static/cilios4.jpg">

    </div>

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
    }

    .galeria img:hover {
        transform: scale(1.05);
    }
    </style>

    """)
