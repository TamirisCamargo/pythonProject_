"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""
# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6
#
# var = func(1,2,3,4,5, nome='Luiz', a6='5')
# print(var)

def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)


    # print(kwargs)
    # for v in args:
    #     print(v)

    # print(args)
    # print(args[0])
    # print(args[-1])
    # print(len(args))

# lista = [1,2,3,4,5]
# print(*lista, sep='-')
# func(1,2,3,4,5)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Tami', sobrenome='Camargo', idade=30)
