from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato
from Modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Pastelaria')
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante('planet Express', 'Pizzaria')
restaurante_pizza.receber_avaliacao('zé', 7.5)
restaurante_praca.receber_avaliacao('Bob', 4)
cafe1 = Bebida('Mocha', 7.00, 'Large')
cafe1.aplicar_desconto()
prato1 = Prato('Risoto', 10.00, 'Risoto à moda gaúcha')
prato1.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(cafe1)
restaurante_praca.adicionar_no_cardapio(prato1)
pudim = Sobremesa('Pudim', 5.00, 'Doce', 'Small', 'Receita da nikolly')
restaurante_praca.adicionar_no_cardapio(pudim)

def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()