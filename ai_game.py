from AI import Ai

class Ai_game:
    def __init__(self):
        self.ai_one = Ai()
        self.ai_two = Ai()
        self.game = self.ai_vs_ai()
        pass

    def ai_vs_ai_moves(self):
        self.ai_one.choose_skill()
        self.ai_two.choose_skill()
        if self.ai_one.selected_move == "Rock" and self.ai_two.selected_move == "Rock":
            print("That's a tie, new moves please!")
            self.ai_vs_ai()
        elif self.ai_one.selected_move == "Paper" and self.ai_two.selected_move == "Paper":
            print("That's a tie, new moves please!")
            self.ai_vs_ai()
        elif self.ai_one.selected_move == "Scissors" and self.ai_two.selected_move == "Scissors":
            print("That's a tie, new moves please!")
            self.ai_vs_ai()
        elif self.ai_one.selected_move == "Lizard" and self.ai_two.selected_move == "Lizard":
            print("That's a tie, new moves please!")
            self.ai_vs_ai()
        elif self.ai_one.selected_move == "Spock" and self.ai_two.selected_move == "Spock":
            print("That's a tie, new moves please!")
            self.ai_vs_ai()

        elif self.ai_one.selected_move == "Rock" and self.ai_two.selected_move == "Scissors" or self.ai_two.selected_move == "Lizard":
            print(f"{self.ai_one.selected_move} beats {self.ai_two.selected_move}! Point for {self.ai_one.name}")
            self.ai_one.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
        
        elif self.ai_one.selected_move =="Rock" and self.ai_two.selected_move == "Paper" or self.ai_two.selected_move == "Spock":
            print(f"{self.ai_one.selected_move} loses to {self.ai_two.selected_move}! Point for {self.ai_two.name}")
            self.ai_two.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
        
        elif self.ai_one.selected_move == "Paper" and self.ai_two.selected_move == "Rock" or self.ai_two.selected_move == "Spock":
            print(f"{self.ai_one.selected_move} beats {self.ai_two.selected_move}! Point for {self.ai_one.name}")
            self.ai_one.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')

        # AI one = paper AI 2 = Scissor or Lizard. Point AI
        elif self.ai_one.selected_move == "Paper" and self.ai_two.selected_move == "Scissors" or self.ai_two.selected_move == "Lizard":
            print(f"{self.ai_one.selected_move} loses to {self.ai_two.selected_move}! Point for {self.ai_two.name}")
            self.ai_two.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')

        # AI one = Scissors AI 2 = paper or lizard. point.ai_one
        elif self.ai_one.selected_move == "Scissors" and self.ai_two.selected_move == "Paper" or self.ai_two.selected_move == "Lizard":
            print(f"{self.ai_one.selected_move} beats {self.ai_two.selected_move}! Point for {self.ai_one.name}")
            self.ai_one.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
       
        # AI one = Scissors AI= rock or spock point AI
        elif self.ai_one.selected_move == "Scissors" and self.ai_two.selected_move == "Rock" or self.ai_two.selected_move == "Spock":
            print(f"{self.ai_one.selected_move} loses to {self.ai_two.selected_move}! Point for {self.ai_two.name}")
            self.ai_two.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
     
        # AI one = Lizard AI = paper or spock. Point AI one
        elif self.ai_one.selected_move == "Lizard" and self.ai_two.selected_move == "Paper" or self.ai_two.selected_move == "Spock":
            print(f"{self.ai_one.selected_move} beats {self.ai_two.selected_move}! Point for {self.ai_one.name}")
            self.ai_one.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
        # AI one = Lizard AI = rock or scissors point AI
        elif self.ai_one.selected_move == "Lizard" and self.ai_two.selected_move == "Rock" or self.ai_two.selected_move == "Scissors":
            print(f"{self.ai_one.selected_move} loses to {self.ai_two.selected_move}! Point for {self.ai_two.name}")
            self.ai_two.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
        # AI one = Spock AI = rock or scissors, point AI one
        elif self.ai_one.selected_move == "Spock" and self.ai_two.selected_move == "Rock" or self.ai_two.selected_move == "Scissors":
            print(f"{self.ai_one.selected_move} beats {self.ai_two.selected_move}! Point for {self.ai_one.name}")
            self.ai_one.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
        #  AI one = Spock AI = lizard or paper, point AI
        elif self.ai_one.selected_move == "Spock" and self.ai_two.selected_move == "Lizard" or self.ai_two.selected_move == "Paper":
            print(f"{self.ai_one.selected_move} loses to {self.ai_two.selected_move}! Point for {self.ai_two.name}")
            self.ai_two.add_point()
            print(f'Current Score: AI Player One = {self.ai_one.current_score}')
            print(f'Current Score: AI Player Two = {self.ai_two.current_score}')
    
    def ai_vs_ai(self):
        while self.ai_one.current_score < 2 and self.ai_two.current_score < 2:
            self.ai_vs_ai_moves()
        if self.ai_one.current_score == 2:
            print(f'We have a winner!! AI Player One wins!!')
        elif self.ai_two.current_score == 2:
            print(f'We have a winner!! AI Player Two wins!!')
        pass
