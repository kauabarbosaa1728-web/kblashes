
from flask import Blueprint
from html import escape
from urllib.parse import quote

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


# ==================================================
# PÁGINA DE VALORES - DESIGN PREMIUM KB LASHES
# ==================================================

@loja_bp.route("/valores")
def valores():

    cards = [
        (
            "✦",
            "Designer de sobrancelhas",
            "Definição perfeita para valorizar a beleza do seu rosto.",
            "R$ 40,00"
        ),
        (
            "♡",
            "Hidra Gloss",
            "Lábios hidratados, macios e com brilho natural.",
            "R$ 25,00"
        ),
        (
            "✧",
            "Extensão Brasileiro",
            "Volume leve e natural para realçar seu olhar.",
            "R$ 120,00"
        ),
        (
            "♛",
            "Extensão Fox",
            "Efeito alongado, elegante e marcante.",
            "R$ 160,00"
        ),
        (
            "❀",
            "Extensão Egípcio",
            "Olhar sofisticado, delicado e cheio de personalidade.",
            "R$ 140,00"
        )
    ]

    conteudo = ""

    for i, (icone, nome, descricao, preco) in enumerate(cards, 1):

        mensagem = quote(
            f"Olá! Vim pelo site da KB Lashes e gostaria "
            f"de agendar {nome}. Quais horários estão disponíveis?"
        )

        link = f"https://wa.me/5511964532697?text={mensagem}"

        conteudo += f"""
        <article class="card">

            <div class="card-topo">
                <span class="numero">
                    PROCEDIMENTO {i:02d}
                </span>

                <div class="icone">
                    {escape(icone)}
                </div>
            </div>

            <div class="card-conteudo">
                <h3>{escape(nome)}</h3>

                <p class="descricao">
                    {escape(descricao)}
                </p>
            </div>

            <div class="preco-area">
                <span>INVESTIMENTO</span>

                <strong>
                    {escape(preco)}
                </strong>
            </div>

            <a
                class="agendar-card"
                href="{escape(link, quote=True)}"
                target="_blank"
                rel="noopener noreferrer"
            >
                ♡ AGENDAR PROCEDIMENTO
                <span>›</span>
            </a>

        </article>
        """

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#542b37">
<meta name="description" content="Confira os procedimentos e valores da KB Lashes.">

<title>Nossos Valores | KB Lashes</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet">

<style>

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    min-height: 100vh;
    font-family: 'DM Sans', Arial, sans-serif;
    color: #ffe9e3;
    background: #542b37;
    isolation: isolate;
}}

body::before {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -2;

    background:
        linear-gradient(
            120deg,
            rgba(43,13,25,.60),
            rgba(66,25,40,.75)
        ),
        url('/static/fundo-luxo.jpg')
        center/cover no-repeat;
}}

body::after {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;

    background: radial-gradient(
        ellipse at top,
        rgba(255,164,184,.20),
        transparent 75%
    );

    pointer-events: none;
}}

a {{
    text-decoration: none;
}}

.topo {{
    text-align: center;
    padding: 28px 18px 48px;
}}

.voltar {{
    display: inline-flex;
    align-items: center;
    justify-content: center;

    padding: 13px 25px;
    border-radius: 50px;

    border: 1px solid rgba(255,214,201,.60);
    background: rgba(73,25,42,.65);

    color: #ffe4df;
    font-size: 13px;
    font-weight: 600;

    transition: .3s;
}}

.voltar:hover {{
    background: rgba(255,159,187,.25);
    transform: translateY(-3px);
}}

.logo {{
    display: block;

    width: 115px;
    height: 115px;

    object-fit: cover;

    margin: 35px auto 17px;
    padding: 5px;

    border-radius: 25px;

    background: #ffe9e0;
    border: 2px solid #fff1e7;

    box-shadow:
        0 0 30px rgba(255,165,183,.55),
        0 12px 35px rgba(0,0,0,.25);
}}

.marca {{
    margin: 0;

    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(40px,6vw,60px);
    font-weight: 500;

    color: #ffe9df;
}}

.marca span {{
    font-family: 'Great Vibes', cursive;
    font-size: 1.3em;
    font-weight: 400;

    color: #ff9cba;
}}

.etiqueta {{
    display: inline-block;

    margin-top: 24px;
    padding: 10px 20px;

    border-radius: 50px;

    border: 1px solid rgba(255,198,192,.50);
    background: rgba(255,160,186,.13);

    color: #ffd5dc;

    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}}

.titulo {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(35px,5vw,55px);
    font-weight: 500;

    margin: 20px 0 12px;

    color: #fff0e7;
}}

.subtitulo {{
    max-width: 560px;
    margin: auto;

    color: #f8d6d6;

    font-size: 15px;
    line-height: 1.8;
}}

.ornamento {{
    margin-top: 23px;
    color: #ffb8c8;
    font-size: 25px;
}}

.container {{
    width: min(1160px, calc(100% - 36px));
    margin: 0 auto;
}}

.cabecalho {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;

    padding-bottom: 18px;
    margin-bottom: 25px;

    border-bottom: 1px solid rgba(255,207,199,.3);
}}

.cabecalho h2 {{
    margin: 0;

    font-family: 'Playfair Display', Georgia, serif;
    font-size: 27px;
    font-weight: 500;
}}

.quantidade {{
    padding: 10px 16px;
    border-radius: 30px;

    background: rgba(255,177,192,.13);
    border: 1px solid rgba(255,213,202,.3);

    color: #ffcfda;
    font-size: 12px;
}}

.grade {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0,1fr));
    gap: 23px;
}}

.card {{
    position: relative;

    display: flex;
    flex-direction: column;

    min-width: 0;
    padding: 27px 23px 23px;

    border-radius: 29px;

    border: 1px solid rgba(255,209,194,.65);

    background: linear-gradient(
        150deg,
        rgba(125,53,72,.78),
        rgba(59,20,36,.92)
    );

    box-shadow:
        0 17px 45px rgba(26,6,17,.32),
        inset 0 0 20px rgba(255,194,185,.08);

    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);

    transition:
        transform .3s,
        box-shadow .3s;

    overflow: hidden;
}}

.card::before {{
    content: "";

    position: absolute;
    top: -60px;
    right: -60px;

    width: 150px;
    height: 150px;

    background: radial-gradient(
        circle,
        rgba(255,187,195,.19),
        transparent 70%
    );

    pointer-events: none;
}}

.card:hover {{
    transform: translateY(-8px);

    box-shadow:
        0 25px 55px rgba(26,6,17,.45),
        0 0 27px rgba(255,157,183,.25);
}}

.card-topo {{
    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 27px;
}}

.numero {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.7px;

    color: #ffc5d0;
}}

.icone {{
    display: flex;
    align-items: center;
    justify-content: center;

    width: 53px;
    height: 53px;

    border-radius: 50%;

    border: 1px solid rgba(255,207,195,.7);
    background: rgba(255,179,194,.15);

    color: #ffd7bd;
    font-size: 29px;

    box-shadow: 0 0 18px rgba(255,164,185,.25);
}}

.card-conteudo {{
    flex: 1;
}}

.card h3 {{
    margin: 0 0 15px;

    font-family: 'Playfair Display', Georgia, serif;
    font-size: 26px;
    font-weight: 500;

    color: #fff0e8;

    line-height: 1.3;
}}

.descricao {{
    min-height: 60px;
    margin: 0;

    color: #f4d1d0;

    font-size: 13px;
    line-height: 1.8;
}}

.preco-area {{
    display: flex;
    flex-direction: column;
    gap: 9px;

    margin: 23px 0;
    padding-top: 22px;

    border-top: 1px solid rgba(255,211,201,.3);
}}

.preco-area span {{
    color: #ffc3cf;

    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}}

.preco-area strong {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 39px;
    font-weight: 500;

    color: #ffb5ce;

    text-shadow: 0 0 17px rgba(255,125,169,.25);
}}

.agendar-card {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;

    min-height: 57px;
    padding: 12px;

    border-radius: 50px;

    background: linear-gradient(
        90deg,
        #ff4a99,
        #fa187f
    );

    color: white;

    font-size: 11px;
    font-weight: 700;
    letter-spacing: .3px;

    box-shadow:
        0 0 20px rgba(255,39,125,.4),
        0 9px 22px rgba(255,31,115,.25);

    transition: .25s;
}}

.agendar-card span {{
    display: flex;
    align-items: center;
    justify-content: center;

    width: 25px;
    height: 25px;

    border: 1px solid rgba(255,255,255,.7);
    border-radius: 50%;

    font-size: 20px;
}}

.agendar-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 0 30px rgba(255,39,125,.65);
}}

.agendar-card:focus-visible,
.voltar:focus-visible,
.cta-botao:focus-visible {{
    outline: 3px solid white;
    outline-offset: 4px;
}}

.cta {{
    max-width: 760px;

    margin: 70px auto 45px;
    padding: 42px 25px;

    text-align: center;

    border-radius: 32px;
    border: 1px solid rgba(255,206,194,.65);

    background: linear-gradient(
        140deg,
        rgba(127,54,74,.82),
        rgba(57,18,34,.92)
    );

    box-shadow: 0 18px 50px rgba(28,6,16,.35);

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}}

.cta h2 {{
    margin: 12px 0 15px;

    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(27px,4vw,40px);
    font-weight: 500;
}}

.cta p {{
    margin: 0 0 27px;

    color: #f9d6d6;

    font-size: 14px;
    line-height: 1.9;
}}

.cta-botao {{
    display: inline-flex;
    align-items: center;
    justify-content: center;

    width: min(100%,390px);
    min-height: 59px;

    padding: 15px 22px;
    border-radius: 50px;

    background: linear-gradient(
        90deg,
        #ffc5d1,
        #fa92af
    );

    color: #763449;

    font-weight: 700;
    font-size: 13px;

    box-shadow: 0 9px 27px rgba(255,137,173,.25);

    transition: .25s;
}}

.cta-botao:hover {{
    transform: translateY(-3px);
}}

.rodape {{
    text-align: center;

    padding: 20px 15px 38px;

    color: #f4c9d0;
    font-size: 12px;
}}

.assinatura {{
    font-family: 'Great Vibes', cursive;
    font-size: 34px;

    color: #ffd5d7;

    margin-bottom: 9px;
}}

/* TABLETS */

@media(max-width:950px) {{

    .grade {{
        grid-template-columns: repeat(2,minmax(0,1fr));
    }}

}}

/* CELULARES */

@media(max-width:600px) {{

    body::before {{
        background-position: 65% center;
    }}

    .topo {{
        padding: 20px 13px 35px;
    }}

    .logo {{
        width: 100px;
        height: 100px;
        margin-top: 27px;
    }}

    .marca {{
        font-size: 41px;
    }}

    .titulo {{
        font-size: 37px;
    }}

    .subtitulo {{
        font-size: 13px;
        padding: 0 8px;
    }}

    .etiqueta {{
        font-size: 9px;
        letter-spacing: 1.3px;
    }}

    .container {{
        width: calc(100% - 26px);
    }}

    .cabecalho h2 {{
        font-size: 22px;
    }}

    .quantidade {{
        font-size: 10px;
        padding: 8px 11px;
        white-space: nowrap;
    }}

    .grade {{
        grid-template-columns: 1fr;
        gap: 19px;
    }}

    .card {{
        padding: 24px 21px;
        border-radius: 27px;
    }}

    .card-topo {{
        margin-bottom: 21px;
    }}

    .card h3 {{
        font-size: 26px;
    }}

    .descricao {{
        min-height: auto;
    }}

    .preco-area {{
        margin: 21px 0;
    }}

    .preco-area strong {{
        font-size: 38px;
    }}

    .agendar-card {{
        min-height: 59px;
        font-size: 12px;
    }}

    .cta {{
        margin: 45px auto 32px;
        padding: 32px 19px;
        border-radius: 27px;
    }}

    .cta h2 {{
        font-size: 30px;
    }}

}}

@media(max-width:360px) {{

    .card {{
        padding: 21px 17px;
    }}

    .agendar-card {{
        font-size: 10px;
    }}

    .marca {{
        font-size: 35px;
    }}

}}

@media(prefers-reduced-motion:reduce) {{

    *,
    *::before,
    *::after {{
        transition: none !important;
        scroll-behavior: auto !important;
    }}

}}

</style>
</head>

<body>

<header class="topo">

    <a class="voltar" href="/">
        ← Voltar ao início
    </a>

    <img
        class="logo"
        src="/static/logo.png"
        alt="Logo KB Lashes"
    >

    <h1 class="marca">
        KB <span>Lashes♡</span>
    </h1>

    <div class="etiqueta">
        ♡ Beleza, cuidado e sofisticação
    </div>

    <h2 class="titulo">
        Nossos Valores
    </h2>

    <p class="subtitulo">
        Sua beleza merece um cuidado especial.
        Conheça nossos procedimentos e escolha
        o seu próximo momento de autoestima.
    </p>

    <div class="ornamento">
        ✧ ♡ ✧
    </div>

</header>

<main class="container">

    <div class="cabecalho">

        <h2>
            Nossos Procedimentos
        </h2>

        <span class="quantidade">
            {len(cards)} opções
        </span>

    </div>

    <section class="grade" aria-label="Lista de procedimentos">
        {conteudo}
    </section>

    <section class="cta">

        <div class="ornamento">
            ♡
        </div>

        <h2>
            Seu momento de brilhar chegou!
        </h2>

        <p>
            Escolha o procedimento ideal para você
            e entre em contato para agendar seu horário.
            Será um prazer cuidar da sua beleza!
        </p>

        <a
            href="{WHATSAPP}"
            class="cta-botao"
            target="_blank"
            rel="noopener noreferrer"
        >
            ♡ FALAR COM A KB LASHES →
        </a>

    </section>

</main>

<footer class="rodape">

    <div class="assinatura">
        Mais que cílios, autoestima ♡
    </div>

    KB Lashes Beauty

</footer>

</body>
</html>
"""
