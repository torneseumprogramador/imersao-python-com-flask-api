from flask import Flask, jsonify

import aplicacao.rotas.config as rotas

app = Flask(__name__)

rotas.registrar(app)

if __name__ == "__main__":
    app.run()
