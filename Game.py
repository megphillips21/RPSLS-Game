
from AI import Ai
from Human_Ai_game import Human_Ai_game
from Ai_game import Ai_game
from Human_game import Human_game

class Game:
    def __init__(self):
        print('Welcome to Rock, Paper Scissors, Lizard, Spock!')
        print("             ")
        print("Here are the rules:\n Scissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats paper\n Paper disproves Spock\n Spock vaporizes Rock\n and of course, Rock crushes Scissors!")
        self.games_list = ["Human vs. Human", "Human vs. Computer", "Computer vs. Computer"]
        for games in self.games_list:
             print(f'Press {self.games_list.index(games) +1} for {games}')
        try:
            game_type = int(input('How would you like to play? '))
            self.picked_game = self.games_list[game_type-1]
        except IndexError:
            print('Please select a number in the list!')
            Game()
       
        

    def run_game(self):
        print("Let's get ready to rumble!")
        if self.picked_game == "Human vs. Computer":
            Human_Ai_game()
        elif self.picked_game == "Computer vs. Computer":
            Ai_game()
        elif self.picked_game == "Human vs. Human":
            Human_game()
        else:
            print("Pick a actual option please!")
        
        

    