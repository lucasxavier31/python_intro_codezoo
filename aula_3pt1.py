#Par ou impar

while True:

    numero = int(input('Insira um número para saber se é par ou impar: '))
    if numero%2 == 0:
        print('O número ' + str(numero) + ' é PAR!')
    else:
        print('O número ' + str(numero) + ' é ÍMPAR!')