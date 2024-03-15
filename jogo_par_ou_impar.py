print('joguinho de par ou ímpar')
from random import randint
cont = 0
player_num = 0
player_choise = ''
while True:
    mashine_num = randint(1, 5)
    while player_num <= 0 or player_num > 5:
        player_num = int(input(' \ndigite um número inteiro de 1 a 5 para jogar (qualquer número ora desse intervalo irá interromper o programa): '))
        if player_num < 0 or player_num > 5 or player_num == 0:
            print(' \nnúmeros negativos ou fora do intervalo não serão tolerados, tente novamente')
    while player_choise != 'P' and player_choise != 'I':
        player_choise = str(input(' \ndeseja jogar como par ou ímpar?\n \n[p]par\n[i]ímpar\n \n')).strip().upper()
        if player_choise != 'P' and player_choise != 'I':
            print(' \nessa resposta é inválida, tente novamente')
    game_play = mashine_num + player_num
    if player_choise == 'P':
        if game_play % 2 == 1:
            break
        else:
            print(f' \nparabéns, você me venceu! a soma das nossas jogadas foi {game_play}. vamos jogar denovo!')
            cont += 1
    else:
        if game_play % 2 == 1:
            print(f' \nparabéns, você me venceu! a soma das nossas jogadas foi {game_play}. vamos jogar denovo!')
            cont += 1
        else:
            break
    player_num = 0
    player_choise = ''
if cont == 0:
    print(' \nnossa, não foi dessa vez. Boa sorte na próxima XD')
if cont == 1:
    print(' \neu venci, mas empatamos no total. bom jogo!')
if cont > 1:
    print(f' \neu venci essa, mas você ganhou de mim no geral pois me venceu {cont} vezes seguidas. não vou facilitar da próxima vez >:(')
