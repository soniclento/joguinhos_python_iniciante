import random
print('estou pensando em um número inteiro de 1 a 10, será que você consegue adivinhar qual é?\n ')
from random import randint
mashine_choise = random.randint(1, 10)
n_tentativas = 0
player_choise = 0
while player_choise != mashine_choise:
    n_tentativas = n_tentativas + 1
    player_choise = int(input('digite seu plapite: '))
    if player_choise != mashine_choise:
        print(' \nnão foi dessa vez, tente novamente XD\n ')
if n_tentativas == 1:
    print(' \nnossa, você conseguiu de primeira, parabéns!!!')
else:
    print(' \nfinalmente, depois de {} tentativas você me venceu!' .format(n_tentativas))
