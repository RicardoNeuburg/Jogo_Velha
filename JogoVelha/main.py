import os
from graphic import drawGraphic
from condition import gameRules
from condition import playTurn


player = 1
playername = [input('Digite o nome do primeiro jogador: ')], [input('Digite o nome do segundo jogador: ')]
os.system('cls')


while True:
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    supportList = [0, 0, 0]
    turns = 0
    replay = ""
    win = 0
    while True:
        win = gameRules(matriz)
        drawGraphic(matriz)
        if win == 1:
            if player == -1:
                print(f'{playername[0]} venceu!')
            else:
                print(f'{playername[1]} venceu!')
            break
        supportList = playTurn(player, matriz, playername)
        matriz[supportList[0]][supportList[1]] = supportList[2]
        if turns < 8:
            turns += 1
            if player == 1:
                player = -1
            else:
                player = 1
        else:
            print('Empate')
            break
        os.system('cls')
    replay = input('Jogar novamente?\n[S] Sim\n[N] Não\n').upper()
    if replay == "S":
        player = -1
    elif replay == "N":
        break
    os.system('cls')
