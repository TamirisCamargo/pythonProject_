"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""

print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print('25.23', type('25.23'))
print('l' == 'L', type('l' == 'L'))
print('', type(''))
print(bool(''))
print(bool(0))

print('luiz', type('luiz'), bool('luiz'))

# String: nome
print('Tamiris Camargo', type('Tamiris Camargo'))

# Idade: int
print(32, type(32))

# Altura: float
print(1.62, type(1.62))

# É maior de idade
print(32 > 18, type(32 > 18))

