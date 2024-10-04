#Last Updated: 03/10/2024
#Working on checkWinner() method

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.winnner = False
        self.board = ["" for _ in range(9)]
    

    def checkWinner(self):
        winConditions = [[0,1,2],
                         [3,4,5],
                         [6,7,8],
                         [0,3,6],
                         [1,4,7],
                         [2,5,8],
                         [0,4,8],
                         [2,4,6]]
        for i in range(len(winConditions)):
            if((self.board[winConditions[i][0]] == self.symbol) and 
            (self.board[winConditions[i][1]] == self.symbol) and
            (self.board[winConditions[i][2]] == self.symbol)):
                self.winnner = True


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

    def gameRound(self):
        print("\nWelcome to Tic-Tac-Toe!")
        self.printBoardOptions() 
        while(self.winnner == False):
            print(self.winnner)
            self.getInput()
            self.printBoard()
            self.checkWinner()
            






class HumanPlayer(Player):
    def __init__(self, symbol):
        self.symbol = symbol
        self.winnner = False
        self.board = [' ' for _ in range(9)]
    
    def getInput(self):
        verified = False
        
        while(verified == False):
            choice = int(input("Enter your choice [1-9]: "))
            if((choice >=1)and(choice <=9)):
                verified = "True"
            else:
                print("\nPlease input a valid number. [1-9]")
                self.printBoardOptions()
        self.board[choice - 1] = self.symbol

humanPlayer = HumanPlayer("X")
humanPlayer.gameRound()