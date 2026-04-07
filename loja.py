from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

@loja_bp.route("/")
def home():
    return """
    <body style="margin:0;font-family:Arial;background:#ffe4ec;">

        <!-- TOPO -->
        <div style="background:#ff69b4;padding:40px;text-align:center;color:white;">
            <h1 style="margin:0;">Karen Brito Studio Beauty</h1>
            <p style="margin-top:10px;">Realçando sua beleza com cílios perfeitos 💖</p>
        </div>

        <!-- GALERIA -->
        <div style="padding:20px;text-align:center;">
            <h2>Resultados</h2>
        </div>

        <div style="display:flex;flex-wrap:wrap;gap:15px;justify-content:center;padding:20px;">

            <img src="https://i.postimg.cc/8crDvCph/02e0fb9f-b793-44fa-a92e-f0aa4b288d82.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/ZY9yHF0V/3b395467_be8b_418d_bb64_be5d02e7009b.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/fTNTdxdZ/31c710da_433e_4dff_8b83_92d9cdf145aa.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/kXmXSxS2/89a6469c_6e25_4ad6_a252_04bc4ccb1d4e.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/rwyVnMgJ/592a55cd_50cc_42cc_9d08_5a8875456ebd.jpg" style="width:250px;border-radius:12px;">
            <img src="https://i.postimg.cc/P56t09Rv/a2782b16_2f43_49d2_8765_df3085e24149.jpg" style="width:250px;border-radius:12px;">

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
                <h3>Hidra Gloss (hidratação)</h3>
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
        <div style="text-align:center;padding:40px;">
            <a href="https://wa.me/5511911524799?text=Olá quero agendar um horário"
               style="background:#25D366;color:white;padding:15px 30px;border-radius:10px;text-decoration:none;font-size:18px;">
               💬 Agendar pelo WhatsApp
            </a>
        </div>

    </body>
    """
