from Human import Human

class Human_game:
    def __init__(self):
        self.player_one = Human(input("Enter name for Player One! "))
        self.player_two = Human(input('Enter name for Player Two! '))

    def human_vs_human_moves(self):
        self.player_one.choose_skill()
        self.player_two.choose_skill()

        if self.player_one.selected_move == "Rock" and self.player_two.selected_move == "Rock":
            print("That's a tie, new moves please!")
            self.human_vs_human_moves()
        elif self.player_one.selected_move == "Paper" and self.player_two.selected_move == "Paper":
            print("That's a tie, new moves please!")
            self.human_vs_human_moves()
        elif self.player_one.selected_move == "Scissors" and self.player_two.selected_move == "Scissors":
            print("That's a tie, new moves please!")
            self.human_vs_human_moves()
        elif self.player_one.selected_move == "Lizard" and self.player_two.selected_move == "Lizard":
            print("That's a tie, new moves please!")
            self.human_vs_human_moves()
        elif self.player_one.selected_move == "Spock" and self.player_two.selected_move == "Spock":
            print("That's a tie, new moves please!")
            self.human_vs_human_moves()

        elif self.player_one.selected_move == "Rock" and self.player_two.selected_move == "Scissors" or self.player_two.selected_move == "Lizard":
            print(f"{self.player_one.selected_move} beats {self.player_two.selected_move}! Point for {self.player_one.name}")
            self.player_one.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')
        
        elif self.player_one.selected_move =="Rock" and self.player_two.selected_move == "Paper" or self.player_two.selected_move == "Spock":
            print(f"{self.player_one.selected_move} loses to {self.player_two.selected_move}! Point for {self.player_two.name}")
            self.player_two.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')

        elif self.player_one.selected_move == "Paper" and self.player_two.selected_move == "Rock" or self.player_two.selected_move == "Spock":
            print(f"{self.player_one.selected_move} beats {self.player_two.selected_move}! Point for {self.player_one.name}")
            self.player_one.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')

        # AI one = paper AI 2 = Scissor or Lizard. Point AI
        elif self.player_one.selected_move == "Paper" and self.player_two.selected_move == "Scissors" or self.player_two.selected_move == "Lizard":
            print(f"{self.player_one.selected_move} loses to {self.player_two.selected_move}! Point for {self.player_two.name}")
            self.player_two.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')

        # AI one = Scissors AI 2 = paper or lizard. poinf.player_one
        elif self.player_one.selected_move == "Scissors" and self.player_two.selected_move == "Paper" or self.player_two.selected_move == "Lizard":
            print(f"{self.player_one.selected_move} beats {self.player_two.selected_move}! Point for {self.player_one.name}")
            self.player_one.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')
       
        # AI one = Scissors AI= rock or spock point AI
        elif self.player_one.selected_move == "Scissors" and self.player_two.selected_move == "Rock" or self.player_two.selected_move == "Spock":
            print(f"{self.player_one.selected_move} loses to {self.player_two.selected_move}! Point for {self.player_two.name}")
            self.player_two.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')
     
        # AI one = Lizard AI = paper or spock. Point AI one
        elif self.player_one.selected_move == "Lizard" and self.player_two.selected_move == "Paper" or self.player_two.selected_move == "Spock":
            print(f"{self.player_one.selected_move} beats {self.player_two.selected_move}! Point for {self.player_one.name}")
            self.player_one.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')
        # AI one = Lizard AI = rock or scissors point AI
        elif self.player_one.selected_move == "Lizard" and self.player_two.selected_move == "Rock" or self.player_two.selected_move == "Scissors":
            print(f"{self.player_one.selected_move} loses to {self.player_two.selected_move}! Point for {self.player_two.name}")
            self.player_two.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')
        # AI one = Spock AI = rock or scissors, point AI one
        elif self.player_one.selected_move == "Spock" and self.player_two.selected_move == "Rock" or self.player_two.selected_move == "Scissors":
            print(f"{self.player_one.selected_move} beats {self.player_two.selected_move}! Point for {self.player_one.name}")
            self.player_one.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')
        #  AI one = Spock AI = lizard or paper, point AI
        elif self.player_one.selected_move == "Spock" and self.player_two.selected_move == "Lizard" or self.player_two.selected_move == "Paper":
            print(f"{self.player_one.selected_move} loses to {self.player_two.selected_move}! Point for {self.player_two.name}")
            self.player_two.add_point()
            print(f'Current Score: {self.player_one.name} = {self.player_one.current_score}')
            print(f'Current Score: {self.player_two.name} = {self.player_two.current_score}')

    def human_vs_human(self):
        while self.player_one.current_score < 2 and self.player_two.current_score < 2:
            self.ai_vs_ai_moves()
        if self.player_one.current_score == 2:
            print(f'We have a winner!! {self.player_one.name} wins!!')
        elif self.player_two.current_score == 2:
            print(f'We have a winner!! {self.player_two.name} wins!!')
        pass