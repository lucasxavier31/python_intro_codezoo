#Aula 1: conhecer o ambiente, escrever seu primeiro programa:
# (‘olá mundo’, ‘inserção de nome e idade’; Nível 2: usar o turtle)
from datetime import datetime
data_atual = datetime.now()
data_texto = data_atual.strftime('%d/%m/%Y '' %H:%M')


nome2 = input('Digite seu nome:    ')

print('Esse é o programa do Lucas Xavier')
print('\nOlá, ' + nome2 + '.')
print('\nEstá é a data de hoje: ' + data_texto)
print('Obrigado por usar o programa')