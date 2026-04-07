from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

@loja_bp.route("/")
def home():
    return """
    <body style="margin:0;font-family:Arial;background:#ffe4ec;">

        <div style="background:#ff69b4;padding:30px;text-align:center;color:white;">
            <h1>Karen Brito Studio Beauty</h1>
            <p>Realçando sua beleza 💖</p>
        </div>

        <div style="padding:20px;text-align:center;">
            <h2>Nossos Serviços</h2>
        </div>

        <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:20px;padding:20px;">

            <div style="background:white;padding:20px;border-radius:12px;width:250px;">
                <h3>Designer de sobrancelhas</h3>
                <p>R$ 40,00</p>
            </div>

            <div style="background:white;padding:20px;border-radius:12px;width:250px;">
                <h3>Hidra Gloss</h3>
                <p>R$ 25,00</p>
            </div>

            <div style="background:white;padding:20px;border-radius:12px;width:250px;">
                <h3>Extensão Brasileiro</h3>
                <p>R$ 120,00</p>
                <small>Manutenção: R$ 50,00</small>
            </div>

            <div style="background:white;padding:20px;border-radius:12px;width:250px;">
                <h3>Extensão Fox</h3>
                <p>R$ 160,00</p>
                <small>Manutenção: R$ 90,00</small>
            </div>

            <div style="background:white;padding:20px;border-radius:12px;width:250px;">
                <h3>Extensão Egípcio</h3>
                <p>R$ 140,00</p>
                <small>Manutenção: R$ 60,00</small>
            </div>

        </div>

        <div style="text-align:center;padding:30px;">
            <a href="https://wa.me/5511911524799?text=Olá quero agendar um horário"
               style="background:#25D366;color:white;padding:15px 25px;border-radius:10px;text-decoration:none;">
               💬 Agendar no WhatsApp
            </a>
        </div>

    </body>
    """
