print('=-' * 30)
print('VAMOS JOGAR PEDAR, PAPEL OU TESOURA')
print('=-' * 30, '\n ')
print('digite RK para escolher pedra (rock)\ndigite PP para escolher papel (paper)\ndigite SR para escolher tesoura (scissor)\n ')
import random
mashine_choise = random.randint(1, 3)
if mashine_choise == 1:
    mashine_play = 'pedra'
else:
    if mashine_choise == 2:
        mashine_play = 'papel'
    else:
        mashine_play = 'tesoura'
player_choise = str(input('')).strip().upper()
print(' ')
print('eu joguei {}' .format(mashine_play), '\n ')
if player_choise == 'RK':
    if mashine_play == 'pedra':
        print(' que pena, EMPATAMOS!')
    else:
        if mashine_play == 'tesoura':
            print('parabéns, VOCÊ ME VENCEU!')
        else:
            print('eba, EU VENCI!')
else:
    if player_choise == 'PP':
        if mashine_play == 'pedra':
            print('parabéns, VOCÊ ME VENCEU!')
        else:
            if mashine_play == 'papel':
                print('que pena, EMPATAMOS!')
            else:
                print('eba, EU VENCI!')
    else:
        if player_choise == 'SR':
            if mashine_play == 'pedra':
                print('eba, EU VENCI!')
            else:
                if mashine_play == 'papel':
                    print('parabéns, VOCÊ ME VENCEU!')
                else:
                    print('que pena, EMPATAMOS!')
        else:
            print('lamento, mas essa opção é inválida. tente novamente')
