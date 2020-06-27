def buildBoard(n=8):
    # nxn board
    # n = 8
    board = []

    # i, ascending (1, n)
    for i in range(1 , n+1):
        # j, descending [n, 0]
        for j in range(n - 1, -1, -1):
            # any square can be expressed as n*i-j
            board.append(n*i-j)
    # board is now indexed, 1 to n.
    # 0 to n-1 index
    return board