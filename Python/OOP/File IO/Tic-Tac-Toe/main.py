
# Last Updated: E. Tam 31/10/2024
import os 
import random
import datetime
from pyfiglet import figlet_format
################# MAIN GAME CLASS DEFINITION #############################
class TicTacToeGame:
    def __init__(self):
        # Initialize an empty 3x3 board 
        self.board = [' ' for _ in range(9)]  

################# MAIN GAME FUNCTIONS DEFINITION #########################
    def resetBoards(self, other):
        # Reset both boards to empty 3x3 grids
        self.board = [' ' for _ in range(9)]
        other.board = [' ' for _ in range(9)]        
    def printBoard(self):
        # Print the current state of the board
        os.system('clear')
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---|---|---")
        print("\n")

    def printBoardOptions(self):
        # Print the board with the possible options a player could take 
        for i in range(0, 9, 3):
            print(f" {i+1} | {i+2} | {i+3} ")
            if i < 6:
                print("---|---|---")
        print("\n")

    def checkWinner(self, symbol):
        # Define the possible win conditions 
        winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                         [0, 4, 8], [2, 4, 6]]  # Diagonals
        # Check if a board has met any of the win conditions
        for condition in winConditions:
            if (self.board[condition[0]] == symbol and
                self.board[condition[1]] == symbol and
                self.board[condition[2]] == symbol):
                return True  
        return False  

    def isBoardFull(self):
        # Check if the board is full 
        return ' ' not in self.board

    def writeToHallOfFame(self, message):
        hallOfFame = open("/home/Elliot/School/ICS4U/Python/OOP/File IO/Tic-Tac-Toe/hallOfFame.txt", "a")
        print(figlet_format(message, font = "small"), file=hallOfFame)
        hallOfFame.close()


    def gameRound(self, player1, player2):
        self.resetBoards(player2)
        currentPlayer = player1  
        # Print starting information
        self.printBoardOptions()  

        # Loop until either the board is full or one of the players has met a win condition
        while True:
            print(f"\n{currentPlayer.symbol}'s turn:")  
            currentPlayer.getInput(self.board)  
            self.printBoard()  

            if self.checkWinner(currentPlayer.symbol):
                print(f"Player {currentPlayer.symbol} wins!")  
                if(currentPlayer.playerType == "Human"): 
                    username = input("Enter your name into the Tic-Tac-Toe Hall of Fame: ")
                    self.writeToHallOfFame(username)
                else: 
                    input()
                break 

            if self.isBoardFull():
                print("It's a tie!")  
                input()
                break   

            # Switch turns
            currentPlayer = player2 if currentPlayer == player1 else player1
            




################### CHILD CLASS DEFINITIONS #############################
class RandomComputerPlayer():
    def __init__(self, symbol):
        self.symbol = symbol 
    def getInput(self, board):
        while True: 
            choice = random.randint(0, 8)
            if 0 <= choice <= 8 and board[choice] == ' ':
                board[choice] = self.symbol
                break  


################### HUMAN PLAYER #############################
class HumanPlayer():
    playerType = "Human"
    def __init__(self, symbol):
        # When a HumanPlayer object is created pass in a symbol value
        self.symbol = symbol

    def getInput(self, board):
        while True:
            # Get input from the player and check if the input is valid
            try:
                choice = int(input(f"Player {self.symbol}, enter your move (1-9): ")) - 1
                if 0 <= choice <= 8 and board[choice] == ' ':
                    board[choice] = self.symbol
                    break  
                else:
                    print("Invalid move, the spot is already taken or out of range. Try again.")
            except ValueError:
                print("Please enter a valid integer between 1 and 9.")


################### AI PLAYER #############################
class MiniMaxAI:
    playerType = "Computer"
    def __init__(self,symbol):
        self.symbol = symbol
        self.opponentSymbol = "O" if symbol == "X" else "X"
    def getInput(self, board):
        bestMove = self.minimax(board, self.symbol)["position"]
        if bestMove is not None:
            board[bestMove] = self.symbol
        else:
            raise ValueError("No valid moves")

    def minimax(self, board, currentPlayer):
        #Base cases return dictonary 
        if self.checkWinner(board, self.opponentSymbol):
            return {"position": None, "score": -1}  
        elif self.checkWinner(board, self.symbol):
            return {"position": None, "score": 1}   
        elif self.isBoardFull(board):
            return {"position": None, "score": 0}   

        if currentPlayer == self.symbol:
            best = {"position": None, "score": -float("inf")}  # Maximize score
        else:
            best = {"position": None, "score": float("inf")}   # Minimize score

        for i in range(9):
            if board[i] == " ":
                # Make the move
                board[i] = currentPlayer 
                # Call minimax recursively to simulate the game after the move
                simScore = self.minimax(board, self.opponentSymbol if currentPlayer == self.symbol else self.symbol)
                # Undo the move
                board[i] = ' '
                # Update best move
                simScore['position'] = i

                #Maximizing
                if currentPlayer == self.symbol:
                    if simScore ["score"] > best["score"]:
                        best = simScore
                #Minimizing
                else:
                    if simScore["score"] < best["score"]:
                        best = simScore

        return best

    def checkWinner(self, board, symbol):
        # Check all winning conditions on the current board for the given symbol
        winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                          [0, 4, 8], [2, 4, 6]]  # Diagonals
        for condition in winConditions:
            if (board[condition[0]] == symbol and
                board[condition[1]] == symbol and
                board[condition[2]] == symbol):
                return True
        return False

    def isBoardFull(self, board):
        # Check if the board is full
        return ' ' not in board


######## MAIN CODE #########


######## HALL OF FAME #########


######## OBJECT DECLORATIONS #########
humanPlayer1 = HumanPlayer("X")
humanPlayer2 = HumanPlayer("O")

minMaxAIPlayer1 = MiniMaxAI("X")
minaMaxAIPlayer2 = MiniMaxAI("O")

randomComputerPlayer1 = RandomComputerPlayer("X")
randomComputerPlayer2 = RandomComputerPlayer("O")

game = TicTacToeGame()







######## Wrapper #########
while True:
    os.system('clear')
    print("""
     _______ _          _______             _______         
    |__   __(_)        |__   __|           |__   __|        
        | |   _  ___ ______| | __ _  ___ ______| | ___   ___ 
        | |  | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \\
        | |  | | (__       | | (_| | (__       | | (_) |  __/
        |_|  |_|\___|      |_|\__,_|\___|      |_|\___/ \___|
    """)
    print("""
     _     ___ _           _       ___ _                   
    / |   / __(_)_ _  __ _| |___  | _ \ |__ _ _  _ ___ _ _ 
    | |_  \__ \ | ' \/ _` | / -_) |  _/ / _` | || / -_) '_|
    |_(_) |___/_|_||_\__, |_\___| |_| |_\__,_|\_, \___|_|  
                    |___/                    |__/         
    """)
    print()
    print("""
    ___     __  __      _ _   _      _                   
   |_  )   |  \/  |_  _| | |_(_)_ __| |__ _ _  _ ___ _ _ 
    / / _  | |\/| | || | |  _| | '_ \ / _` | || / -_) '_|
   /___(_) |_|  |_|\_,_|_|\__|_| .__/_\__,_|\_, \___|_|  
                                |_|          |__/         
    """)
    print()
    print("""
     ____    _  _      _ _        __   ___                        _.+._
    |__ /   | || |__ _| | |  ___ / _| | __|_ _ _ __  ___        (^\/^\/^)
     |_ \_  | __ / _` | | | / _ \  _| | _/ _` | '  \/ -_)        \@*@*@/
    |___(_) |_||_\__,_|_|_| \___/_|   |_|\__,_|_|_|_\___|        {_____}
    """)
    print()
    print("""
     _ _         ___     _ _   
    | | |       | __|_ _(_) |_   
    |_  _|      | _|\ \ / |  _|
      |_(_)     |___/_\_\_|\__|
    """)
    #Game mode input
    gameChoice = input("")








######## SINGLE PLAYER #########
    if(gameChoice == "1"):
        os.system('clear')
        while True:
            os.system("clear")
            print()
            print("""
     _     ___              
    / |   | __|__ _ ____  _ 
    | |_  | _|/ _` (_-< || |
    |_(_) |___\__,_/__/\_, |
                        |__/ 
            """)
            print()
            print("""
     ___     _  _             _ 
    |_  )   | || |__ _ _ _ __| |
     / / _  | __ / _` | '_/ _` |
    /___(_) |_||_\__,_|_| \__,_|
            """)
            print()
            print("""
     ____    ___     _ _   
    |__ /   | __|_ _(_) |_ 
     |_ \_  | _|\ \ / |  _|
    |___(_) |___/_\_\_|\__|
            """)
            difficultyChoice = input("")
            if(difficultyChoice == "1"):
                os.system("clear")
                game.gameRound(humanPlayer1, randomComputerPlayer2)
            if(difficultyChoice == "2"):
                os.system('clear')
                game.gameRound(humanPlayer1, minaMaxAIPlayer2)
                input()
            if(difficultyChoice == "3"):
                os.system("clear")
                break








######## MULTIPLAYER #########
    elif(gameChoice == "2"):
        while True: 
            os.system("clear")
            print("""
         _     _____                ___ _                   
        / |   |_   _|_ __ _____ ___| _ \ |__ _ _  _ ___ _ _ 
        | |_    | | \ V  V / _ \___|  _/ / _` | || / -_) '_|
        |_(_)   |_|  \_/\_/\___/   |_| |_\__,_|\_, \___|_|  
                                            |__/         
            """)
            print()
            print("""
         ___     ___     _ _   
        |_  )   | __|_ _(_) |_ 
         / / _  | _|\ \ / |  _|
        /___(_) |___/_\_\_|\__|
            """)
            difficultyChoice = input("")
            if(difficultyChoice == "1"):
                os.system("clear")
                game.gameRound(humanPlayer1, humanPlayer2)
            if(difficultyChoice == "2"):
                os.system('clear')
                break















######## HALL OF FAME#########
    elif(gameChoice == "3"):
        while True:
            hallOfFame = open("/home/Elliot/School/ICS4U/Python/OOP/File IO/Tic-Tac-Toe/hallOfFame.txt", "r")
            os.system("clear")
            print("""
                     _  _      _ _        __   ___                        _.+._
                    | || |__ _| | |  ___ / _| | __|_ _ _ __  ___        (^\/^\/^)
                    | __ / _` | | | / _ \  _| | _/ _` | '  \/ -_)        \@*@*@/
                    |_||_\__,_|_|_| \___/_|   |_|\__,_|_|_|_\___|        {_____}
    """)
            print()
            print(hallOfFame.read())


            print("""
 ___     ___     _ _   
|_  )   | __|_ _(_) |_ 
 / / _  | _|\ \ / |  _|
/___(_) |___/_\_\_|\__|
            """)
            difficultyChoice = input("")
            if(difficultyChoice == "2"):
                os.system('clear')
                hallOfFame.close()
                break



    elif(gameChoice == "4"):
        os.system("clear")
        break
        
    else:
        print()