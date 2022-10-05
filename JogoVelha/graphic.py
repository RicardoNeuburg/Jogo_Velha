def drawGraphic(anyList):
    for i in range(len(anyList)):
        for j in range(len(anyList)):
            if anyList[i][j] == 1:
                symbol = " X "
            elif anyList[i][j] == -1:
                symbol = " O "
            else:
                symbol = "   "
            if j == 0 or j == 1:
                print(symbol, end='|')
            else:
                print(symbol, end='')
        print()
        if i != 2:
            print('-----------')