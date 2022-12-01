import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter #letter is x or o
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # gets random valid spot for next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # checks that this is correct value by trying to cast to an integer
            # if not, say it's invalid
            # if spot if not available on board, also say it's invalid
            try:
                val = int(square) 
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if successful
            except ValueError:
                print('Invalid square. Try again.')

        return val  