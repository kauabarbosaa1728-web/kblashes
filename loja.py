from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

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
                animation: fundo 15s infinite;
            }

            /* 🔥 FUNDO COM SUAS FOTOS */
            @keyframes fundo {
                0% { background-image: url('https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg'); }
                33% { background-image: url('https://i.postimg.cc/ZY9yHF0V/3b395467_be8b_418d_bb64_be5d02e7009b.jpg'); }
                66% { background-image: url('https://i.postimg.cc/fTNTdxdZ/31c710da_433e_4dff_8b83_92d9cdf145aa.jpg'); }
                100% { background-image: url('https://i.postimg.cc/kXmXSxS2/89a6469c_6e25_4ad6_a252_04bc4ccb1d4e.jpg'); }
            }

            /* 🔥 ESCURECER PRA DESTACAR */
            body::before {
                content:"";
                position:fixed;
                width:100%;
                height:100%;
                background:rgba(255, 20, 147, 0.4);
                top:0;
                left:0;
                z-index:-1;
            }

            /* 🔥 PERFIL */
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
                margin-bottom:20px;
                font-size:14px;
            }

            /* 🔥 BOTÕES */
            .link {
                display:block;
                margin:12px auto;
                width:85%;
                max-width:320px;
                padding:15px;
                background:linear-gradient(90deg,#ff4da6,#ff1493);
                color:white;
                text-decoration:none;
                border-radius:12px;
                font-size:16px;
                box-shadow:0 5px 20px rgba(0,0,0,0.3);
            }

            .link:hover {
                transform:scale(1.05);
            }

            /* 🔥 FRASE TOP */
            .frase {
                margin-top:10px;
                font-size:13px;
                opacity:0.9;
            }

        </style>
    </head>

    <body>

        <div class="perfil">
            <img src="https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg">
            <div class="nome">💖 KB Lashes</div>
            <div class="desc">Extensão de cílios | Beleza feminina ✨</div>

            <div class="frase">🔥 Transforme seu olhar hoje mesmo</div>
            <div class="frase">💎 Atendimento profissional</div>
        </div>

        <a class="link" href="https://wa.me/5511964532697?text=Quero agendar agora">
            📲 AGENDAR AGORA
        </a>

        <a class="link" href="https://wa.me/5511964532697?text=Quero ver valores">
            💰 VER VALORES
        </a>

        <a class="link" href="https://wa.me/5511964532697?text=Quero fazer meus cílios">
            💖 QUERO FICAR LINDA
        </a>

    </body>
    </html>
    """
