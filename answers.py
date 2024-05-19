from random import randint 

class Answers:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def random(self, var):
        if var == 1:
            return randint(1, 10)
        else:
            return randint(1, 3)
        
    def color_assign(self, guess_color):
        if guess_color == "red":
            return 1
        elif guess_color == "white":
            return 2
        else:
            return 3
        
    def rev_color_assign(self, z):
        if z == 1:
            return "red"
        elif z == 2:
            return "white"
        else:
            return "black"
        
    def answer_reveal(self, x, z):
        if z == 1:
            print(f"The answer is {x} and red")
        elif z == 2:
            print(f"The answer is {x} and white")
        else:
            print(f"The answer is {x} and black")
