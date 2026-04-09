from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

# 🔥 BIO (LINK DA BIO DO INSTAGRAM)
@loja_bp.route("/")
def bio():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>

            body {
                margin:0;
                font-family:Arial;
                background:#fff;
                text-align:center;
            }

            .perfil {
                padding:30px;
            }

            .perfil img {
                width:120px;
                height:120px;
                border-radius:50%;
                object-fit:cover;
            }

            .nome {
                font-size:22px;
                font-weight:bold;
                margin-top:10px;
            }

            .desc {
                color:#777;
                margin-bottom:20px;
            }

            .link {
                display:block;
                margin:10px auto;
                width:80%;
                max-width:300px;
                padding:15px;
                background:#ff4da6;
                color:white;
                text-decoration:none;
                border-radius:10px;
                font-size:16px;
            }

        </style>
    </head>

    <body>

        <div class="perfil">
            <img src="https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg">
            <div class="nome">💖 KB Lashes</div>
            <div class="desc">Extensão de cílios | Beleza feminina ✨</div>
        </div>

        <a class="link" href="https://wa.me/5511964532697?text=Quero agendar">
            📲 Agendar Horário
        </a>

        <a class="link" href="/servicos">
            💅 Ver Serviços
        </a>

    </body>
    </html>
    """


# 🔥 SUA LOJA / SERVIÇOS
@loja_bp.route("/servicos")
def servicos():
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <style>

            body {
                margin:0;
                font-family:Arial;
                background:#fff;
            }

            .topo {
                background:#ff4da6;
                padding:30px;
                text-align:center;
                color:white;
            }

            h2 { text-align:center; }

            .servicos {
                display:flex;
                flex-wrap:wrap;
                justify-content:center;
                gap:20px;
                padding:20px;
            }

            .card {
                background:white;
                padding:20px;
                border-radius:15px;
                width:250px;
                box-shadow:0 5px 15px rgba(0,0,0,0.1);
                text-align:center;
            }

            .preco {
                color:#ff4da6;
                font-weight:bold;
                font-size:18px;
            }

            .botao {
                display:inline-block;
                margin-top:10px;
                background:#ff4da6;
                color:white;
                padding:10px 15px;
                border-radius:10px;
                text-decoration:none;
            }

        </style>
    </head>

    <body>

        <div class="topo">
            <h1>💅 Nossos Serviços</h1>
        </div>

        <div class="servicos">

            <div class="card">
                <h3>Designer de sobrancelhas</h3>
                <p class="preco">R$ 40,00</p>
                <a href="https://wa.me/5511964532697?text=Quero designer" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Hidra Gloss</h3>
                <p class="preco">R$ 25,00</p>
                <a href="https://wa.me/5511964532697?text=Quero Hidra Gloss" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Brasileiro</h3>
                <p class="preco">R$ 120,00</p>
                <a href="https://wa.me/5511964532697?text=Quero Brasileiro" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Fox</h3>
                <p class="preco">R$ 160,00</p>
                <a href="https://wa.me/5511964532697?text=Quero Fox" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Egípcio</h3>
                <p class="preco">R$ 140,00</p>
                <a href="https://wa.me/5511964532697?text=Quero Egípcio" class="botao">Agendar</a>
            </div>

        </div>

    </body>
    </html>
    """
