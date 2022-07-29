"""
Desenvolver uma lista de frutas com 10 frutas diferentes e cada fruta possui um preço por kg.

Ex: 'Banana' : 1.50, 'Manga': 2.00..... (cadastrar 10 frutas)

A função irá receber 2 parâmetros. Nome da fruta e a quantidade em kg (se for em gramas precisa ser no seguinte
formato 0.500 g.) Passar somente o valor do kilo e não o kg ou g.

Verificar se o nome da fruta existe na lista, se existir calcular o valor final pelo peso informado. ex: Banana 10
será 10* 1.50 = 15 reais. Se não existir retornar que a fruta informada não está disponível para venda. Se tiver a
fruta fazer o calculo e retornar uma string amigável informando o valor final da fruta.

Obs: use a função input() python para receber os parametros.
ex: fruta = input('Qual fruta deseja comprar? ')
"""

frutas: dict[str, float] = {
    'Banana': 1.50,
    'Banana': 3.00,
    'Manga': 2.00,
    'Goiaba': 3.00,
    'Maçã': 1.55,
    'Abacaxi': 5.00,
    'Morango': 4.00,
    'Laranja': 2.50,
    'amora': 1.00,
    'Acerola': 3.10,
    'Kiwi': 7.00,
    'frutas-citricaas' : ['Banana': 1.2]
}

while True:
    escolha_fruta = input('Digite a FRUTA desejada: ')
    escolha_fruta = escolha_fruta.title()
    if escolha_fruta in frutas.keys():

        try:
            peso = input('Digite o PESO desejado: ')
            soma = float(peso) * float(frutas[escolha_fruta])
            print(f'Obrigada, o valor total da fruta {escolha_fruta} é R$ {soma}')
        except Exception as erro:
            print(f'Por favor, informar o peso em formato númerico')

    else:
        print(f'Sorry, infelizmente não temos a fruta desejada. \n'
              f'Segue nossa lista de frutas disponíveis {frutas}')


