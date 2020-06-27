def validMove(n=8, m=1):
    # for nxn board
    # valid moves for position m
    rawMoves = [
        m - 2 * n - 1,
        m - 2 * n + 1,
        m - n - 2,
        m - n + 2,
        m + n - 2,
        m + n + 2,
        m + 2 * n - 1,
        m + 2 * n + 1,
    ]


    return [item for item in rawMoves if item >0 and item <= 64]