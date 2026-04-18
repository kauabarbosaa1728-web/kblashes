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
                text-align:center;
                color:white;

                background-size:cover;
                background-position:center;
                animation: fundo 12s infinite;
            }

            @keyframes fundo {
                0% { background-image: url('https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg'); }
                33% { background-image: url('https://i.postimg.cc/ZY9yHF0V/3b395467_be8b_418d_bb64_be5d02e7009b.jpg'); }
                66% { background-image: url('https://i.postimg.cc/fTNTdxdZ/31c710da_433e_4dff_8b83_92d9cdf145aa.jpg'); }
            }

            body::before {
                content:"";
                position:fixed;
                width:100%;
                height:100%;
                background:linear-gradient(180deg, rgba(255,20,147,0.5), rgba(255,105,180,0.5));
                top:0;
                left:0;
                z-index:-1;
            }

            .perfil {
                padding:40px 20px;
            }

            .perfil img {
                width:120px;
                height:120px;
                border-radius:50%;
                border:3px solid white;
            }

            .nome {
                font-size:24px;
                font-weight:bold;
                margin-top:10px;
            }

            .desc {
                margin-bottom:10px;
            }

            .frase {
                font-size:14px;
                font-weight:bold;
                margin:5px;
            }

            .link {
                display:block;
                margin:12px auto;
                width:85%;
                max-width:320px;
                padding:16px;
                background:linear-gradient(90deg,#ff4da6,#ff1493);
                color:white;
                text-decoration:none;
                border-radius:12px;
                font-size:16px;
                box-shadow:0 5px 20px rgba(0,0,0,0.4);
                transition:0.2s;
            }

            .link:hover {
                transform:scale(1.05);
            }

            .link:first-of-type {
                animation: pulse 1.5s infinite;
            }

            @keyframes pulse {
                0% { transform:scale(1); }
                50% { transform:scale(1.07); }
                100% { transform:scale(1); }
            }

        </style>
    </head>

    <body>

        <div class="perfil">
            <img src="https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg">
            <div class="nome">💖 KB Lashes</div>
            <div class="desc">Extensão de cílios | Beleza feminina ✨</div>

            <div class="frase">🔥 Vagas limitadas hoje</div>
            <div class="frase">💖 Realce seu olhar em minutos</div>
            <div class="frase">✨ Atendimento profissional</div>
        </div>

        <a class="link" href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F">
            📲 AGENDAR AGORA
        </a>

        <a class="link" href="/servicos">
            💅 VER SERVIÇOS
        </a>

        <a class="link" href="/valores">
            💰 VER VALORES
        </a>

    </body>
    </html>
    """


# 🔥 VALORES
@loja_bp.route("/valores")
def valores():
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>

            body {
                margin:0;
                font-family:Arial;
                background:#0f0f0f;
                color:white;
            }

            .topo {
                background:linear-gradient(90deg,#ff4da6,#ff1493);
                padding:30px;
                text-align:center;
                font-size:24px;
                font-weight:bold;
            }

            .sub {
                text-align:center;
                margin:10px;
                color:#ccc;
                font-size:14px;
            }

            .servicos {
                display:flex;
                flex-wrap:wrap;
                justify-content:center;
                gap:20px;
                padding:20px;
            }

            .card {
                background:#1a1a1a;
                padding:20px;
                border-radius:15px;
                width:260px;
                box-shadow:0 5px 20px rgba(0,0,0,0.5);
                text-align:center;
                transition:0.3s;
            }

            .card:hover {
                transform:scale(1.05);
            }

            .desc {
                font-size:13px;
                color:#bbb;
                margin-bottom:10px;
            }

            .preco {
                color:#ff4da6;
                font-weight:bold;
                font-size:20px;
                margin:10px 0;
            }

            .botao {
                display:inline-block;
                margin-top:10px;
                background:linear-gradient(90deg,#ff4da6,#ff1493);
                color:white;
                padding:10px 15px;
                border-radius:10px;
                text-decoration:none;
                font-weight:bold;
            }

        </style>
    </head>

    <body>

        <div class="topo">
            💰 Nossos Valores
        </div>

        <div class="sub">
            ✨ Realce seu olhar com qualidade e profissionalismo 💖
        </div>

        <div class="servicos">

            <div class="card">
                <h3>Designer de sobrancelhas</h3>
                <div class="desc">✨ Definição perfeita para o seu rosto</div>
                <div class="preco">R$ 40,00</div>
                <a href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Hidra Gloss</h3>
                <div class="desc">💖 Lábios hidratados e com brilho natural</div>
                <div class="preco">R$ 25,00</div>
                <a href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Brasileiro</h3>
                <div class="desc">🔥 Volume leve e natural</div>
                <div class="preco">R$ 120,00</div>
                <a href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Fox</h3>
                <div class="desc">👑 Efeito alongado e marcante</div>
                <div class="preco">R$ 160,00</div>
                <a href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Egípcio</h3>
                <div class="desc">🌸 Olhar sofisticado e elegante</div>
                <div class="preco">R$ 140,00</div>
                <a href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F" class="botao">Agendar</a>
            </div>

        </div>

    </body>
    </html>
    """
