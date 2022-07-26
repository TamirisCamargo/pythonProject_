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

frutas = {
    'Banana': 1.50,
    'Manga': 2.00,
    'Goiaba': 3.00,
    'Maçã': 1.55,
    'Abacaxi': 5.00,
    'Morango': 4.00,
    'Laranja': 2.50,
    'Amora': 1.00,
    'Acerola': 3.10,
    'Kiwi': 7.00
}
print(frutas['Acerola'])

escolha_fruta = input('Digite a fruta desejada: ')
# peso = input('Digite o peso desejado: ')

if escolha_fruta in frutas:
    print(escolha_fruta)
else:
    print('Sorry, infelizmente não temos a fruta desejada')

# print(frutas['Amora'])
