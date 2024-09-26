"""
Import random library which we can use to 
generate values for simulated dice rolls
"""
import random


"""
When desiging this program I wanted to create a parent class 
with common methods and varibles that could be overiden.
The goal was to have a "template" for a pig player and then
inhearent & change the template.

For example:
The player class holds common varibles like the state of the game
and wheather the player has one or not. It also holds methods like roll & bank.
The Human_Player class inhearents these methods and chooses to call them based off of
human input.

Also notitce how this class and all follwing classes  created do not follow the
naming convention used for varibles (lorem_ipsum) but instead are capitalized.
This is because it's best practice to capitalze your class names to distinguish them instances
of said class.
"""
class Player: 



    """
This constructor is called whenever a instance of
the Player class is created. It creates an array to 
store the game state as well as a boolean win varible
The state varible is an array that holds the follwing values at each of
its index's

    [0] --> The objects game score
    [1] --> An opponets game score
    [2] --> The objects round score

"""
    def __init__(self):
        self.state = [0,0,0]        
        self.winner = False

    """
The roll method passes in an instance of the player class and updates
said instance's state based on the result of the rolll. 
In acorandce to the rules if the player rolls a one their round 
score gets set to zero, otherwise add the roll to their round score.
"""
    def roll(self): 
        roll_value = random.randint(1, 6)
        if(roll_value < 2):
            self.state[2] = 0 
        else: 
            self.state[2] += roll_value

    """
The bank method transfers the current round score to the
objects game score (self.state[0]). It then sets the round score
to zero. 
"""
    def bank(self):
        self.state[0] += self.state[2]
        self.state[2] = 0 

    """
The most complicated method in this class is the game round function.
The goal of this method is to take in another Player object and "play a game of pig" with 
the other agent. 

To start off we first need to pass in the other player as a paramiter.
After that we need to define some varibles that are important for keeping track of the game.

    game_state[] --> Similar to self.state this varible takes both of the states both objects
                     and creates one central game state array. 

    player1_turn --> This is a boolean varible used to keep track of turns, when True it is 
                     Player1s turn (The Player object) and when False it is the opponents turn

    game_turn    --> This is a varible that keeps track of the total turns in the game, it gets
                     incremented by one every round. 
"""
    def game_round(self, Player2):
        game_state = []
        player1_turn = True
        game_turn = 1 

    """
    This is the main loop of the game, we loop through this until etither the player object or the 
    oppenent has won. 
"""
        while ((self.winner or Player2.winner) != True):

    """
    These 2 conditonals check whos turn it is, and gets the input of
    whosever turn it is. After getting the input we set the game state
    to the its new values. 

    Another important thing to note is that if either of the players 
    round score is == 0 that means 1 of two things;

    1. The player decided to roll and got a 1
    2. The player decided to bank

    Either of these results end the players turn so by checking the current 
    round score after an input we can find out if that players turn should end 
    and act accordingly. 

"""
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
    """
    Increment the game turn by one
"""
            game_turn += 1 

    """
    Check if either of the players gamescore is greater or equal to 100.
    If they are, set the winner varible to true (In turn breaking out of the loop)
    and print a message describing who won as well as the final scores
"""
            if(game_state[0] >= 100):
                self.winner = True
                print("Player 1 Wins! Final score of :",game_state[0]," vs ",game_state[1])
            elif(game_state[1] >= 100):
                Player2.winner = True
                print("Player 2 Wins! Final score of :",game_state[1]," vs ",game_state[0])

    """
    If neither player has won print the current state of the game and
    return to the top of the loop. 
"""
            else:
                print(game_state)

    """
    This is where inheartince comes in. Here we create a new class called Human_Player.
    Human player's inputs are based off of terminal inputs. So when an instance of this
    class is passed into the game_round method, when we ask for its inputs we prompt
    the user in the terminal. 

    If the user chooses "R" we call the roll function,
    if the user chooses "B" we call the bank function.

    Any other input is rejected and the user will be asked to 
    input a valid responce. 
"""

class Human_Player(Player): 
    def __init__(self): 
        super().__init__()  
    def get_input(self):
        choice = input("Roll or Bank? [R/B]: ")
        if(choice == "R"):
            self.roll()
        elif (choice == "B"):
            self.bank()
        else:
            print("Please Input a valid choice")

     """
     This class's inputs are completly random, 
     its has a 50/50 chance of either banking or rolling. 
     When it's get input method is called it gets a random number 
     from the random class and determines its result based on 
     whether the nubmer returned is a 1 or a zero. 
"""
class Computer_Player_Random(Player):
    def __init__(self): 
        super().__init__()  
    def get_input(self):
        choice = random.randint(0, 1)
        if(choice == 1):
            self.roll()
        else:
            self.bank()

    """
    These next two classes countinuesly will roll
    unless certain conditions are met. 

    1. Roll until the round score is either 20/25

    2. If the round score + the bank score is enough to win the game
       then bank. 

"""
class Computer_Player_Hold_20(Player):
    def __init__(self): 
        super().__init__()  
    def get_input(self):
        if((self.state[2] < 20) and (not((self.state[2]+self.state[0]) == 100))):
            self.roll()
        else:
            self.bank()

class Computer_Player_Hold_25(Player):
    def __init__(self): 
        super().__init__()  
    def get_input(self):
        if((self.state[2] < 25) and (not((self.state[2]+self.state[0]) == 100))):
            self.roll()
        else:
            self.bank()



    """
    Here we create instances of each of our child classes, this allows
    the user to pick and choose who they want to play as or against. 
"""
human_player1 = Human_Player()
human_player2 = Human_Player()
random_computer_player = Computer_Player_Random() 
hold_25_computer_player = Computer_Player_Hold_25()
hold_20_computer_player = Computer_Player_Hold_20()

    """
    Here we call the game_round() function and choose to play
    against the hold_25_computer_player object. 
"""
human_player1.game_round(hold_25_computer_player)