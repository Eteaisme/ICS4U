gameState = [("_")*3 for i in range(3)]

def printGameState(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print("")
def getInput(gameState):
    row, collum = map(int, input("Where do you want to move: ").split())
    print("Row: ", row)
    print("Collum: ", collum)
    choice = input("What move do you want ot make: ")
    gameState[[row][collum]] = choice
    print(gameState[0][])
    
printGameState(gameState)
getInput(gameState)
printGameState(gameState)