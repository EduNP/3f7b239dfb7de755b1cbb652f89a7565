from models import Estoque_Produto, Estoque_Negativo, Anuncio_Produto, Tabela_Integracao


def adicionar_produto(nome, qnt):
    r = Estoque_Produto()