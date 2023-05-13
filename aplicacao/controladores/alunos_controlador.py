from flask import jsonify, request

import dominio.entidades.aluno as entidade
import dominio.servicos.aluno_repositorio as repo
import dominio.servicos.converter_para_lista_dict as conv
# import infraestrutura.db.memoria.db as db
# import infraestrutura.db.postgres.db as db
import infraestrutura.db.mysql.db as db


def alunos_index():
    alunos = repo.AlunoRepositorio(db).todos()
    return jsonify(conv.converter_para_lista_dict(alunos))

def alunos_criar():
    aluno = entidade.Aluno(request.get_json())
    aluno = repo.AlunoRepositorio(db).salvar(aluno)
    return jsonify(aluno.__dict__), 201

def alunos_atualizar(id):
    if not repo.AlunoRepositorio(db).existe_este_id(id):
        return jsonify({ "erro": "Aluno não existe" }), 404

    aluno_dict = request.get_json()
    aluno_dict["id"] = id
    aluno = entidade.Aluno(aluno_dict)
    aluno = repo.AlunoRepositorio(db).salvar(aluno)
    return jsonify(aluno.__dict__), 200

def alunos_apagar(id):
    if not repo.AlunoRepositorio(db).existe_este_id(id):
        return jsonify({ "erro": "Aluno não existe" }), 404

    repo.AlunoRepositorio(db).excluir_por_id(id)
    return jsonify({}), 204

