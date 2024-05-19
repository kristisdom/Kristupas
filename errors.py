from abc import ABC, abstractmethod

class Errors(ABC):
    @abstractmethod
    def invalid_bet(self):
        pass
    @abstractmethod
    def invalid_guess(self):
        pass

class Errors1(Errors):
    def invalid_bet(self, coins):
        print("Insufficient balance")
        return float(input(f"Input a bet amount between 1 and {coins}: "))
    
    def invalid_guess(self):
        print("Invalid input")
        return float(input("Guess again between 1 and 10: "))
    
class Errors2(Errors):
    def invalid_bet(self, coins):
        print("Bets of max 1 decimal place are allowed")
        return float(input(f"Input a bet amount between 1 and {coins}: "))
    
    def invalid_guess(self):
        print("Invalid input")
        return input("Guess again - red, white or black: ")
