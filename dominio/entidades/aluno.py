class Aluno:
    def __init__(self, aluno_dict = {}):
        self.id = aluno_dict["id"]
        self.nome = aluno_dict["nome"]
        self.matricula = aluno_dict["matricula"]