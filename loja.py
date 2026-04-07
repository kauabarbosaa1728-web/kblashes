from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

@loja_bp.route("/")
def home():
    return """
    <body style="margin:0;font-family:Arial;background:#ffe4ec;">

        <!-- TOPO -->
        <div style="background:#ff69b4;padding:30px;text-align:center;color:white;">
            <h1>Karen Brito Studio Beauty</h1>
            <p>Realçando sua beleza com cílios perfeitos 💖</p>
        </div>

        <!-- GALERIA -->
        <div style="padding:20px;text-align:center;">
            <h2>Resultados</h2>
        </div>

        <div style="display:flex;flex-wrap:wrap;gap:15px;justify-content:center;padding:20px;">

            <img src="https://i.postimg.cc/02e0fb9f/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/3b395467/3b395467-be8b-418d-bb64-be5d02e7009b.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/31c710da/31c710da-433e-4dff-8b83-92d9cdf145aa.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/89a6469c/89a6469c-6e25-4ad6-a252-04bc4ccb1d4e.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/592a55cd/592a55cd-50cc-42cc-9d08-5a8875456ebd.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/a2782b16/a2782b16-2f43-49d2-8765-df3085e24149.jpg" style="width:250px;border-radius:12px;">

        </div>

        <!-- SERVIÇOS -->
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

        <!-- WHATSAPP -->
        <div style="text-align:center;padding:30px;">
            <a href="https://wa.me/5511911524799?text=Olá quero agendar um horário"
               style="background:#25D366;color:white;padding:15px 25px;border-radius:10px;text-decoration:none;font-size:18px;">
               💬 Agendar pelo WhatsApp
            </a>
        </div>

    </body>
    """
