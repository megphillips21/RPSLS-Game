from AI import Ai
from Human import Human

class Game:
    def __init__(self):
        self.human = Human(input("Enter your name!  "))
        self.ai = Ai(input("Computer would like to know what you call computer. Computer no have name like humans. Thank you, from Computer  "))

    def run_game(self):
        print("Let's get ready to rumble!")
        self.pick_first_skill()
        pass

    def pick_first_skill(self):
        self.human.choose_skill()
        self.ai.choose_skill()