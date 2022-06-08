#child class
from Player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.age = 150
        self.name = "Beepy"
        pass

    def choose_skill(self):
        self.selected_move = random.choice(self.skills_list)
        print(f'{self.name} chose {self.selected_move} as their move!')
        pass

    
    # def choose_name(self):
    #     ai_name = input('Computer would like to know what you call computer. Computer no have name like humans. Thank you, from Computer ')
