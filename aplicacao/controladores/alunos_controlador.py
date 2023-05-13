from flask import jsonify

import dominio.servicos.aluno_repositorio as repo
import dominio.servicos.converter_para_lista_dict as conv
import infraestrutura.db.memoria.db as db


def alunos_index():
    alunos = repo.AlunoRepositorio(db).todos()
    return jsonify(conv.converter_para_lista_dict(alunos))
