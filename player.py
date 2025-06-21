import math
import random

class player:
    def __init__(self,letter):
        # letter is x or o
        self.letter = letter

    # we want all the players get their next move 
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
       square = random.choice(game. available_moves())
       return square

class HumanPlayer(player):
    def  __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid
            # if that spot is not available on the board, we also say it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True              #if these successfuly then yes
            except ValueError:
                print("Invalid saquare, please try again!!")


        return val