def container(conteudo):
    return f"""
    <html>
    <head>
        <title>KB Lashes</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
        body {{
            margin: 0;
            font-family: Arial;
            background: #111;
            color: white;
        }}

        h2 {{
            color: #ff2d7a;
        }}

        a {{
            text-decoration: none;
        }}
        </style>

    </head>

    <body>

    {conteudo}

    </body>
    </html>
    """
