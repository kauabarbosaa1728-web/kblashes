from flask import Blueprint
from layout import container
import os

servicos_bp = Blueprint("servicos_bp", __name__)

@servicos_bp.route("/servicos")
def servicos():

    imagens_html = ""

    pasta = "static"
    frases = [
        "✨ Olha esse resultado incrível",
        "💖 Venha realçar seu olhar",
        "🔥 Resultado perfeito",
        "😍 Cliente apaixonada",
        "💅 Cílios naturais e lindos",
        "⚡ Atendimento rápido",
        "🌸 Olhar transformado",
        "👑 Você merece isso"
    ]

    i = 0

    for arquivo in os.listdir(pasta):
        if arquivo.endswith((".png", ".jpg", ".jpeg")):
            frase = frases[i % len(frases)]
            imagens_html += f"""
            <div class="card">
                <img src="/static/{arquivo}">
                <div class="texto">{frase}</div>
            </div>
            """
            i += 1

    return container(f"""

    <h2 style="text-align:center;">✨ Nossos Trabalhos</h2>

    <div class="feed">
        {imagens_html}
    </div>

    <a href="https://wa.me/5511964532697" class="botao">
        💬 AGENDAR AGORA
    </a>

    <style>

    body {{
        background:#000;
    }}

    .feed {{
        display:flex;
        flex-direction:column;
        gap:20px;
        padding:20px;
    }}

    .card {{
        position:relative;
        width:100%;
    }}

    .card img {{
        width:100%;
        border-radius:20px;
    }}

    .texto {{
        position:absolute;
        bottom:10px;
        left:10px;
        right:10px;
        color:white;
        font-size:18px;
        font-weight:bold;
        background:rgba(0,0,0,0.5);
        padding:10px;
        border-radius:10px;
    }}

    .botao {{
        display:block;
        margin:20px auto;
        background:#ff2d7a;
        color:white;
        padding:15px;
        text-align:center;
        border-radius:12px;
        text-decoration:none;
        width:90%;
        font-size:18px;
        font-weight:bold;
    }}

    </style>

    """)
