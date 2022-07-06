"""
Funções - def em Python (Parte 1)
"""
def funcao(msg):
    print(msg)
funcao('Mensagem')
funcao("Hello")
funcao('Tchau')
funcao('Eu posso escrever o que eu quiser aqui.')

def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao(nome='Zezinho', msg="Hi")
saudacao('Hello', 'Léo')

def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)