import unittest

import dominio.entidades.aluno as entidade


class TestAluno(unittest.TestCase):
    def test_init(self):
        aluno_dict = {
            "id": 1,
            "nome": "João",
            "matricula": "20210001"
        }
        aluno = entidade.Aluno(aluno_dict)
        self.assertEqual(aluno.id, 1)
        self.assertEqual(aluno.nome, "João")
        self.assertEqual(aluno.matricula, "20210001")

        aluno_dict = {
            "id": 2,
            "nome": "Maria"
        }
        aluno = entidade.Aluno(aluno_dict)
        self.assertEqual(aluno.id, 2)
        self.assertEqual(aluno.nome, "Maria")
        self.assertIsNone(aluno.matricula)


        aluno_dict = {
            "nome": "Maria",
            "matricula": "20210001"
        }
        aluno = entidade.Aluno(aluno_dict)
        self.assertIsNone(aluno.id)
        self.assertEqual(aluno.nome, "Maria")
        self.assertEqual(aluno.matricula, "20210001")

