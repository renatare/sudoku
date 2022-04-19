class Sudoku:
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def print_gameboard(self):
        for row in range(len(self.gameboard)):
            if row % 3 == 0 and row != 0:
                print("- " * 13 + '\n', end="")

            for column in range(len(self.gameboard[0])):
                if column % 3 == 0:
                    print("| ", end="")

                if column == 8:
                    print(str(self.gameboard[row][column]) + " |")
                else:
                    print(str(self.gameboard[row][column]) + " ", end="")

    def validate_gameboard(self):
        for row in self.gameboard:
            if len(row) != 9:
                raise ValueError("Klasikiniame Sudoku turi būti 9 stulpeliai")
        if len(self.gameboard) != 9:
            raise ValueError("Klasikiniame Sudoku turi būti 9 eilutės")

    def find_empty_field(self):
        for row in range(len(self.gameboard)):
            for colum in range(len(self.gameboard[0])):
                if self.gameboard[row][colum] == 0:
                    position = (row, colum)
                    return position

    def validate_fields(self, number, x, y):
        for row in range(len(self.gameboard)):
            if self.gameboard[row][y] == number and (row, y) != (x, y):
                return False

        for column in range(len(self.gameboard[0])):
            if self.gameboard[x][column] == number and (x, column) != (x, y):
                return False

        block_x = y // 3 * 3
        block_y = x // 3 * 3

        for i in range(block_y, block_y + 3):
            for j in range(block_x, block_x + 3):
                if self.gameboard[i][j] == number and (i, j) != (x, y):
                    return False

        return True

    def solve_sudoku(self):
        empty_position = self.find_empty_field()
        if not empty_position:
            return True # print("Sudoku is solved")
        
        x, y = empty_position
        
        for number in range(1, 10):
            if self.validate_fields(number, x, y):
                self.gameboard[x][y] = number
                
                if self.solve_sudoku():
                    return True
                else:
                    self.gameboard[x][y] = 0
        return False
