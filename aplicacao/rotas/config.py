import aplicacao.controladores.alunos_controlador as alunos_controlador
import aplicacao.controladores.inicial_controlador as inicial_controlador


def registrar(app):
    app.route("/", methods=["GET"])(inicial_controlador.inicial_index)

    app.route("/alunos", methods=["GET"])(alunos_controlador.alunos_index)
    app.route("/alunos", methods=["POST"])(alunos_controlador.alunos_criar)

