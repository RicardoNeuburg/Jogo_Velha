def gameRules(anyList):
    localSum1 = [0, 0] # [0] Diagonal Primaria [1] Diagonal Secundaria
    for i in range(len(anyList)):
        localSum2 = [0, 0] # [0] Horizontal [1] Vertical
        for j in range(len(anyList)):
            localSum2[0] += anyList[i][j]
            localSum2[1] += anyList[j][i]
            if i == j: # anyList[i] == anyList[j]
                localSum1[0] += anyList[i][j]
            if j == 2:
                localSum1[1] += anyList[i][len(anyList) - 1 - i]
            if localSum1[0] == 3 or localSum1[1] == 3 or localSum2[0] == 3 or localSum2[1] == 3:
                return 1
            elif localSum1[0] == -3 or localSum1[1] == -3 or localSum2[0] == -3 or localSum2[1] == -3:
                return 1

def playTurn(whoPlay, anyList, playername):
    play = [0, 0, 0] # [0] linha [1] coluna [2] simbolo do jogador
    if whoPlay == 1: name = playername[0]
    else: name = playername[1]
    while True:
        print(f'{name}, seu turno: ')
        play[0] = int(input('Escolha a linha de 1 à 3: ')) - 1
        play[1] = int(input('Escolha a coluna de 1 à 3: ')) - 1
        if anyList[play[0]][play[1]] == 0:
            play[2] = whoPlay
            return play
        else:
            print('Posição já ocupada, tente novamente.')
