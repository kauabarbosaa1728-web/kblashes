from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

@loja_bp.route("/")
def home():
    return """
    <html>
    <head>
        <style>
            body {
                margin:0;
                font-family:Arial;
                background:#ffe4ec;
            }

            .topo {
                background:#ff69b4;
                padding:40px;
                text-align:center;
                color:white;
            }

            .galeria {
                overflow:hidden;
                width:100%;
                margin-top:20px;
            }

            .slider {
                display:flex;
                flex-direction:column;
                animation: subir 20s linear infinite;
            }

            .slider img {
                width:300px;
                margin:10px auto;
                border-radius:12px;
            }

            @keyframes subir {
                0% { transform: translateY(0); }
                100% { transform: translateY(-100%); }
            }

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
                border-radius:12px;
                width:250px;
                box-shadow:0 2px 10px rgba(0,0,0,0.1);
            }

            .botao {
                background:#25D366;
                color:white;
                padding:15px 30px;
                border-radius:10px;
                text-decoration:none;
                font-size:18px;
            }
        </style>
    </head>

    <body>

        <div class="topo">
            <h1>Karen Brito Studio Beauty</h1>
            <p>Realçando sua beleza com cílios perfeitos 💖</p>
        </div>

        <h2 style="text-align:center;margin-top:20px;">Resultados</h2>

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

        <h2 style="text-align:center;">Nossos Serviços</h2>

        <div class="servicos">

            <div class="card">
                <h3>Designer de sobrancelhas</h3>
                <p>R$ 40,00</p>
            </div>

            <div class="card">
                <h3>Hidra Gloss</h3>
                <p>R$ 25,00</p>
            </div>

            <div class="card">
                <h3>Extensão Brasileiro</h3>
                <p>R$ 120,00</p>
                <small>Manutenção: R$ 50,00</small>
            </div>

            <div class="card">
                <h3>Extensão Fox</h3>
                <p>R$ 160,00</p>
                <small>Manutenção: R$ 90,00</small>
            </div>

            <div class="card">
                <h3>Extensão Egípcio</h3>
                <p>R$ 140,00</p>
                <small>Manutenção: R$ 60,00</small>
            </div>

        </div>

        <div style="text-align:center;padding:40px;">
            <a href="https://wa.me/5511964532697?text=Olá quero agendar um horário" class="botao">
                💬 Agendar pelo WhatsApp
            </a>
        </div>

    </body>
    </html>
    """
