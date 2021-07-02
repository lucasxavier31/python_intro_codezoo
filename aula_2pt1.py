
#trabalhando com variáveis e número

nome = 'Codezoo'
print('bem-vindo(a) a calculadora da ' + nome)
nome_usuario = input('Qual seu nome? ')
#num1 = input('Digite o primeiro número para multiplicar: ')
#num2 = input('Digite o segundo número para multiplicar: ')

#mult = int(num1)*int(num2)

#print(nome_usuario.title() + ' o resultado da multiplicação é ' + str(mult))

numero = input('Digite o número que você deseja saber a TABUADA: ')

for i in range(1,11):
    multi = int(numero)*i
    print('      ' + str(numero) + ' x ' + str(i) + ' = ' + str(multi))

