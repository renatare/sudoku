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
            raise ValueError("Standartiniame Sudoku turi būti 9 stulpeliai")
    if len(gameboard) != 9:
        raise ValueError("Standartiniame Sudoku turi būti 9 eilutės")

validate_gameboard(gameboard)
print_gameboard(gameboard)
