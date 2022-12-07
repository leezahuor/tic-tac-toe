import math
import random

# This is the base player class. Other classes will inherit from this. 
class Player:
    def __init__(self, letter):
        self.letter = letter #letter is x or o
    
    def get_move(self, game):
        pass

# allows input for human player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square: # (while valid_square is False)
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # checks that this is correct value by trying to cast to an integer
            # if not, say it's invalid
            # if spot if not available on board, also say it's invalid
            try:
                val = int(square) 
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if prev conditions are successful
            except ValueError: # catches ValueError, repeats loop to get valid square
                print('Invalid square. Try again.')
        return val # returns val once a valid square is given

# allows computer's turn
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # initialize superclass

    def get_move(self, game):
        # gets random valid spot for next move
        square = random.choice(game.available_moves())
        return square

class GeniusComputerPlayer(Player):
    # uses minimax algorithm to be unbeatable 
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9: # if all spaces are available, grabs random spot
            square = random.choice(game.available_moves()) # randomly chooses spot
        else:
            # gets square based off minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square 
    
    def minimax(self, state, player):
        # state passes in 'screenshots' or 'states' of game
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # other player takes other available letter

        # check if prev move is winner --> base case
        if state.current_winner == other_player:
            # should return position and score to keep track of score
            # for minimax to work
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
                
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
        
        # initialize some dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize
        
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move 
            
            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else: 
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best 
