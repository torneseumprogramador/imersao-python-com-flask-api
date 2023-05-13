import aplicacao.controladores.alunos_controlador as alunos_controlador
import aplicacao.controladores.inicial_controlador as inicial_controlador


def registrar(app):
    app.route("/", methods=["GET"])(inicial_controlador.inicial_index)

    app.route("/alunos", methods=["GET"])(alunos_controlador.alunos_index)
    app.route("/alunos", methods=["POST"])(alunos_controlador.alunos_criar)
    app.route("/alunos/<int:id>", methods=["PUT"])(alunos_controlador.alunos_atualizar)
    app.route("/alunos/<int:id>", methods=["DELETE"])(alunos_controlador.alunos_apagar)

