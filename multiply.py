class Multiply:
    def multiplier(self, coins, bet_amount, guess_num, answer_color, x, z):       
        self.coins = coins
        self.bet_amount = bet_amount
        if x == guess_num and z == answer_color:
            print("You won 15x coins!!")
            return self.apply_multiply(15)
        elif z == answer_color:
            print("You won 3x coins!")
            return self.apply_multiply(3)
        elif x == guess_num:
            print("You won 10x coins!")
            return self.apply_multiply(10)
        else:
            print("You did not guess right :(")
            return coins   
      
    def apply_multiply(self, mult):
        return (((self.coins + self.bet_amount * mult) * 10) // 1) / 10
