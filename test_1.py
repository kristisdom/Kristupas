import unittest
from game import *

class test_game(unittest.TestCase):
    
    def set_up(self):
        self.balance = 100 #mock balance
        self.game = Game(self.balance)
        self.mock_variables()

    def mock_variables(self):
        self.x = 1 #mock answer num
        self.z = 1 #mock answer color
        self.x_guess = 1 #mock guess num
        self.z_guess = "red" #mock guess color
         
    def test_color_assign(self):
        y = self.game.answers.color_assign(self.z_guess)
        self.assertEqual(y, self.z)
    
    def test_rev_color_assign(self):
        y = self.game.answers.color_assign(self.z_guess)
        c = self.game.answers2.color_assign(y)
        self.assertEqual(c, self.z)    
        

if __name__ == '__main__':
    unittest.main()
