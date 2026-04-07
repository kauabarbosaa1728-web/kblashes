from flask import Blueprint

loja_bp = Blueprint("loja", __name__)

@loja_bp.route("/")
def home():
    return """
    <body style="margin:0;font-family:Arial;background:#fff5f8;">
        <div style="background:#ff69b4;padding:30px;text-align:center;color:white;">
            <h1 style="margin:0;">KB Lashes</h1>
            <p style="margin-top:10px;">Cílios que valorizam seu olhar</p>
        </div>

        <div style="padding:30px;text-align:center;">
            <h2>Nossos Produtos</h2>
        </div>

        <div style="display:flex;justify-content:center;gap:20px;flex-wrap:wrap;padding:20px;">

            <div style="background:white;border-radius:12px;padding:20px;width:220px;box-shadow:0 2px 10px rgba(0,0,0,0.1);text-align:center;">
                <img src="https://via.placeholder.com/200x200" style="width:100%;border-radius:10px;">
                <h3>Cílios Volume Russo</h3>
                <p>R$ 29,90</p>
                <a href="https://wa.me/5511911524799?text=Ol%C3%A1%2C%20quero%20comprar%20os%20C%C3%ADlios%20Volume%20Russo"
                   style="display:inline-block;background:#25D366;color:white;padding:12px 18px;border-radius:8px;text-decoration:none;">
                   Comprar no WhatsApp
                </a>
            </div>

            <div style="background:white;border-radius:12px;padding:20px;width:220px;box-shadow:0 2px 10px rgba(0,0,0,0.1);text-align:center;">
                <img src="https://via.placeholder.com/200x200" style="width:100%;border-radius:10px;">
                <h3>Kit Cílios Completo</h3>
                <p>R$ 59,90</p>
                <a href="https://wa.me/5511911524799?text=Ol%C3%A1%2C%20quero%20comprar%20o%20Kit%20C%C3%ADlios%20Completo"
                   style="display:inline-block;background:#25D366;color:white;padding:12px 18px;border-radius:8px;text-decoration:none;">
                   Comprar no WhatsApp
                </a>
            </div>

        </div>
    </body>
    """
