"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d -Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# print(divisao)
# print('{:.2f}'.format(divisao))  # (f'{divisao:.2f}')

nome = 'Luiz Otávio'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')  # (f'{num_2:0^10}')

nome = 'Otávio Miranda'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
# print((50-len(nome)))
# print(f'{nome:#^50}')


