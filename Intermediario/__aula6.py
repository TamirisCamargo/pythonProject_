# def funcao(arg, arg2):
#     return arg * arg2
#
# var = funcao(2,2)
# print(var)

# a = lambda x, y: x * y
#
# print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# def func(item):
#     return item[1]

# lista.sort(key=lambda item: item[1])
# print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)