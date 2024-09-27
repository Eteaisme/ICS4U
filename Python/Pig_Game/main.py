#Last updated: E. Tam 27-09-2024
import random


######## MAIN CLASS DEFINITION #################################
class Player: 
    ######## FUNCTION DEFINITIONS #################################
    def __init__(self):
    #Constructor creating an array to hold the current state of the game
        # [Game score, Opponent score, Round score] as well as a winner variable 
        self.state = [0,0,0]        
        self.winner = False

    def roll(self): 
    #Get a random number [1-6] and set the objects state accordingly 
    #Parameters: self
        roll_value = random.randint(1, 6)
        if(roll_value < 2):
            self.state[2] = 0 
        else: 
            self.state[2] += roll_value
    def bank(self):
    #Set the objects bank score to it's current round score and then
        #reset the round score 
    #Parameters: self
        self.state[0] += self.state[2]
        self.state[2] = 0 
    ######## MAIN GAME FUNCTION#################################
    #Function that allows the object to play against another agent
    #Parameters: Self Player2/Other agent
    def game_round(self, Player2):
        #Create variables to keep track of the state of the game
        game_state = []
        player1_turn = True
        game_turn = 1 
        #Loop until either the object or the other agent has won
        while ((self.winner or Player2.winner) != True):
            #Check who's turn it is and then get that objects input
                # and update the game_state array accordingly 
            if player1_turn == True:
                self.get_input()
                game_state = [(self.state[0]),(Player2.state[0]),(self.state[2])]
                if game_state[2] == 0:
                    player1_turn = False
            else:
                Player2.get_input()
                game_state = [(self.state[0]),(Player2.state[0]),(Player2.state[2])]
                if game_state[2] == 0:
                    player1_turn = True
            game_turn += 1 
            #Check if either the object or the other agents game score is
                #greater than or equal to 100 and if they are print the winner 
            if(game_state[0] >= 100):
                self.winner = True
                print("Player 1 Wins! Final score of :",game_state[0]," vs ",game_state[1])
            elif(game_state[1] >= 100):
                Player2.winner = True
                print("Player 2 Wins! Final score of :",game_state[1]," vs ",game_state[0])

            else:
                print(game_state)

######## CHILD CLASS DEFINITIONS #################################
class Human_Player(Player): 
    def __init__(self): 
        #Inherit values from parent class constructor 
        #Parameters: self
        super().__init__()  
    def get_input(self):
        #Get input from the terminal(human player)
        #Parameters: self
        choice = input("Roll or Bank? [R/B]: ")
        #Check the input and roll or bank based off of the input if the 
            #input is not valid prompt the user to try again
        if(choice == "R"):
            self.roll()
        elif (choice == "B"):
            self.bank()
        else:
            print("Please Input a valid choice")
class Computer_Player_Random(Player):
    def __init__(self): 
        #Inherit values from parent class constructor 
        #Parameters: self
        super().__init__()  
    def get_input(self):
        #Get a random input [0-1] and roll/bank based off the result
        #Parameters: self
        choice = random.randint(0, 1)
        if(choice == 1):
            self.roll()
        else:
            self.bank()

class Computer_Player_Hold_20(Player):
    def __init__(self): 
        #Inherit values from parent class constructor 
        #Parameters: self
        super().__init__()  
    def get_input(self):
        #Check if the objects current round score is less than 20 and
            #roll if it is
        #Parameters: self
        if((self.state[2] < 20) and (not((self.state[2]+self.state[0]) == 100))):
            self.roll()
        else:
            self.bank()

class Computer_Player_Hold_25(Player):
    def __init__(self): 
        #Inherit values from parent class constructor 
        #Parameters: self
        super().__init__()  
    def get_input(self):
        #Check if the objects current round score is less than 25 and
            #roll if it is
        #Parameters: self
        if((self.state[2] < 25) and (not((self.state[2]+self.state[0]) == 100))):
            self.roll()
        else:
            self.bank()


######## OBJECT DECLARATIONS #################################
human_player1 = Human_Player()
human_player2 = Human_Player()
random_computer_player = Computer_Player_Random() 
hold_25_computer_player = Computer_Player_Hold_25()
hold_20_computer_player = Computer_Player_Hold_20()

######## MAIN CODE #################################
human_player1.game_round(hold_25_computer_player)