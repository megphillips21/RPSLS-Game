from AI import Ai
from Human import Human

class Game:
    def __init__(self):
        self.human = Human(input("Enter your name!  "))
        self.ai = Ai(input("Computer would like to know what you call computer. Computer no have name like humans. Thank you, from Computer  "))

    def run_game(self):
        print("Let's get ready to rumble!")
        self.pick_first_skill()
        self.determine_winner()
        pass

    def pick_first_skill(self):
        self.human.choose_skill()
        self.ai.choose_skill()
        # determine a tie
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

        # determine points for human player
        # Human = Rock and AI picks Scissors or Lizard point Human
        elif self.human.selected_move == "Rock" and self.ai.selected_move == "Scissors" or self.ai.selected_move == "Lizard":
            print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
            self.player.human.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

        # Human = Rock and AI picks paper or spock, point AI
        elif self.human.selected_move == "Rock" and self.ai.selected_move == "Paper" or self.ai.selected_move == "Spock":
            print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
            self.ai.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}') 

        # Human = paper and AI picks rock or spock point Human
        elif self.human.selected_move == "Paper" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Spock":
            print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
            self.human.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

        # Human = paper AI = Scissor or Lizard. Point AI
        elif self.human.selected_move == "Paper" and self.ai.selected_move == "Scissors" or self.ai.selected_move == "Lizard":
            print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
            self.ai.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

        # Human = Scissors AI = paper or lizard. point human
        elif self.human.selected_move == "Scissors" and self.ai.selected_move == "Paper" or self.ai.selected_move == "Lizard":
            print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
            self.human.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
        # Human = Scissors AI= rock or spock point AI
        elif self.human.selected_move == "Scissors" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Spock":
            print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
            self.ai.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
        # Human = Lizard AI = paper or spock. Point Human
        elif self.human.selected_move == "Lizard" and self.ai.selected_move == "Paper" or self.ai.selected_move == "Spock":
            print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
            self.human.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
        # Human = Lizard AI = rock or scissors point AI
        elif self.human.selected_move == "Lizard" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Scissors":
            print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
            self.ai.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
        # Human = Spock AI = rock or scissors, point Human
        elif self.human.selected_move == "Spock" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Scissors":
            print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
            self.human.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
        #Human = Spock AI = lizard or paper, point AI
        elif self.human.selected_move == "Spock" and self.ai.selected_move == "Lizard" or self.ai.selected_move == "Paper":
            print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
            self.ai.add_point()
            print(f'Current Score:{self.human.name} = {self.human.current_score}')
            print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

    def determine_winner(self ):
        pass
    def game_round(self):
        pass