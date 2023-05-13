from flask import Flask
from flask_cors import CORS

import aplicacao.rotas.config as rotas

app = Flask(__name__)
rotas.registrar(app)
CORS(app)

if __name__ == "__main__":
    app.run()
