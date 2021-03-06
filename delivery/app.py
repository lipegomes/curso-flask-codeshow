from flask import Flask

app = Flask(__name__)


@app.route("/")  # decorator para definir a rota para "/"
def index():
    return "<h1>Hello, Filipe !!!</h1>"


@app.route("/sobre")  # decorator para definir a rota para "/sobre"
def sobre():
    return "<h1>Somos uma startup de delivery com foco em atender pequenos e médios empreendimentos.</h1>"
