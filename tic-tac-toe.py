
class board:
    def __init__(self):
        self.initialize()
        self.print()

    def initialize(self):
        self.grid = [] 
        for i in range(3):
            self.grid.append(['', '', ''])

    def place(self, value, row, column):
        row = int(row)
        column = int(column)
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise ("invalid operation")
        if self.isPlaced(row, column):
            raise ("this location is alreay placed")
        self.grid[row][column] = value

        self.print()
        return

    def isPlaced(self, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise ("invalid operation")
        return self.grid[row][column] != ''

    def won(self):
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == 'x' or \
           self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == 'o' or \
           self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == 'x' or \
           self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == 'o' or \
           self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == 'x' or \
           self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == 'o' or \
           self.grid[0][0] == self.grid[1][0] == self.grid[2][0] == 'x' or \
           self.grid[0][0] == self.grid[1][0] == self.grid[2][0] == 'o' or \
           self.grid[0][1] == self.grid[1][1] == self.grid[2][1] == 'x' or \
           self.grid[0][1] == self.grid[1][1] == self.grid[2][1] == 'o' or \
           self.grid[0][2] == self.grid[1][2] == self.grid[2][2] == 'x' or \
           self.grid[0][2] == self.grid[1][2] == self.grid[2][2] == 'o' or \
           self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == 'x' or \
           self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == 'o':
            return True
        return False

    def print(self):
        for row in self.grid:
            print(row)

#represent 'x', make moves after human
def computer():
    def __init__(self, board):
        pass

    def think(self, board):
        pass

    def think(self, board, row, column):
        pass

board = board()

while (not board.won()):
    row = int(input("row?"))
    column = int(input("column?"))
    value = input("computer => x; human => o")
    board.place(value, row, column)