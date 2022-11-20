from random import randint
xy = ''
atkXY = ''
pc_valido = ''
player_valido = ''
pontuacao_player = 5
pontuacao_computador = 5
jogada = 0
posicoes_player = []
posicoes_computador = []


def tabuleiro(linha, coluna,):
    tab = []
    for i in range(linha):
        tab.append(coluna * [0])
    return tab

def mostrartabj():
    print("\nTabuleiro do Jogador")
    for c in range(5):
        print(jogador[c])


def mostrartabc():
    print("\nTabuleiro do Computador")
    for d in range(5):
        print(ocultoComputador[d])
    print('------------------------------------')


jogador = tabuleiro(5, 10)
computador = tabuleiro(5, 10)
ocultoComputador = tabuleiro(5, 10)


for i in range(5):
    while player_valido != 'valido':
        xy = str(input(f'Digite a posição do {i}º do barco, para x de 0 à 4, para y de 0 à 9 (x, y): '))
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

mostrartabc()
mostrartabj()


while True:
    if pontuacao_player == 0 or pontuacao_computador == 0:
        break
    else:
        if jogada % 2 == 0: #player ataca
            atkXY = str(input('Digite o a posição de deseja atacar, para x de 0 à 4, para y de 0 à 9(x, y): '))
            if computador[int(atkXY[0])][int(atkXY[1])] == 1:
                ocultoComputador[int(atkXY[0])][int(atkXY[1])] = 'x'
                pontuacao_computador -= 1
                print('Voce acertou!')
                mostrartabc()
                print("Embarcações Restantes",pontuacao_player)
                mostrartabj()
                print("Embarcações Restantes",pontuacao_computador)

            else:
                print('Voce errou!')
            jogada += 1
        else: #pc ataca
            atkXY = str(randint(0, 4)) + str(randint(0, 9))
            if jogador[int(atkXY[0])][int(atkXY[1])] == 1:
                jogador[int(atkXY[0])][int(atkXY[1])] = 'x'
                pontuacao_player -= 1
                print('Computador acertou!')
                mostrartabc()
                print("Embarcações Restantes", pontuacao_player)
                mostrartabj()
                print("Embarcações Restantes", pontuacao_computador)
            else:
                print('Computador errou!')
            jogada += 1

if pontuacao_player == 0:
    print("Parabéns, você afundou todas as embarcações do inimigo")
else:
    print("Você perdeu, o Computador derrubou todas as suas embarcações")
print("Jogo desenvolvido por Stuart Correa, Nicolas Lamback e Caroline Sales")
