import aplicacao.controladores.alunos_controlador as alunos_controlador
import aplicacao.controladores.inicial_controlador as inicial_controlador


def registrar(app):
    app.route("/")(inicial_controlador.inicial_index)
    app.route("/alunos")(alunos_controlador.alunos_index)

