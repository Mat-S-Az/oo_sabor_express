from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Pastelaria')
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante('planet Express', 'Pizzaria')
restaurante_pizza.receber_avaliacao('zé', 7.5)
restaurante_praca.receber_avaliacao('Bob', 4)
cafe1 = Bebida('Mocha', 7.00, 'Large')
prato1 = Prato('Risoto', 10.00, 'Risoto à moda gaúcha')
restaurante_praca.adicionar_bebida_no_cardapio(cafe1)
restaurante_praca.adicionar_prato_no_cardapio(prato1)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()