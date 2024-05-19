from answers import *
from errors import *
from multiply import *
from text import *

class Game:
    def __init__(self, balance):
        self.coins = balance
        self.answers = Answers()
        self.errors1 = Errors1()
        self.errors2 = Errors2()
        self.multiply = Multiply()
        self.txt = Text()
        
    def intro(func):
        def wrap(*args, **kwargs):
            print("Welcome to the casino!")
            func(*args, **kwargs)
            print("Good luck!\n")
        return wrap
            
    @intro
    def rules(self):
        print("The rules are very simple")
        print("You get coins for guessing the right numbers from 1 to 10")
        print("or a color red, white or black")
        

    def start(self):
        self.txt.file_delete()
        a = input("To start press 1: ")
        coins = self.coins
        
        while a == "1" and coins > 0:
            print(f"You have {coins} coins")
            x = self.answers.random(1)
            z = self.answers.random(2)
            bet_amount = float(input("Input bet amount: "))

            while coins < bet_amount or bet_amount <= 0:
                bet_amount = self.errors1.invalid_bet(coins)
            
            while (bet_amount * 10) % 1 != 0:
                bet_amount = self.errors2.invalid_bet(coins)

            guess_num = float(input("Guess a number between 1 and 10: "))
            
            while not (1 <= guess_num <= 10 and guess_num == int(guess_num)):
                guess_num = self.errors1.invalid_guess()

            guess_color = input("Guess a color - red, white or black: ")
            
            while guess_color not in ["red", "white", "black"]:
                guess_color = self.errors2.invalid_guess()

            coins -= bet_amount
            print("Bet in progress...")

            answer_color = self.answers.color_assign(guess_color)

            self.answers.answer_reveal(x, z)
            
            coins = self.multiply.multiplier(coins, bet_amount, guess_num, answer_color, x, z)
            
            self.txt.file_write(bet_amount, guess_num, guess_color, x, z)

        if a != "1":
            print("fair enough")
        else:
            print("you lost...")
