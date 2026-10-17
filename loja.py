
from flask import Blueprint
from html import escape

loja_bp = Blueprint("loja", __name__)

WHATSAPP = (
    "https://wa.me/5511964532697?"
    "text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio."
    "%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA"
    "%20tem%20dispon%C3%ADveis%3F"
)


@loja_bp.route("/")
def bio():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#552c3a">
<meta name="description" content="KB Lashes: extensão de cílios e beleza feminina. Agende seu horário.">
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
    color: #ffe9e2;
    background: #552c3a;
    isolation: isolate;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -2;
    background:
        linear-gradient(
            90deg,
            rgba(50,17,28,.12),
            rgba(48,16,28,.22),
            rgba(50,17,28,.10)
        ),
        url('/static/fundo-luxo.jpg') center/cover no-repeat;
}

body::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    pointer-events: none;
    background: linear-gradient(
        180deg,
        rgba(38,12,21,.08),
        rgba(38,12,21,.19)
    );
}

.pagina {
    min-height: 100vh;
    min-height: 100dvh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 34px 16px;
}

.painel {
    position: relative;
    isolation: isolate;
    width: 100%;
    max-width: 570px;
    padding: 35px 39px 33px;
    text-align: center;
    border-radius: 37px;
    border: 1px solid rgba(255,204,190,.85);
    background: linear-gradient(
        150deg,
        rgba(114,48,59,.55),
        rgba(54,17,30,.76) 57%,
        rgba(109,43,58,.57)
    );
    box-shadow:
        0 25px 85px rgba(40,9,21,.42),
        0 0 25px rgba(255,150,161,.18),
        inset 0 0 27px rgba(255,193,176,.08);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    animation: entrada .8s ease both;
    overflow: hidden;
}

.painel::before {
    content: "";
    position: absolute;
    inset: 4px;
    border: 1px solid rgba(255,211,193,.25);
    border-radius: 32px;
    pointer-events: none;
}

.painel::after {
    content: "";
    position: absolute;
    width: 200px;
    height: 200px;
    top: -105px;
    right: -70px;
    background: radial-gradient(
        circle,
        rgba(255,188,179,.25),
        transparent 70%
    );
    pointer-events: none;
}

.logo {
    position: relative;
    width: 145px;
    height: 145px;
    object-fit: cover;
    border-radius: 28px;
    padding: 6px;
    background: #ffe9e3;
    border: 2px solid #fff0e7;
    box-shadow:
        0 0 0 5px rgba(255,189,178,.15),
        0 0 30px rgba(255,177,172,.45),
        0 12px 35px rgba(30,9,18,.3);
}

.nome {
    margin: 20px 0 3px;
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 12px;
    white-space: nowrap;
}

.nome-kb {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(53px,8vw,77px);
    font-weight: 500;
    line-height: 1.2;
    color: #ffe6d6;
    text-shadow: 0 3px 14px rgba(255,181,158,.32);
}

.nome-lashes {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(59px,9vw,84px);
    font-weight: 400;
    line-height: 1.2;
    color: #ff99b9;
    text-shadow: 0 0 17px rgba(255,115,161,.35);
}

.subtitulo {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin: 8px 0 28px;
    font-size: 12px;
    letter-spacing: 4px;
    line-height: 1.9;
    text-transform: uppercase;
    color: #ffe2d9;
}

.subtitulo::before,
.subtitulo::after {
    content: "";
    width: 40px;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #ffc8b7
    );
}

.subtitulo::after {
    transform: rotate(180deg);
}

.beneficios {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 0;
    margin: 0 0 31px;
}

.beneficio {
    padding: 6px 10px;
    font-size: 12px;
    line-height: 1.5;
    color: #ffe5df;
}

.beneficio + .beneficio {
    border-left: 1px solid rgba(255,210,197,.43);
}

.icone-beneficio {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 51px;
    height: 51px;
    margin: 0 auto 10px;
    border-radius: 50%;
    font-size: 26px;
    background: linear-gradient(
        145deg,
        rgba(255,174,188,.23),
        rgba(255,213,194,.07)
    );
    border: 1px solid rgba(255,198,182,.75);
    box-shadow:
        0 0 14px rgba(255,147,161,.24),
        inset 0 0 12px rgba(255,202,194,.1);
}

.botoes {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.botao {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    min-height: 79px;
    padding: 12px 19px;
    border-radius: 50px;
    text-decoration: none;
    border: 2px solid rgba(255,236,225,.85);
    transition:
        transform .25s ease,
        box-shadow .25s ease;
}

.botao:hover {
    transform: translateY(-4px) scale(1.015);
}

.botao:focus-visible {
    outline: 3px solid white;
    outline-offset: 4px;
}

.botao-icone {
    width: 47px;
    height: 47px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    flex-shrink: 0;
}

.botao-texto {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    gap: 4px;
    text-align: center;
}

.botao-titulo {
    font-size: 17px;
    font-weight: 700;
    letter-spacing: .4px;
}

.botao-sub {
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.seta {
    width: 34px;
    height: 34px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
    border-radius: 50%;
    font-size: 24px;
    border: 1px solid currentColor;
}

.agendar {
    color: white;
    background: linear-gradient(
        100deg,
        #ff4698,
        #fa147d 55%,
        #ff328e
    );
    box-shadow:
        0 0 19px rgba(255,34,126,.55),
        0 9px 25px rgba(255,27,110,.28),
        inset 0 2px 8px rgba(255,255,255,.28);
    animation: pulsar 2.8s ease-in-out infinite;
}

.agendar:hover {
    box-shadow:
        0 0 30px rgba(255,43,137,.8),
        0 12px 32px rgba(255,30,115,.45);
}

.servicos {
    color: #793849;
    background: linear-gradient(
        100deg,
        #ffc3cf,
        #ff94ac 65%,
        #f5a1b3
    );
    box-shadow:
        0 0 15px rgba(255,181,186,.38),
        0 8px 20px rgba(46,12,23,.2),
        inset 0 2px 8px rgba(255,255,255,.45);
}

.valores {
    color: #793849;
    background: linear-gradient(
        100deg,
        #fff2e8,
        #ffd6dc 65%,
        #ffe7e3
    );
    box-shadow:
        0 0 15px rgba(255,226,210,.4),
        0 8px 20px rgba(46,12,23,.2),
        inset 0 2px 8px rgba(255,255,255,.55);
}

.coroa {
    margin: -9px auto -4px;
    color: #ffd0a4;
    font-size: 27px;
    z-index: 1;
    filter: drop-shadow(0 0 8px #ffb07e);
}

.rodape {
    margin-top: 30px;
    color: #ffdbd5;
}

.ornamento {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 14px;
    font-size: 24px;
    color: #ffc2ce;
}

.ornamento::before,
.ornamento::after {
    content: "";
    width: 67px;
    height: 1px;
    background: rgba(255,209,197,.55);
}

.assinatura {
    margin-top: 10px;
    font-family: 'Great Vibes', cursive;
    font-size: 36px;
    line-height: 1.3;
    color: #ffe4d9;
    text-shadow: 0 0 12px rgba(255,173,176,.3);
}

.brilho {
    position: absolute;
    color: #ffcabd;
    font-size: 19px;
    pointer-events: none;
    animation: cintilar 3s ease-in-out infinite;
}

.brilho-1 {
    top: 12%;
    left: 7%;
}

.brilho-2 {
    top: 27%;
    right: 8%;
    animation-delay: 1s;
}

.brilho-3 {
    bottom: 12%;
    left: 8%;
    animation-delay: 2s;
}

@keyframes entrada {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulsar {
    0%,100% {
        box-shadow:
            0 0 16px rgba(255,34,126,.45),
            0 8px 23px rgba(255,27,110,.23);
    }
    50% {
        box-shadow:
            0 0 27px rgba(255,34,126,.7),
            0 10px 29px rgba(255,27,110,.4);
    }
}

@keyframes cintilar {
    0%,100% {
        opacity: .35;
        transform: scale(.8);
    }
    50% {
        opacity: 1;
        transform: scale(1.2);
    }
}

/* CELULARES */
@media (max-width: 600px) {

    body::before {
        background-position: 69% center;
        background-size: cover;
    }

    .pagina {
        min-height: 100dvh;
        padding: 20px 12px;
        align-items: center;
    }

    .painel {
        width: 100%;
        max-width: 420px;
        padding: 25px 19px 27px;
        border-radius: 29px;
        background: linear-gradient(
            155deg,
            rgba(105,40,55,.64),
            rgba(55,18,31,.82),
            rgba(110,44,60,.68)
        );
        border: 1px solid rgba(255,209,190,.85);
        box-shadow:
            0 0 24px rgba(255,150,170,.28),
            0 18px 55px rgba(35,8,20,.38),
            inset 0 0 18px rgba(255,196,183,.09);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
    }

    .painel::before {
        border-radius: 24px;
    }

    .logo {
        width: 108px;
        height: 108px;
        border-radius: 23px;
        box-shadow:
            0 0 0 4px rgba(255,198,187,.16),
            0 0 25px rgba(255,175,177,.48);
    }

    .nome {
        margin-top: 17px;
        gap: 8px;
    }

    .nome-kb {
        font-size: clamp(43px,12vw,60px);
    }

    .nome-lashes {
        font-size: clamp(49px,13vw,68px);
    }

    .subtitulo {
        margin: 7px 0 24px;
        font-size: 10px;
        letter-spacing: 2px;
        gap: 8px;
    }

    .subtitulo::before,
    .subtitulo::after {
        width: 20px;
    }

    .beneficios {
        margin-bottom: 26px;
    }

    .beneficio {
        padding: 5px 4px;
        font-size: 10px;
        line-height: 1.5;
    }

    .icone-beneficio {
        width: 43px;
        height: 43px;
        margin-bottom: 9px;
        font-size: 21px;
        box-shadow: 0 0 13px rgba(255,147,161,.3);
    }

    .botoes {
        gap: 13px;
    }

    .botao {
        min-height: 70px;
        padding: 10px 12px;
        border-radius: 40px;
    }

    .botao-icone {
        width: 35px;
        height: 38px;
        font-size: 22px;
    }

    .botao-titulo {
        font-size: 14px;
        letter-spacing: .2px;
    }

    .botao-sub {
        font-size: 8px;
        letter-spacing: 1px;
    }

    .seta {
        width: 28px;
        height: 28px;
        font-size: 20px;
    }

    .coroa {
        font-size: 24px;
        margin-bottom: -5px;
    }

    .rodape {
        margin-top: 25px;
    }

    .assinatura {
        font-size: 29px;
        margin-top: 8px;
    }

    .ornamento {
        font-size: 21px;
    }

    .ornamento::before,
    .ornamento::after {
        width: 48px;
    }

    .brilho {
        font-size: 15px;
    }
}

/* CELULARES PEQUENOS */
@media (max-width: 360px) {

    .painel {
        padding: 21px 12px;
    }

    .nome-kb {
        font-size: 40px;
    }

    .nome-lashes {
        font-size: 47px;
    }

    .beneficio {
        font-size: 9px;
    }

    .botao-titulo {
        font-size: 12px;
    }

    .botao-sub {
        font-size: 7px;
    }

    .assinatura {
        font-size: 26px;
    }
}

/* TELAS COM POUCA ALTURA */
@media (max-height: 700px) and (max-width: 600px) {

    .pagina {
        align-items: flex-start;
        padding-top: 12px;
        padding-bottom: 12px;
    }

    .painel {
        padding-top: 18px;
        padding-bottom: 18px;
    }

    .logo {
        width: 90px;
        height: 90px;
    }

    .nome {
        margin-top: 9px;
    }

    .subtitulo {
        margin-bottom: 15px;
    }

    .beneficios {
        margin-bottom: 16px;
    }

    .botao {
        min-height: 61px;
    }

    .botoes {
        gap: 9px;
    }

    .rodape {
        margin-top: 17px;
    }
}

@media (prefers-reduced-motion: reduce) {
    .painel,
    .agendar,
    .brilho {
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

<span class="brilho brilho-1">✦</span>
<span class="brilho brilho-2">✧</span>
<span class="brilho brilho-3">✦</span>

<img
    class="logo"
    src="/static/logo.png"
    alt="Logo KB Lashes"
>

<h1 class="nome">
    <span class="nome-kb">KB</span>
    <span class="nome-lashes">Lashes♡</span>
</h1>

<p class="subtitulo">
    <span>
        Extensão de cílios<br>
        Beleza feminina
    </span>
</p>

<div class="beneficios">

    <div class="beneficio">
        <div class="icone-beneficio">💎</div>
        Vagas limitadas hoje
    </div>

    <div class="beneficio">
        <div class="icone-beneficio">🗓️</div>
        Realce seu olhar em minutos
    </div>

    <div class="beneficio">
        <div class="icone-beneficio">💗</div>
        Atendimento profissional
    </div>

</div>

<nav class="botoes" aria-label="Links principais">

<div class="coroa">♛</div>

<a
    class="botao agendar"
    href="https://wa.me/5511964532697?text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio.%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA%20tem%20dispon%C3%ADveis%3F"
    target="_blank"
    rel="noopener noreferrer"
>
    <span class="botao-icone">🗓️</span>
    <span class="botao-texto">
        <span class="botao-titulo">AGENDAR AGORA</span>
        <span class="botao-sub">Garanta seu horário</span>
    </span>
    <span class="seta">›</span>
</a>

<a class="botao servicos" href="/servicos">
    <span class="botao-icone">✨</span>
    <span class="botao-texto">
        <span class="botao-titulo">VER SERVIÇOS</span>
        <span class="botao-sub">Conheça nossos procedimentos</span>
    </span>
    <span class="seta">›</span>
</a>

<a class="botao valores" href="/valores">
    <span class="botao-icone">💎</span>
    <span class="botao-texto">
        <span class="botao-titulo">VER VALORES</span>
        <span class="botao-sub">Veja nossos preços</span>
    </span>
    <span class="seta">›</span>
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
            <h3>{escape(nome)}</h3>
            <div class="desc">{escape(descricao)}</div>
            <div class="preco">{escape(preco)}</div>
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
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Valores | KB Lashes</title>

<style>
* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial,sans-serif;
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
