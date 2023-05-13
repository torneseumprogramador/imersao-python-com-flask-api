import unittest

from dominio.servicos.converter_para_lista_dict import \
    converter_para_lista_dict


class TestConverterParaListaDict(unittest.TestCase):
    def test_converter_para_lista_dict(self):
        class Item:
            def __init__(self, id, nome):
                self.id = id
                self.nome = nome

        # Criar uma lista de instâncias da classe Item para testar o método
        lista_de_objeto = [
            Item(1, "Item 1"),
            Item(2, "Item 2"),
            Item(3, "Item 3")
        ]

        # Chamar o método converter_para_lista_dict para obter o resultado
        lista_de_dict = converter_para_lista_dict(lista_de_objeto)

        # Verificar se o resultado está correto
        self.assertEqual(len(lista_de_dict), len(lista_de_objeto))  # Verificar se o tamanho da lista é o mesmo
        for i, item_objeto in enumerate(lista_de_objeto):
            self.assertEqual(lista_de_dict[i], item_objeto.__dict__)  # Verificar se cada item na lista é igual ao dicionário de atributos do item correspondente
