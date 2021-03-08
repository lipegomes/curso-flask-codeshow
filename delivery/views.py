from flask import Flask


# Type annotation (app: Flask) define que app é uma instância do Flask
def init_app(app: Flask):
    """Factory de inicialização de extensões"""

    @app.route("/")  # Decorator para definir a rota para "/"
    def index():
        return "<h1>Hello, Filipe !!!</h1>"

    @app.route("/sobre")  # Decorator para definir a rota para "/sobre"
    def sobre():
        return (
            "<h1>Somos uma startup de delivery com foco em atender pequenos"
            "e médios empreendimentos.</h1>"
        )
