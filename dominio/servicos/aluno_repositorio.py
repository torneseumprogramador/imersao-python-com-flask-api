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
    
    def existe_este_id(self, id):
        alunos_dic_list = self.db.executar("SELECT id FROM alunos where id = %s", [id])
        return len(alunos_dic_list) > 0
    
    def excluir_por_id(self, id):
        self.db.executar("delete from alunos where id = %s", [id])
    
    def salvar(self, aluno):
        if aluno.id == 0 or aluno.id == None:
            id_cadastrado = self.db.executar(
                "INSERT INTO alunos (nome, matricula) VALUES (%s, %s)",
                [ aluno.nome, aluno.matricula ]
            )

            aluno.id = int(id_cadastrado)
            return aluno
        else:
            self.db.executar(
                "UPDATE alunos set nome=%s, matricula=%s where id=%s",
                [ aluno.nome, aluno.matricula, aluno.id ]
            )

            return aluno
