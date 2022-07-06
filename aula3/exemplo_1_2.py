"""
Operadores Lógicos = Aula 4
and, or, not
in e not in
"""

#  (Verdadeiro E Verdadeiro) = Verdadeiro
#  (Verdadeiro E False = Falso
#  comparacao1 and comparacao2

# Verdadeiro OU Verdadeiro
# Qualquer uma das duas expressões que ser Verdadeira, vai retornar Verdadeiro.
#  comp1 OR comp2

a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

nome = 'Luiz Otávio.'

if 'vio' not in nome:
    print('Existe.')
else:
    print("Não existe.")

# verificar senha

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = "luiz"
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')





