
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
        game_type = int(input('How would you like to play? '))
        self.picked_game = self.games_list[game_type-1]
       
        

    def run_game(self):
        print("Let's get ready to rumble!")
        if self.picked_game == "Human vs. Computer":
            Human_Ai_game()
        elif self.picked_game == "Computer vs. Computer":
            Ai_game()
        elif self.picked_game == "Human vs. Human":
            Human_game()
        
        pass

    # def ai_human_moves(self):
    #     self.human.choose_skill()
    #     self.ai.choose_skill()
    #     # determine a tie
    #     if self.human.selected_move == "Rock" and self.ai.selected_move == "Rock":
    #         print("It's a tie, pick again")
    #         self.ai_human_moves()
    #     elif self.human.selected_move == "Paper" and self.ai.selected_move == "Paper":
    #         print("It's a tie, pick again")
    #         self.ai_human_moves()
    #     elif self.human.selected_move == "Scissors" and self.ai.selected_move == "Scissors":
    #         print("It's a tie, pick again")
    #         self.ai_human_moves()
    #     elif self.human.selected_move == "Lizard" and self.ai.selected_move == "Lizard":
    #         print("It's a tie, pick again")
    #         self.ai_human_moves()
    #     elif self.human.selected_move == "Spock" and self.ai.selected_move == "Spock":
    #         print("It's a tie, pick again")
    #         self.ai_human_moves()

    #     # determine points for human player
    #     # Human = Rock and AI picks Scissors or Lizard point Human
    #     elif self.human.selected_move == "Rock" and self.ai.selected_move == "Scissors" or self.ai.selected_move == "Lizard":
    #         print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
    #         self.human.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

    #     # Human = Rock and AI picks paper or spock, point AI
    #     elif self.human.selected_move =="Rock" and self.ai.selected_move == "Paper" or self.ai.selected_move == "Spock":
    #         print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
    #         self.ai.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}') 

    #     # Human = paper and AI picks rock or spock point Human
    #     elif self.human.selected_move == "Paper" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Spock":
    #         print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
    #         self.human.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

    #     # Human = paper AI = Scissor or Lizard. Point AI
    #     elif self.human.selected_move == "Paper" and self.ai.selected_move == "Scissors" or self.ai.selected_move == "Lizard":
    #         print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
    #         self.ai.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

    #     # Human = Scissors AI = paper or lizard. point human
    #     elif self.human.selected_move == "Scissors" and self.ai.selected_move == "Paper" or self.ai.selected_move == "Lizard":
    #         print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
    #         self.human.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
    #     # Human = Scissors AI= rock or spock point AI
    #     elif self.human.selected_move == "Scissors" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Spock":
    #         print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
    #         self.ai.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
    #     # Human = Lizard AI = paper or spock. Point Human
    #     elif self.human.selected_move == "Lizard" and self.ai.selected_move == "Paper" or self.ai.selected_move == "Spock":
    #         print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
    #         self.human.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
    #     # Human = Lizard AI = rock or scissors point AI
    #     elif self.human.selected_move == "Lizard" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Scissors":
    #         print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
    #         self.ai.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
    #     # Human = Spock AI = rock or scissors, point Human
    #     elif self.human.selected_move == "Spock" and self.ai.selected_move == "Rock" or self.ai.selected_move == "Scissors":
    #         print(f"{self.human.selected_move} beats {self.ai.selected_move}! Point for {self.human.name}")
    #         self.human.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')
    #     #Human = Spock AI = lizard or paper, point AI
    #     elif self.human.selected_move == "Spock" and self.ai.selected_move == "Lizard" or self.ai.selected_move == "Paper":
    #         print(f"{self.human.selected_move} loses to {self.ai.selected_move}! Point for {self.ai.name}")
    #         self.ai.add_point()
    #         print(f'Current Score:{self.human.name} = {self.human.current_score}')
    #         print(f'Current Score:{self.ai.name} = {self.ai.current_score}')

    # def ai_vs_human(self):
    #     while self.human.current_score < 2 and self.ai.current_score < 2:
    #         self.ai_human_moves()
    #     if self.human.current_score == 2:
    #         print(f'We have a winner!! {self.human.name} wins!!')
    #     elif self.ai.current_score == 2:
    #         print(f'We have a winner!! {self.ai.name} wins!!')
    #     pass
    