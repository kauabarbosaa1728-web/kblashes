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
            <div class="card" onclick="abrirImagem('/static/{arquivo}')">
                <img src="/static/{arquivo}">
                <div class="texto">{frase}</div>
            </div>
            """
            i += 1

    return container(f"""

    <h2 style="text-align:center;">✨ Nossos Trabalhos</h2>
    <p style="text-align:center;">Veja alguns resultados reais 💖</p>

    <div class="feed">
        {imagens_html}
    </div>

    <a href="https://wa.me/5511964532697" class="botao">
        💬 AGENDAR AGORA
    </a>

    <!-- 🔥 MODAL (imagem grande) -->
    <div id="modal" onclick="fecharImagem()">
        <img id="imgModal">
    </div>

    <style>

    body {{
        background:#000;
    }}

    .feed {{
        display:flex;
        flex-direction:column;
        gap:15px;
        padding:15px;
    }}

    .card {{
        position:relative;
        width:100%;
        cursor:pointer;
    }}

    /* 🔥 TAMANHO MENOR (AJUSTADO) */
    .card img {{
        width:100%;
        height:300px;
        object-fit:cover;
        border-radius:15px;
    }}

    .texto {{
        position:absolute;
        bottom:10px;
        left:10px;
        right:10px;
        color:white;
        font-size:16px;
        font-weight:bold;
        background:rgba(0,0,0,0.5);
        padding:8px;
        border-radius:8px;
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

    /* 🔥 MODAL */
    #modal {{
        display:none;
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:100%;
        background:rgba(0,0,0,0.9);
        justify-content:center;
        align-items:center;
        z-index:999;
    }}

    #modal img {{
        max-width:90%;
        max-height:90%;
        border-radius:15px;
    }}

    </style>

    <script>
    function abrirImagem(src) {{
        document.getElementById("modal").style.display = "flex";
        document.getElementById("imgModal").src = src;
    }}

    function fecharImagem() {{
        document.getElementById("modal").style.display = "none";
    }}
    </script>

    """)
