"""
Operadores Relacionais - Aula 4
== igualdade
> maior que
>= maior que ou igual que
< menor que
<= menor que ouigual que
!= diferente
"""
# num_1 = 2
# num_2 = '2'

# print(num_1 == num_2)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# Limite para pegar empréstimo
# idade_limite = 18

idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
