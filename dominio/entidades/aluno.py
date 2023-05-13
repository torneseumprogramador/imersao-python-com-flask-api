class Aluno:
    def __init__(self, aluno_dict = {}):
        self.id = aluno_dict.get("id")
        self.nome = aluno_dict.get("nome")
        self.matricula = aluno_dict.get("matricula")