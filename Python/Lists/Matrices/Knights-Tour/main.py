def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print("")

def moveKnight(board, desigeredPosition, prevPosition):
    board[prevPosition[0]][prevPosition[1]] = "_"
    board[desigeredPosition[0]][desigeredPosition[1]] = "K"



board = []
knightPosition = [0,0]
position = [2,3]
for i in range(8):
    row = []
    for j in range (8):
        row.append("_")
    board.append(row)
board[knightPosition[0]][knightPosition[1]] = "K"
printBoard(board)
moveKnight(board, position, knightPosition,)
print("\n")
printBoard(board)