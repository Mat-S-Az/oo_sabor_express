from Modelos.avaliacao import Avaliacao
from Modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {self.media_avaliacao} {'|'.rjust(20)}{self.ativo}.'

    @classmethod
    def listar_restaurantes(cls):
        print(f'\n{'Nome'.ljust(25)}  {'Categoria'.ljust(26)}  {'Avaliação'.ljust(23)}  Status')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Não ativo'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 5 >= nota >= 0:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print(f'\nErro ao avaliar {self._nome}, insira uma nota de 0 a 5')

    @property
    def media_avaliacao(self):
        notas = []

        if not self._avaliacao:
            return ' - '
        
        for avaliacao in self._avaliacao:
            notas.append(avaliacao._nota)

        soma_das_notas = sum(notas)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'\nCardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i} - {item._nome} | Preço: R${item._preco} | Descricao: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i} - {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)

