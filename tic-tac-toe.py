from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import math
import time

class TicTacToe:
    def __init__(self):
        self.board = self.make_board() # 3x3 board
        self.current_winner = None # keeps track of winner
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        # Indexes into length 9 list 
        # i in range(3)
        # [i*3:(i+1) * 3] = chooses group of 3 spaces representing rows
            # ex) i = 0 --> [0:3] --> numbers in 2st row, i = 1 --> [3:6] --> numbers in 2nd row
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]: 
            print('| ' + ' | '.join(row) + ' |') # .join means to join as string where sep is

    @staticmethod # don't have to pass in self, prints numbers corresponding to spots
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1) * 3)] for j in range(3)] # have range start at 1 so squares can be numbered 1-9?
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if valid move, make move (assigns square to letter)
        # then return True; If invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere
        # check row
        row_ind = math.floor(square // 3)
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True
        
        # check diagonals
        # only if square is even number(0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True 
        
        # if all checks fail then return False bc no winner
        return False 

    def empty_squares(self):
        return ' ' in self.board 

    def num_empty_squares(self):
        return self.board.count(' ')
    
    def available_moves(self):
        # if x is ' ' return i in that ' ', then returns list
        return [i for i, x in enumerate(self.board) if x == " "] # written as a list comprehension instead
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

def play(game, x_player, o_player, print_game=True):
    # returns the letter of the winner, or None for a tie
    if print_game:
        game.print_board_nums() # shows which numbers correspond to which spots 

    letter = 'X' # starting letter
    # iterate while there's still empty squares
    # don't worry about winner because it'll return when loop breaks
    while game.empty_squares():
        # gets move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') # just empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after move is made, alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches players 
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
        
        # time.sleep(.8) # creates a tiny break/delay

    if print_game:
        print('It\'s a tie!')

# if __name__ == '__main__':
#     x_player = HumanPlayer('X')
#     o_player = GeniusComputerPlayer('O') 
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game=True)

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O') 
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After 100 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties.')