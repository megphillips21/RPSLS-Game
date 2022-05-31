# child class
from Player import Player

class Human(Player):
    def __init__(self):
        super().__init__('JJ')
        self.age = 15
        pass

    def choose_skill(self):
        print('Human has made their choice')