from random import randint
xy = ''
atkXY = ''
pc_valido = ''
player_valido = ''
pontuacao_player = 0
pontuacao_computador = 0
jogada = 0
posicoes_player = []
posicoes_computador = []


def tabuleiro(linha, coluna,):
    tab = []
    for i in range(linha):
        tab.append(coluna * [0])
    return tab


jogador = tabuleiro(5, 10)
computador = tabuleiro(5, 10)


for i in range(5):
    while player_valido != 'valido':
        xy = str(input(f'Digite a posição do {i+1}º do barco (x, y): '))
        if xy not in posicoes_player:
            jogador[int(xy[0])][int(xy[1])] = 1
            posicoes_player.append(xy)
            player_valido = 'valido'

    while pc_valido != 'valido':
        xy = str(randint(0, 4)) + str(randint(0, 9))
        if xy not in posicoes_computador:
            computador[int(xy[0])][int(xy[1])] = 1
            posicoes_computador.append(xy)
            pc_valido = 'valido'
    player_valido = ''
    pc_valido = ''


for c in range(5):
    print(jogador[c])
print('------------------------------------')
for d in range(5):
    print(computador[d])


while True:
    if pontuacao_player == 5 or pontuacao_computador == 5:
        break
    else:
        if jogada % 2 == 0: #player ataca
            atkXY = str(input('Digite o a posição de deseja atacar (x, y): '))
            if computador[int(atkXY[0])][int(atkXY[1])] == 1:
                print('Voce acertou!')
                pontuacao_player += 1
            else:
                print('Voce errou!')
            jogada += 1
        else: #pc ataca
            atkXY = str(randint(0, 4)) + str(randint(0, 9))
            if jogador[int(atkXY[0])][int(atkXY[1])] == 1:
                print('Computador acertou!')
                pontuacao_computador += 1
            else:
                print('Computador errou!')
            jogada += 1
