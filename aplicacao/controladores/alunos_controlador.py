from flask import jsonify, request

import dominio.entidades.aluno as entidade
import dominio.servicos.aluno_repositorio as repo
import dominio.servicos.converter_para_lista_dict as conv
# import infraestrutura.db.memoria.db as db
import infraestrutura.db.mysql.db as db


def alunos_index():
    alunos = repo.AlunoRepositorio(db).todos()
    return jsonify(conv.converter_para_lista_dict(alunos))

def alunos_criar():
    print(request.get_json())

    aluno = entidade.Aluno(request.get_json())
    aluno = repo.AlunoRepositorio(db).salvar(aluno)
    return jsonify(aluno.__dict__), 201

