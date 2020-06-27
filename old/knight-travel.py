import random
from buildBoard import buildBoard
from validMove import validMove
from selectMove import selectMove
from boardEdges import boardEdges
from innerEdges import innerEdges
from notEdges import notEdges




startingPosition = 3
# board size nxn
n = 8

# board as a list, 1 to n
board = buildBoard(n)
# edges of the board
edges = list(set(board).difference(set(notEdges(n))))


# list of valid moves

def moveKnight(startingPosition, board):


    moves = validMove(n, startingPosition)

    # randomly select a valid move
    selectedMove = moves[selectMove(moves)]
    if selectedMove not in edges and selectedMove in board:
        board.pop(selectedMove - 1)
        print('selected', selectedMove)
        print('board list', board)
        return (moveKnight(selectedMove, board))
    print('Ended on', selectedMove)
    print('final board list', board)


# moveKnight(startingPosition, board)

for startingPosition in board:
    print(startingPosition, validMove(n, startingPosition))
#
