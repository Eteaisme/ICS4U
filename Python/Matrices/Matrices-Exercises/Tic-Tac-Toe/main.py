#Last Updated: 03/10/2024

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.winnner = False
        self.board = [' ' for _ in range(9)]
    

    def checkWinner(self, board):
        winConditions = [(0,1,2), (3,4,5), (6,7,8), # Rows
                            (0,3,6), (1,4,7), (2,5,8), # Columns
                            (0,4,8), (2,4,6)] # Diagonals
        for condition in winConditions:
            if board[condition[0]]== self.symbol:
                self.winnner = True

    def printBoard(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---|---|---")
        print("\n")    

humanPlayer = Player("X")
humanPlayer.board[0] = humanPlayer.symbol
humanPlayer.board[1] = humanPlayer.symbol
humanPlayer.board[2] = humanPlayer.symbol
humanPlayer.printBoard()
humanPlayer.checkWinner(humanPlayer.board)
print(humanPlayer.winnner)
