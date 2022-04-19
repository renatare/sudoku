from sudoku_solver import Sudoku

if __name__ == "__main__":
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

    sudoku = Sudoku(gameboard)

    sudoku.validate_gameboard()
    #sudoku.print_gameboard()
    sudoku.solve_sudoku()
    sudoku.print_gameboard()
