from answers import *

class Text:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.answers2 = Answers()

    def file_read(self):
        with open('balance.txt', 'r') as text_balance:
            balance = int(text_balance.read())
        return balance
    
    def file_write(self, bet_amount, guess_num, guess_color, x, z):
        with open('betlog.txt', 'a') as bet_log:
            bet_log.write(f"Stake: {bet_amount}\n")
            bet_log.write(f"Bet on: {int(guess_num)} {guess_color}\n")
            bet_log.write(f"Answers: {x} {self.answers2.rev_color_assign(z)}\n")
            bet_log.write("\n")
            
    def file_delete(self):
        with open('betlog.txt', 'w') as bet_log:
            bet_log.write("")
