
from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

WHATSAPP = (
    "https://wa.me/5511964532697?"
    "text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio."
    "%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA"
    "%20tem%20dispon%C3%ADveis%3F"
)


@loja_bp.route("/")
def bio():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#542b37">
<title>KB Lashes | Beleza & Sofisticação</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet">

<style>
* {
    box-sizing: border-box;
}

html {
    min-height: 100%;
}

body {
    margin: 0;
    min-height: 100vh;
    min-height: 100dvh;
    font-family: 'DM Sans', Arial, sans-serif;
    color: #fff0eb;
    background: #542b37;
    position: relative;
    isolation: isolate;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -2;
    background-image:
        linear-gradient(
            90deg,
            rgba(48,18,28,.15),
            rgba(65,25,37,.30) 50%,
            rgba(48,18,28,.08)
        ),
        url('/static/fundo-luxo.jpg');
    background-size: cover;
    background-position: center;
}

body::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    background: linear-gradient(
        180deg,
        rgba(30,12,19,.10),
        rgba(30,12,19,.20)
    );
    pointer-events: none;
}

.pagina {
    min-height: 100vh;
    min-height: 100dvh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 35px 18px;
}

.painel {
    width: 100%;
    max-width: 510px;
    padding: 28px 32px 32px;
    text-align: center;
    background: rgba(58,27,37,.43);
    border: 1px solid rgba(255,220,211,.25);
    border-radius: 30px;
    box-shadow: 0 20px 65px rgba(25,8,14,.28);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    animation: aparecer .8s ease both;
}

.logo {
    width: 130px;
    height: 130px;
    object-fit: cover;
    border-radius: 23px;
    padding: 5px;
    background: rgba(255,239,231,.95);
    border: 2px solid #ffe1d6;
    box-shadow: 0 8px 30px rgba(0,0,0,.24);
}

.nome {
    margin: 15px 0 3px;
    display: flex;
    justify-content: center;
    align-items: baseline;
    gap: 10px;
    white-space: nowrap;
}

.nome-kb {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(42px,8vw,60px);
    font-weight: 500;
    color: #ffe5d8;
}

.nome-lashes {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(48px,9vw,70px);
    font-weight: 400;
    color: #ff99b5;
}

.subtitulo {
    font-size: 11px;
    line-height: 1.9;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin: 3px 0 24px;
    color: #ffe1d8;
}

.beneficios {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    margin-bottom: 25px;
}

.beneficio {
    padding: 5px 9px;
    font-size: 11px;
    line-height: 1.5;
    color: #ffe3de;
}

.beneficio + .beneficio {
    border-left: 1px solid rgba(255,218,210,.35);
}

.beneficio span {
    display: block;
    font-size: 23px;
    margin-bottom: 7px;
}

.botoes {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.botao {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    width: 100%;
    min-height: 57px;
    border-radius: 50px;
    padding: 13px 18px;
    text-decoration: none;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: .4px;
    transition: transform .25s, box-shadow .25s;
}

.botao:hover {
    transform: translateY(-3px);
    box-shadow: 0 9px 25px rgba(0,0,0,.25);
}

.agendar {
    color: white;
    background: linear-gradient(90deg,#ff4b98,#f71e81);
    border: 1px solid #ff90ba;
    box-shadow: 0 5px 20px rgba(255,40,125,.35);
}

.servicos {
    color: #783e4b;
    background: linear-gradient(90deg,#ffc1ce,#fa8ca9);
    border: 1px solid #ffd1db;
}

.valores {
    color: #783e4b;
    background: linear-gradient(90deg,#fff0e9,#ffd6dc);
    border: 1px solid #fff0ed;
}

.rodape {
    margin-top: 25px;
    color: #ffd9d4;
}

.ornamento {
    font-size: 20px;
    color: #ffb5c8;
}

.assinatura {
    font-family: 'Great Vibes', cursive;
    font-size: 30px;
    margin-top: 5px;
}

@keyframes aparecer {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media(max-width:600px) {
    body::before {
        background-position: 68% center;
    }

    .pagina {
        padding: 20px 12px;
    }

    .painel {
        padding: 24px 17px;
        border-radius: 24px;
        background: rgba(58,27,37,.68);
    }

    .logo {
        width: 105px;
        height: 105px;
    }

    .subtitulo {
        letter-spacing: 2px;
        font-size: 10px;
    }

    .beneficio {
        padding: 4px;
        font-size: 10px;
    }

    .botao {
        min-height: 53px;
    }

    .assinatura {
        font-size: 27px;
    }
}

@media(prefers-reduced-motion:reduce) {
    .painel {
        animation: none;
    }
    .botao {
        transition: none;
    }
}
</style>
</head>

<body>
<main class="pagina">
<section class="painel">

<img
    class="logo"
    src="/static/logo.png"
    alt="Logo KB Lashes"
>

<h1 class="nome">
    <span class="nome-kb">KB</span>
    <span class="nome-lashes">Lashes</span>
</h1>

<p class="subtitulo">
    Extensão de cílios<br>
    Beleza feminina
</p>

<div class="beneficios">
    <div class="beneficio">
        <span>💎</span>
        Vagas limitadas hoje
    </div>

    <div class="beneficio">
        <span>🗓️</span>
        Realce seu olhar em minutos
    </div>

    <div class="beneficio">
        <span>💗</span>
        Atendimento profissional
    </div>
</div>

<nav class="botoes">

<a
    class="botao agendar"
    href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F"
    target="_blank"
    rel="noopener noreferrer"
>
    🗓️ AGENDAR AGORA
</a>

<a class="botao servicos" href="/servicos">
    ✨ VER SERVIÇOS
</a>

<a class="botao valores" href="/valores">
    💎 VER VALORES
</a>

</nav>

<footer class="rodape">
    <div class="ornamento">♡</div>
    <div class="assinatura">
        Mais que cílios, autoestima 💗
    </div>
</footer>

</section>
</main>
</body>
</html>
"""


# PÁGINA DE VALORES ORIGINAL
@loja_bp.route("/valores")
def valores():
    cards = [
        (
            "Designer de sobrancelhas",
            "✨ Definição perfeita para o seu rosto",
            "R$ 40,00"
        ),
        (
            "Hidra Gloss",
            "💖 Lábios hidratados e com brilho natural",
            "R$ 25,00"
        ),
        (
            "Extensão Brasileiro",
            "🔥 Volume leve e natural",
            "R$ 120,00"
        ),
        (
            "Extensão Fox",
            "👑 Efeito alongado e marcante",
            "R$ 160,00"
        ),
        (
            "Extensão Egípcio",
            "🌸 Olhar sofisticado e elegante",
            "R$ 140,00"
        )
    ]

    conteudo = ""

    for nome, descricao, preco in cards:
        conteudo += f"""
        <div class="card">
            <h3>{nome}</h3>
            <div class="desc">{descricao}</div>
            <div class="preco">{preco}</div>
            <a href="{WHATSAPP}" class="botao">
                Agendar
            </a>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Valores | KB Lashes</title>

<style>
* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #0f0f0f;
    color: white;
}}

.topo {{
    background: linear-gradient(90deg,#ff4da6,#ff1493);
    padding: 30px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}}

.sub {{
    text-align: center;
    margin: 15px;
    color: #ccc;
    font-size: 14px;
}}

.servicos {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    padding: 20px;
}}

.card {{
    background: #1a1a1a;
    padding: 20px;
    border-radius: 15px;
    width: 260px;
    box-shadow: 0 5px 20px rgba(0,0,0,.5);
    text-align: center;
    transition: .3s;
}}

.card:hover {{
    transform: scale(1.05);
}}

.desc {{
    font-size: 13px;
    color: #bbb;
    margin-bottom: 10px;
}}

.preco {{
    color: #ff4da6;
    font-weight: bold;
    font-size: 20px;
    margin: 10px 0;
}}

.botao {{
    display: inline-block;
    margin-top: 10px;
    background: linear-gradient(90deg,#ff4da6,#ff1493);
    color: white;
    padding: 10px 15px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}}

.voltar {{
    display: block;
    text-align: center;
    color: #ff89bd;
    margin: 25px auto;
    text-decoration: none;
}}
</style>
</head>

<body>
<div class="topo">💰 Nossos Valores</div>

<div class="sub">
    ✨ Realce seu olhar com qualidade e profissionalismo 💖
</div>

<div class="servicos">
    {conteudo}
</div>

<a href="/" class="voltar">← Voltar ao início</a>
</body>
</html>
"""
