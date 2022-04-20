class Sudoku:
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def print_gameboard(self):
        result = ''
        for row in range(len(self.gameboard)):
            if row % 3 == 0 and row != 0:
                result += "- " * 13 + '\n'

            for column in range(len(self.gameboard[0])):
                if column % 3 == 0:
                    result += "| "

                if column == len(self.gameboard[0]) - 1:
                    result += str(self.gameboard[row][column]) + " |"
                else:
                    result += str(self.gameboard[row][column]) + " "
            result += '\n'

        return result

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
                    return (row, colum) # row is y_axis, column is x_axis

    def find_all_empty_fields(self):
        empty_fields = []
        for row in range(len(self.gameboard)):
            for colum in range(len(self.gameboard[0])):
                if self.gameboard[row][colum] == 0:
                    position = (row, colum)
                    empty_fields.append(position)
        return empty_fields

    def validate_fields(self, number, y, x): #(y, x) is empty position
        for yy in range(len(self.gameboard)):
            if self.gameboard[yy][x] == number and (yy, x) != (y, x): # checks if number not in the column
                return False

        for xx in range(len(self.gameboard[0])):
            if self.gameboard[y][xx] == number and (y, xx) != (y, x): # checks if number not in the row
                return False

        block_x = x // 3 * 3
        block_y = y // 3 * 3

        for yy in range(block_y, block_y + 3):
            for xx in range(block_x, block_x + 3):
                if self.gameboard[yy][xx] == number and (yy, xx) != (y, x):
                    return False

        return True

    def solve_sudoku(self):
        empty_position = self.find_empty_field()
        if not empty_position:
            return True # print("Sudoku is solved")
        
        y, x = empty_position # row is y_axis, column is x_axis
        
        for number in range(1, 10):
            if self.validate_fields(number, y, x):
                self.gameboard[y][x] = number
                
                if self.solve_sudoku():
                    return True
                else:
                    self.gameboard[y][x] = 0
        return False
