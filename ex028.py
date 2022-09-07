import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
sort = random.randint(0, 5)
if num == sort:
    print('Parabéns você acertou!! número escolhido foi {}'.format(num))
else:
    print('Que pena, você errou, mas quem sabe na próxima!!')
    print('O número que pensei foi {}!!'.format(sort))