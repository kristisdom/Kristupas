from game import *

txt_r = Text()
balance = txt_r.file_read()
game = Game(balance)
game.rules()
game.start()

