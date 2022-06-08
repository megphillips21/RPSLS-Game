from AI import Ai

class Ai_game:
    def __init__(self):
        self.ai_one = Ai()
        self.ai_two = Ai()
        pass

    def ai_vs_ai(self):
        self.ai_one.choose_skill()
        self.ai_two.choose_skill()
        pass