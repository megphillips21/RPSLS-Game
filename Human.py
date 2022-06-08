# child class
from Player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__()
        self.age = 15
        self.name = name
        pass

    def choose_skill(self):
        for skills in self.skills_list:
            print(f'Press {self.skills_list.index(skills)+ 1} for {skills}')
        try:
            user_input = int(input(f'{self.name} Please make pick your move! '))
            self.selected_move = self.skills_list[user_input-1]
            print(f'{self.name} has made their choice! They picked {self.selected_move}!')
        except IndexError:
            print("Please select a number in the list!")
            self.choose_skill()
        
        pass

    def choose_name(self):
        self.human.name = input("Enter your name human!  ")
      