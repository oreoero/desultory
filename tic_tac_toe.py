# https://www.neverstopbuilding.com/blog/2013/12/13/tic-tac-toe-understanding-the-minimax-algorithm13/
import sys
from copy import deepcopy


class Board(object):
    def __init__(self):
        self.grid = []
        for i in range(3):
            self.grid.append(['', '', ''])

    def move(self, mark, row, column):
        row = int(row)
        column = int(column)
        if not self.check_input(row, column):
            return

        self.grid[row][column] = mark

        return

    def available_moves(self):
        available_moves = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if not self.is_occupied(i, j):
                    available_moves.append([i, j])

        return available_moves

    def check_winner(self):
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == 'x' or \
           self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == 'x' or \
           self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == 'x' or \
           self.grid[0][0] == self.grid[1][0] == self.grid[2][0] == 'x' or \
           self.grid[0][1] == self.grid[1][1] == self.grid[2][1] == 'x' or \
           self.grid[0][2] == self.grid[1][2] == self.grid[2][2] == 'x' or \
           self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == 'x' or \
           self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == 'x':
            return 'x'
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == 'o' or \
           self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == 'o' or \
           self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == 'o' or \
           self.grid[0][0] == self.grid[1][0] == self.grid[2][0] == 'o' or \
           self.grid[0][1] == self.grid[1][1] == self.grid[2][1] == 'o' or \
           self.grid[0][2] == self.grid[1][2] == self.grid[2][2] == 'o' or \
           self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == 'o' or \
           self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == 'o':
            return 'o'
        return None

    def check_input(self, row, column):
        if row < 0 or row > len(self.grid) - 1 or \
           column < 0 or column > len(self.grid) - 1:
            raise Exception("Invalid operation")

        if self.is_occupied(row, column):
            raise Exception("This location is already occupied: row - " + str(row) + "; column - " + str(column))
        return True

    def is_occupied(self, row, column):
        return self.grid[row][column] != ''

    def print(self):
        for row in self.grid:
            print(row)


class Player(object):
    def __init__(self, name, mark, opponent_mark):
        self.name = name
        self.mark = mark
        self.opponent_mark = opponent_mark

    def move(self, board, row, column):
        board.move(self.mark, row, column)


class ComputerPlayer(Player):
    def __init__(self, mark, opponent_mark):
        super(ComputerPlayer, self).__init__('Computer', mark, opponent_mark)


class HumanPlayer(Player):
    def __init__(self, mark, opponent_mark):
        super(HumanPlayer, self).__init__('Human', mark, opponent_mark)


class AI(object):
    MAX_SCORE_VALUE = 10
    MIN_SCORE_VALUE = -10
    DRAW_SCORE_VALUE = 0

    def __init__(self):
        self.suggested_move = ()

    def score(self, board, player, depth):
        if board.check_winner() == player.mark:
            return self.MAX_SCORE_VALUE - depth
        elif board.check_winner() is not None:
            return self.MIN_SCORE_VALUE + depth
        return self.DRAW_SCORE_VALUE

    def run_minimax_algo(self, board, player, is_player_turn, depth):
        if board.check_winner() is not None:
            return self.score(board, player, depth)

        possible_outcomes = {}

        for move in board.available_moves():
            row, column = move[0], move[1]
            board_copy = deepcopy(board)
            board_copy.move(player.mark if is_player_turn else player.opponent_mark, row, column)
            score = self.run_minimax_algo(board_copy, player, not is_player_turn, depth + 1)

            possible_outcomes[(row, column)] = score

        if is_player_turn:
            largest_score = - sys.maxsize
            for move in possible_outcomes.keys():
                if possible_outcomes[move] > largest_score:
                    largest_score = possible_outcomes[move]
                    self.suggested_move = move
            return largest_score
        else:
            smallest_score = sys.maxsize
            for move in possible_outcomes.keys():
                if possible_outcomes[move] < smallest_score:
                    smallest_score = possible_outcomes[move]
                    self.suggested_move = move
            return smallest_score


class GameController(object):
    def __init__(self):
        self.board = Board()
        self.computer_player = ComputerPlayer('x', 'o')
        self.human_player = HumanPlayer('o', 'x')
        self.ai = AI()

    def start_game(self):
        while not self.board.check_winner():
            self.board.print()
            valid_user_input = self.get_valid_user_input()
            row = valid_user_input[0]
            column = valid_user_input[1]
            self.human_player.move(self.board, row, column)

            self.ai.run_minimax_algo(self.board, self.computer_player, True, 0)
            print(self.ai.suggested_move)
            suggested_row_move = self.ai.suggested_move[0]
            suggested_column_move = self.ai.suggested_move[1]
            self.computer_player.move(self.board, suggested_row_move, suggested_column_move)

        winner_mark = self.board.check_winner()
        if winner_mark == self.computer_player.mark:
            print("Computer player wins!")
        elif winner_mark == self.human_player.mark:
            print("Human player wins!")
        else:
            print("It's a tie.")

    def get_valid_user_input(self):
        while True:
            row = int(input("row?"))
            column = int(input("column?"))

            try:
                if self.board.check_input(row, column):
                    break
            except:
                print("Oops, your input is invalid")

        return row, column


game_controller = GameController()
game_controller.start_game()
