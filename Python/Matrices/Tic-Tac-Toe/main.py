# Last Updated: 03/10/2024
# Players now share a common board

class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
    
    def printBoard(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---|---|---")
        print("\n")

    def printBoardOptions(self):
        for i in range(0, 9, 3):
            print(f" {i+1} | {i+2} | {i+3} ")
            if i < 6:
                print("---|---|---")
        print("\n")

    def checkWinner(self, symbol):
        winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                         [0, 4, 8], [2, 4, 6]]  # Diagonals
        for condition in winConditions:
            if (self.board[condition[0]] == symbol and
                self.board[condition[1]] == symbol and
                self.board[condition[2]] == symbol):
                return True
        return False

    def isBoardFull(self):
        return ' ' not in self.board

    def gameRound(self, player1, player2):
        current_player = player1
        print("\nWelcome to Tic-Tac-Toe!")
        self.printBoardOptions()
        
        while True:
            print(f"\n{current_player.symbol}'s turn:")
            current_player.getInput(self.board)  
            self.printBoard()

            if self.checkWinner(current_player.symbol):
                print(f"Player {current_player.symbol} wins!")
                break

            if self.isBoardFull():
                print("It's a tie!")
                break

            current_player = player2 if current_player == player1 else player1




class HumanPlayer():
    def __init__(self, symbol):
        self.symbol = symbol

    def getInput(self, board):
        while True:
            try:
                choice = int(input(f"Player {self.symbol}, enter your move (1-9): ")) - 1
                if 0 <= choice <= 8 and board[choice] == ' ':
                    board[choice] = self.symbol
                    break
                else:
                    print("Invalid move, the spot is already taken or out of range. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")


######## MAIN CODE #########
humanPlayer1 = HumanPlayer("X")
humanPlayer2 = HumanPlayer("O")

game = TicTacToeGame()

game.gameRound(humanPlayer1, humanPlayer2)
