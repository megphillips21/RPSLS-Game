#child class
from Player import Player

class AI(Player):
    def __init__(self):
        super().__init__('Beep-Boop')
        self.age = 150
        pass

    def choose_skill(self):
        print('Computer has made their choice')