
from flask import Blueprint, url_for
from html import escape
from pathlib import Path

servicos_bp = Blueprint("servicos_bp", __name__)

WHATSAPP = (
    "https://wa.me/5511964532697?"
    "text=Oi%2C%20quero%20agendar%20um%20hor%C3%A1rio."
    "%20Quais%20dias%20e%20hor%C3%A1rios%20voc%C3%AA"
    "%20tem%20dispon%C3%ADveis%3F"
)


@servicos_bp.route("/servicos")
def servicos():

    pasta = Path(__file__).resolve().parent / "static"

    frases = [
        "Um olhar que encanta",
        "Beleza em cada detalhe",
        "Realce sua beleza natural",
        "Olhar marcante e delicado",
        "Cílios que fazem a diferença",
        "Seu olhar merece esse cuidado",
        "Elegância e sofisticação",
        "Um toque especial de beleza"
    ]

    # Imagens que não pertencem à galeria
    ignorar = {
        "logo.png",
        "logo.jpg",
        "logo.jpeg",
        "fundo-luxo.jpg",
        "fundo-luxo.png",
        "fundo-login.png",
        "favicon.png"
    }

    extensoes = {".png", ".jpg", ".jpeg", ".webp"}

    arquivos = []

    if pasta.exists():
        arquivos = sorted(
            [
                arquivo
                for arquivo in pasta.iterdir()
                if arquivo.is_file()
                and arquivo.suffix.lower() in extensoes
                and arquivo.name.lower() not in ignorar
                and not arquivo.name.lower().startswith(
                    ("logo", "fundo", "banner", "background")
                )
            ],
            key=lambda arquivo: arquivo.name.lower()
        )

    imagens_html = ""

    for i, arquivo in enumerate(arquivos):

        frase = frases[i % len(frases)]

        imagem_url = url_for(
            "static",
            filename=arquivo.name
        )

        imagens_html += f"""
        <button
            type="button"
            class="card"
            data-imagem="{escape(imagem_url, quote=True)}"
            data-legenda="{escape(frase, quote=True)}"
            aria-label="Ampliar trabalho {i + 1}"
        >
            <div class="foto">
                <img
                    src="{escape(imagem_url, quote=True)}"
                    alt="Trabalho de beleza KB Lashes {i + 1}"
                    loading="lazy"
                >
                <span class="zoom">⤢</span>
            </div>

            <div class="card-info">
                <span class="numero">
                    TRABALHO {i + 1:02d}
                </span>

                <h3>{escape(frase)}</h3>

                <span class="detalhe">
                    KB Lashes Beauty ♡
                </span>
            </div>
        </button>
        """

    if not arquivos:
        imagens_html = """
        <div class="vazio">
            <div class="vazio-icone">♡</div>
            <h3>Nossa galeria está sendo preparada</h3>
            <p>Em breve, novos trabalhos por aqui!</p>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="pt-BR">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#542b37">

<title>Nossos Trabalhos | KB Lashes</title>

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
    background: #542b37;
    color: #fff0e9;
    isolation: isolate;
}}

body::before {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -2;
    background:
        linear-gradient(
            180deg,
            rgba(49,16,28,.65),
            rgba(56,20,34,.88)
        ),
        url('/static/fundo-luxo.jpg')
        center/cover no-repeat;
}}

body::after {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    pointer-events: none;
    background: radial-gradient(
        ellipse at top,
        rgba(255,146,175,.16),
        transparent 70%
    );
}}

a {{
    text-decoration: none;
}}

.topo {{
    padding: 25px 20px 45px;
    text-align: center;
}}

.voltar {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #ffe3db;
    font-size: 13px;
    font-weight: 600;
    padding: 11px 20px;
    border: 1px solid rgba(255,211,200,.45);
    border-radius: 50px;
    background: rgba(68,24,39,.55);
    transition: .3s;
}}

.voltar:hover {{
    background: rgba(255,139,177,.25);
    transform: translateY(-2px);
}}

.logo {{
    display: block;
    width: 105px;
    height: 105px;
    margin: 30px auto 13px;
    object-fit: cover;
    border-radius: 23px;
    border: 4px solid #ffe4dd;
    box-shadow:
        0 0 25px rgba(255,172,177,.4),
        0 10px 30px rgba(0,0,0,.2);
}}

.marca {{
    margin: 0;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(35px,6vw,55px);
    font-weight: 500;
    color: #ffe5dc;
}}

.marca span {{
    font-family: 'Great Vibes', cursive;
    font-size: 1.25em;
    font-weight: 400;
    color: #ff9cbd;
}}

.etiqueta {{
    display: inline-block;
    margin-top: 16px;
    padding: 8px 18px;
    border: 1px solid rgba(255,197,190,.45);
    border-radius: 50px;
    background: rgba(255,161,176,.12);
    color: #ffd3d3;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}}

.titulo {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(30px,5vw,47px);
    font-weight: 500;
    margin: 19px 0 10px;
    color: #fff0e6;
}}

.descricao {{
    max-width: 550px;
    margin: 0 auto;
    color: #f7d7d5;
    font-size: 15px;
    line-height: 1.8;
}}

.ornamento {{
    margin: 23px auto 0;
    color: #ffc3cd;
    font-size: 25px;
}}

.container {{
    width: min(1180px, calc(100% - 36px));
    margin: 0 auto;
}}

.cabecalho-galeria {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin: 0 0 24px;
    padding-bottom: 17px;
    border-bottom: 1px solid rgba(255,213,203,.27);
}}

.cabecalho-galeria h2 {{
    margin: 0;
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 25px;
    font-weight: 500;
    color: #ffe8de;
}}

.contador {{
    font-size: 12px;
    color: #ffcfda;
    background: rgba(255,177,193,.12);
    border: 1px solid rgba(255,205,202,.24);
    padding: 9px 14px;
    border-radius: 30px;
}}

.feed {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0,1fr));
    gap: 23px;
}}

.card {{
    display: block;
    width: 100%;
    min-width: 0;
    padding: 8px;
    text-align: left;
    color: inherit;
    font: inherit;
    cursor: pointer;
    border-radius: 24px;
    border: 1px solid rgba(255,206,195,.47);
    background: linear-gradient(
        145deg,
        rgba(119,56,70,.74),
        rgba(58,22,37,.88)
    );
    box-shadow:
        0 12px 30px rgba(20,5,13,.25),
        inset 0 0 14px rgba(255,205,195,.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition:
        transform .3s ease,
        box-shadow .3s ease,
        border-color .3s ease;
}}

.card:hover {{
    transform: translateY(-7px);
    border-color: #ffd0c6;
    box-shadow:
        0 20px 42px rgba(20,5,13,.36),
        0 0 22px rgba(255,150,173,.2);
}}

.card:focus-visible {{
    outline: 3px solid #ff9cb9;
    outline-offset: 4px;
}}

.foto {{
    position: relative;
    height: 310px;
    overflow: hidden;
    border-radius: 17px;
    background: #6a3848;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.foto img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    transition: transform .4s ease;
}}

.card:hover .foto img {{
    transform: scale(1.035);
}}

.zoom {{
    position: absolute;
    top: 12px;
    right: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(55,18,30,.7);
    color: #fff1ea;
    border: 1px solid rgba(255,224,215,.6);
    font-size: 24px;
}}

.card-info {{
    padding: 18px 12px 16px;
}}

.numero {{
    color: #ffb3c9;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}}

.card-info h3 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 500;
    color: #fff0e9;
    font-size: 21px;
    margin: 9px 0 10px;
}}

.detalhe {{
    font-family: 'Great Vibes', cursive;
    color: #ffb9ce;
    font-size: 23px;
}}

.vazio {{
    grid-column: 1/-1;
    text-align: center;
    padding: 60px 20px;
    border: 1px solid rgba(255,211,203,.35);
    border-radius: 25px;
    background: rgba(66,24,39,.65);
}}

.vazio-icone {{
    font-size: 50px;
    color: #ffb7ca;
}}

.vazio h3 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 500;
}}

.cta {{
    max-width: 720px;
    margin: 65px auto 50px;
    padding: 35px 25px;
    border-radius: 30px;
    text-align: center;
    background: linear-gradient(
        140deg,
        rgba(126,54,72,.77),
        rgba(64,20,38,.88)
    );
    border: 1px solid rgba(255,202,194,.55);
    box-shadow: 0 15px 45px rgba(28,6,16,.3);
}}

.cta h2 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(26px,5vw,37px);
    font-weight: 500;
    margin: 0 0 12px;
}}

.cta p {{
    color: #ffdad7;
    font-size: 14px;
    line-height: 1.7;
    margin: 0 0 25px;
}}

.botao {{
    display: inline-flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    width: min(100%,380px);
    min-height: 58px;
    padding: 14px 20px;
    border-radius: 50px;
    background: linear-gradient(
        90deg,
        #ff4899,
        #fa167e
    );
    color: white;
    font-weight: 700;
    font-size: 14px;
    box-shadow:
        0 0 19px rgba(255,38,128,.42),
        0 8px 24px rgba(255,38,128,.23);
    transition: .3s;
}}

.botao:hover {{
    transform: translateY(-3px);
    box-shadow: 0 0 29px rgba(255,38,128,.6);
}}

.rodape {{
    padding: 25px 15px 35px;
    text-align: center;
    color: #f6c8ce;
    font-size: 12px;
}}

.assinatura {{
    font-family: 'Great Vibes', cursive;
    font-size: 30px;
    color: #ffced4;
    margin-bottom: 7px;
}}

/* VISUALIZADOR DE FOTOS */
.modal {{
    display: none;
    position: fixed;
    inset: 0;
    z-index: 9999;
    align-items: center;
    justify-content: center;
    padding: 65px 15px 30px;
    background: rgba(20,5,13,.94);
    backdrop-filter: blur(12px);
}}

.modal.ativo {{
    display: flex;
}}

.modal-conteudo {{
    max-width: 95vw;
    text-align: center;
}}

.modal img {{
    display: block;
    max-width: 92vw;
    max-height: 76vh;
    max-height: 76dvh;
    width: auto;
    height: auto;
    margin: 0 auto;
    object-fit: contain;
    border-radius: 15px;
    border: 1px solid rgba(255,207,199,.55);
    box-shadow: 0 15px 50px rgba(0,0,0,.4);
}}

.modal-legenda {{
    color: #ffe1de;
    margin-top: 15px;
    font-size: 15px;
}}

.fechar {{
    position: absolute;
    top: 18px;
    right: 20px;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    border: 1px solid #ffbdc9;
    background: #7c344c;
    color: white;
    font-size: 26px;
    cursor: pointer;
}}

body.modal-aberto {{
    overflow: hidden;
}}

/* TABLET */
@media(max-width:900px) {{
    .feed {{
        grid-template-columns: repeat(2,minmax(0,1fr));
        gap: 17px;
    }}

    .foto {{
        height: 290px;
    }}
}}

/* CELULAR */
@media(max-width:600px) {{

    body::before {{
        background-position: 65% center;
    }}

    .topo {{
        padding: 20px 14px 33px;
    }}

    .logo {{
        width: 90px;
        height: 90px;
        margin-top: 25px;
    }}

    .marca {{
        font-size: 38px;
    }}

    .etiqueta {{
        font-size: 9px;
        letter-spacing: 1.5px;
    }}

    .titulo {{
        font-size: 32px;
    }}

    .descricao {{
        font-size: 13px;
        padding: 0 8px;
    }}

    .container {{
        width: calc(100% - 26px);
    }}

    .cabecalho-galeria {{
        gap: 10px;
    }}

    .cabecalho-galeria h2 {{
        font-size: 21px;
    }}

    .contador {{
        font-size: 10px;
        padding: 8px 10px;
        white-space: nowrap;
    }}

    .feed {{
        grid-template-columns: 1fr;
        gap: 19px;
    }}

    .card {{
        padding: 7px;
        border-radius: 22px;
    }}

    .foto {{
        height: 330px;
        border-radius: 16px;
    }}

    .card-info {{
        padding: 15px 12px;
    }}

    .card-info h3 {{
        font-size: 21px;
    }}

    .cta {{
        margin: 42px auto 35px;
        padding: 30px 17px;
        border-radius: 25px;
    }}

    .cta h2 {{
        font-size: 29px;
    }}

    .botao {{
        font-size: 13px;
    }}
}}

@media(max-width:360px) {{
    .foto {{
        height: 270px;
    }}

    .marca {{
        font-size: 33px;
    }}

    .cabecalho-galeria h2 {{
        font-size: 18px;
    }}
}}

@media(prefers-reduced-motion:reduce) {{
    *,
    *::before,
    *::after {{
        scroll-behavior: auto !important;
        transition: none !important;
    }}
}}

</style>
</head>

<body>

<header class="topo">

    <a href="/" class="voltar">
        ← Voltar ao início
    </a>

    <img
        class="logo"
        src="/static/logo.png"
        alt="Logo KB Lashes"
    >

    <h1 class="marca">
        KB <span>Lashes</span>
    </h1>

    <div class="etiqueta">
        ✨ Nosso portfólio de beleza
    </div>

    <h2 class="titulo">
        Nossos Trabalhos
    </h2>

    <p class="descricao">
        Cada olhar tem sua beleza única.
        Conheça alguns dos nossos trabalhos
        e inspire-se para realçar ainda mais o seu!
    </p>

    <div class="ornamento">♡</div>

</header>

<main class="container">

    <div class="cabecalho-galeria">
        <h2>Galeria de beleza</h2>
        <span class="contador">
            {len(arquivos)} trabalhos
        </span>
    </div>

    <div class="feed">
        {imagens_html}
    </div>

    <section class="cta">

        <h2>
            Pronta para realçar seu olhar?
        </h2>

        <p>
            Seu momento de beleza começa aqui.
            Entre em contato e agende seu atendimento!
        </p>

        <a
            href="{WHATSAPP}"
            class="botao"
            target="_blank"
            rel="noopener noreferrer"
        >
            💗 AGENDAR MEU HORÁRIO →
        </a>

    </section>

</main>

<footer class="rodape">
    <div class="assinatura">
        Mais que cílios, autoestima ♡
    </div>

    KB Lashes Beauty
</footer>

<div
    id="modal"
    class="modal"
    role="dialog"
    aria-modal="true"
    aria-label="Visualização de trabalho"
    aria-hidden="true"
>
    <button
        type="button"
        class="fechar"
        id="fecharModal"
        aria-label="Fechar imagem"
    >
        ×
    </button>

    <div class="modal-conteudo">
        <img id="imgModal" alt="Trabalho ampliado">
        <p class="modal-legenda" id="legendaModal"></p>
    </div>
</div>

<script>
(function() {{
    const modal = document.getElementById("modal");
    const imagem = document.getElementById("imgModal");
    const legenda = document.getElementById("legendaModal");
    const fechar = document.getElementById("fecharModal");

    let ultimoFoco = null;

    function abrirImagem(src, texto) {{
        ultimoFoco = document.activeElement;

        imagem.src = src;
        imagem.alt = texto;
        legenda.textContent = texto;

        modal.classList.add("ativo");
        modal.setAttribute("aria-hidden", "false");

        document.body.classList.add("modal-aberto");
        fechar.focus();
    }}

    function fecharImagem() {{
        modal.classList.remove("ativo");
        modal.setAttribute("aria-hidden", "true");

        document.body.classList.remove("modal-aberto");

        imagem.removeAttribute("src");

        if (ultimoFoco) {{
            ultimoFoco.focus();
        }}
    }}

    document.querySelectorAll(".card").forEach(card => {{
        card.addEventListener("click", () => {{
            abrirImagem(
                card.dataset.imagem,
                card.dataset.legenda
            );
        }});
    }});

    fechar.addEventListener("click", fecharImagem);

    modal.addEventListener("click", evento => {{
        if (evento.target === modal) {{
            fecharImagem();
        }}
    }});

    document.addEventListener("keydown", evento => {{
        if (!modal.classList.contains("ativo")) return;

        if (evento.key === "Escape") {{
            fecharImagem();
        }}

        if (evento.key === "Tab") {{
            evento.preventDefault();
            fechar.focus();
        }}
    }});
}})();
</script>

</body>
</html>
"""
