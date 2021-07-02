#FAzendo uma calculadora de IMC


print('-------------------------------------------')
print('            Calculadora de IMC')
print('-------------------------------------------')
while True:

    massa = float(input('\nInsira sua massa em kg:  '))
    altura = float(input('Insira sua altura em cm:   '))

    imc = (massa)/(altura/100)**2

    print('\nSeu indice de massa corporral é: {:.1f}'.format(imc))

    if imc < 18.4:
        print('O resultado foi:  Magreza')
    elif imc >= 18.4 and imc <= 24.9:
        print('O resultado foi:  Adequado')
    elif imc > 24.9 and imc <= 29.9:
        print('O resultado foi:  Sobrepeso')
    else:
        print('O resultado foi:  Obesidade')
