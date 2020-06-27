def notEdges(n=8):
    miniBoard = []

    for i in range( 3, n-1):
        for j in range(n-2, 2, -1):
            miniBoard.append(n*i-j+1)
    return sorted(miniBoard)
