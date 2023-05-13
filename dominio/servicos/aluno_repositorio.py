import dominio.entidades.aluno as entidade


class AlunoRepositorio:
    def __init__(self, db):
        self.db = db

    def todos(self):
        alunos_dic_list = self.db.execute("SELECT * FROM alunos")
        alunos = []

        for aluno_dict in alunos_dic_list:
            aluno = entidade.Aluno(aluno_dict)

            alunos.append(aluno)

        return alunos
