from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

@loja_bp.route("/")
def home():
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

            /* 🔥 TOPO */
            .topo {
                background:linear-gradient(90deg,#ff4da6,#ff85c1);
                padding:60px 20px;
                text-align:center;
                color:white;
                box-shadow:0 5px 20px rgba(0,0,0,0.2);
            }

            h1 { margin:0; font-size:32px; }
            h2 { text-align:center; margin-top:40px; }

            /* 🔥 GALERIA */
            .galeria {
                overflow:hidden;
                height:400px;
                margin-top:20px;
            }

            .slider {
                display:flex;
                flex-direction:column;
                animation: subir 25s linear infinite;
            }

            .slider img {
                width:280px;
                margin:10px auto;
                border-radius:15px;
                transition:0.3s;
                box-shadow:0 5px 15px rgba(0,0,0,0.2);
            }

            .slider img:hover {
                transform:scale(1.05);
            }

            @keyframes subir {
                0% { transform: translateY(0); }
                100% { transform: translateY(-100%); }
            }

            /* 🔥 SERVIÇOS */
            .servicos {
                display:flex;
                flex-wrap:wrap;
                justify-content:center;
                gap:25px;
                padding:30px;
            }

            .card {
                background:white;
                padding:25px;
                border-radius:15px;
                width:260px;
                box-shadow:0 10px 25px rgba(0,0,0,0.1);
                transition:0.3s;
                text-align:center;
            }

            .card:hover {
                transform:translateY(-5px);
            }

            .preco {
                color:#ff4da6;
                font-size:20px;
                font-weight:bold;
            }

            /* 🔥 BOTÃO AGENDAR */
            .botao {
                display:inline-block;
                margin-top:15px;
                background:#ff4da6;
                color:white;
                padding:12px 20px;
                border-radius:10px;
                text-decoration:none;
                font-size:16px;
            }

            .botao:hover {
                background:#ff3385;
            }

            /* 🔥 WHATS FIXO */
            .whats {
                position:fixed;
                bottom:20px;
                right:20px;
                background:#25D366;
                color:white;
                padding:15px 20px;
                border-radius:50px;
                text-decoration:none;
                font-size:18px;
                box-shadow:0 5px 15px rgba(0,0,0,0.3);
            }

            .whats:hover {
                transform:scale(1.1);
            }

            /* 🔥 DEPOIMENTOS */
            .depoimentos {
                text-align:center;
                padding:40px 20px;
                background:#fff0f5;
            }

            .depoimentos p {
                max-width:400px;
                margin:10px auto;
                font-style:italic;
            }

        </style>
    </head>

    <body>

        <div class="topo">
            <h1>💖 Karen Brito Studio Beauty</h1>
            <p>Realçando sua beleza com cílios perfeitos ✨</p>
        </div>

        <h2>✨ Resultados</h2>

        <div class="galeria">
            <div class="slider">
                <img src="https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg">
                <img src="https://i.postimg.cc/ZY9yHF0V/3b395467_be8b_418d_bb64_be5d02e7009b.jpg">
                <img src="https://i.postimg.cc/fTNTdxdZ/31c710da_433e_4dff_8b83_92d9cdf145aa.jpg">
                <img src="https://i.postimg.cc/kXmXSxS2/89a6469c_6e25_4ad6_a252_04bc4ccb1d4e.jpg">
                <img src="https://i.postimg.cc/rwyVnMgJ/592a55cd_50cc_42cc_9d08_5a8875456ebd.jpg">
                <img src="https://i.postimg.cc/P56t09Rv/a2782b16_2f43_49d2_8765_df3085e24149.jpg">
            </div>
        </div>

        <h2>💅 Nossos Serviços</h2>

        <div class="servicos">

            <div class="card">
                <h3>Designer de sobrancelhas</h3>
                <p class="preco">R$ 40,00</p>
                <a href="https://wa.me/5511964532697?text=Quero designer de sobrancelhas" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Hidra Gloss</h3>
                <p class="preco">R$ 25,00</p>
                <a href="https://wa.me/5511964532697?text=Quero Hidra Gloss" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Brasileiro</h3>
                <p class="preco">R$ 120,00</p>
                <small>Manutenção: R$ 50,00</small><br>
                <a href="https://wa.me/5511964532697?text=Quero Extensão Brasileiro" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Fox</h3>
                <p class="preco">R$ 160,00</p>
                <small>Manutenção: R$ 90,00</small><br>
                <a href="https://wa.me/5511964532697?text=Quero Extensão Fox" class="botao">Agendar</a>
            </div>

            <div class="card">
                <h3>Extensão Egípcio</h3>
                <p class="preco">R$ 140,00</p>
                <small>Manutenção: R$ 60,00</small><br>
                <a href="https://wa.me/5511964532697?text=Quero Extensão Egípcio" class="botao">Agendar</a>
            </div>

        </div>

        <!-- 🔥 DEPOIMENTOS -->
        <div class="depoimentos">
            <h2>⭐ O que nossas clientes dizem</h2>
            <p>⭐⭐⭐⭐⭐ "Perfeito! Atendimento maravilhoso 😍"</p>
            <p>⭐⭐⭐⭐⭐ "Amei meus cílios, ficou lindo!"</p>
            <p>⭐⭐⭐⭐⭐ "Super profissional, recomendo muito 💖"</p>
        </div>

        <!-- 🔥 WHATS -->
        <a href="https://wa.me/5511964532697?text=Olá quero agendar um horário" class="whats">
            💬
        </a>

    </body>
    </html>
    """
