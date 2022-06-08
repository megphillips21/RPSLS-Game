# Parent class- similarities for both human and ai-

class Player:
    def __init__(self, name):
        self.name = name
        self.skills_list = ["Rock","Paper","Scissors","Lizard", "Spock"]
        self.selected_move = " "
        self.current_score = 0
        pass

    def choose_skill(self):
        pass

    def choose_name(self):
        pass
    
    def add_point(self):
        self.current_score += 1

    