from AI import Ai
from Human import Human

class Game:
    def __init__(self):
        self.human = Human(input("Enter your name!  "))
        self.ai = Ai(input("Computer would like to know what you call computer. Computer no have name like humans. Thank you, from Computer  "))

    def run_game(self):
        print("Let's get ready to rumble!")
        self.pick_first_skill()
        self.determine_winner
        pass

    def pick_first_skill(self):
        self.human.selected_move = self.human.choose_skill()
        self.ai.selected_move = self.ai.choose_skill()

        if self.human.selected_move == "Rock" and self.ai.selected_move == "Rock":
            print("It's a tie, pick again")
            self.pick_first_skill()
        elif self.human.selected_move == "Paper" and self.ai.selected_move == "Paper":
            print("It's a tie, pick again")
            self.pick_first_skill()
        elif self.human.selected_move == "Scissors" and self.ai.selected_move == "Scissors":
            print("It's a tie, pick again")
            self.pick_first_skill()
        elif self.human.selected_move == "Lizard" and self.ai.selected_move == "Lizard":
            print("It's a tie, pick again")
            self.pick_first_skill()
        elif self.human.selected_move == "Spock" and self.ai.selected_move == "Spock":
            print("It's a tie, pick again")
            self.pick_first_skill()

        
    def determine_winner(self ):
        pass
    def game_round(self):
        pass