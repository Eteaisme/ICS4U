#Last updated: E. Tam 27-09-2024
import random


class Player: 
    def __init__(self):
        self.state = [0,0,0]        
        self.winner = False

    def roll(self): 
        roll_value = random.randint(1, 6)
        if(roll_value < 2):
            self.state[2] = 0 
        else: 
            self.state[2] += roll_value
    def bank(self):
        self.state[0] += self.state[2]
        self.state[2] = 0 

    def game_round(self, Player2):
        game_state = []
        player1_turn = True
        game_turn = 1 
        while ((self.winner or Player2.winner) != True):
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

            if(game_state[0] >= 100):
                self.winner = True
                print("Player 1 Wins! Final score of :",game_state[0]," vs ",game_state[1])
            elif(game_state[1] >= 100):
                Player2.winner = True
                print("Player 2 Wins! Final score of :",game_state[1]," vs ",game_state[0])

            else:
                print(game_state)


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
class Computer_Player_Random(Player):
    def __init__(self): 
        super().__init__()  
    def get_input(self):
        choice = random.randint(0, 1)
        if(choice == 1):
            self.roll()
        else:
            self.bank()

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



human_player1 = Human_Player()
human_player2 = Human_Player()
random_computer_player = Computer_Player_Random() 
hold_25_computer_player = Computer_Player_Hold_25()
hold_20_computer_player = Computer_Player_Hold_20()

human_player1.game_round(hold_25_computer_player)