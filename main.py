gameboard = [
    [0, 6, 0, 3, 0, 2, 0, 0, 1],
    [3, 0, 0, 0, 0, 0, 0, 6, 8],
    [7, 0, 1, 5, 0, 0, 9, 0, 0],
    [0, 8, 0, 9, 0, 3, 7, 0, 0],
    [9, 0, 0, 0, 2, 0, 0, 0, 0],
    [6, 0, 7, 0, 0, 1, 2, 5, 0],
    [1, 0, 9, 0, 0, 6, 0, 0, 0],
    [0, 5, 0, 7, 4, 0, 0, 3, 0],
    [0, 2, 0, 0, 0, 5, 0, 0, 0]
]

def print_gameboard(gameboard):
    for row in range(len(gameboard)):
        if row % 3 == 0 and row != 0:
            print("- " * 13 + '\n', end="") 
            # print("- - - - - - - - - - - - -\n", end="")

        for column in range(len(gameboard[0])):
            if column % 3 == 0: # and column != 0
                print("| ", end="")

            if column == 8:
                print(str(gameboard[row][column]) + " |")
            else:
                print(str(gameboard[row][column]) + " ", end="")

def validate_gameboard(gameboard):
    for row in gameboard:
        if len(row) != 9:
            raise ValueError("Klasikiniame Sudoku turi būti 9 stulpeliai")
    if len(gameboard) != 9:
        raise ValueError("Klasikiniame Sudoku turi būti 9 eilutės")

def find_empty_field(gameboard):
    for row in range(len(gameboard)):
        for colum in range(len(gameboard[0])):
            if gameboard[row][colum] == 0:
                position = (row, colum)
                return position

def validate_fields(gameboard, number, x, y):
    for row in range(len(gameboard)):
        if gameboard[row][y] == number and (row, y) != (x, y):
            return False

    for column in range(len(gameboard[0])):
        if gameboard[x][column] == number and (x, column) != (x, y):
            return False

    block_x = y // 3 * 3
    block_y = x // 3 * 3

    for i in range(block_y, block_y + 3):
        for j in range(block_x, block_x + 3):
            if gameboard[i][j] == number and (i, j) != (x, y):
                return False

    return True

def solve_sudoku(gameborad):
    empty_position = find_empty_field(gameboard)
    if not empty_position:
        return True # print("Sudoku is solved")
    
    x, y = empty_position
    
    for number in range(1, 10):
        if validate_fields(gameboard, number, x, y):
            gameboard[x][y] = number
            
            if solve_sudoku(gameboard):
                return True
            else:
                gameborad[x][y] = 0
    return False

validate_gameboard(gameboard)
solve_sudoku(gameboard)
print_gameboard(gameboard)
