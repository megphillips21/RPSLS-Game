# child class
from Player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.age = 15
        pass

    def choose_skill(self):
        for skills in self.skills_list:
            print(f'Press {self.skills_list.index(skills)+ 1} for {skills}')
        
        user_input = int(input(f'{self.name} please make pick your first move! '))
        self.selected_move = self.skills_list[user_input-1]
        print(f'{self.name} has made their choice! They picked {self.selected_move}!')
        
        pass