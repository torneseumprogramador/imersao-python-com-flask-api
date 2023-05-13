import dominio.entidades.aluno as entidade


class AlunoRepositorio:
    def __init__(self, db):
        self.db = db

    def todos(self):
        alunos_dic_list = self.db.executar("SELECT * FROM alunos")
        alunos = []

        for aluno_dict in alunos_dic_list:
            aluno = entidade.Aluno({
                "id": aluno_dict[0],
                "nome": aluno_dict[1],
                "matricula": aluno_dict[2]
            })

            alunos.append(aluno)

        return alunos
    
    def salvar(self, aluno):
        id_cadastrado = self.db.executar(
            "INSERT INTO alunos (nome, matricula) VALUES (%s, %s)",
            [ aluno.nome, aluno.matricula ]
        )

        aluno.id = int(id_cadastrado)
        return aluno
