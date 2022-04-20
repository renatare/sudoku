from sudoku_solver import Sudoku
from datetime import datetime
from loginimas import logger

if __name__ == "__main__":
    start_time = datetime.now()

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

    end_time = datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds()

    logger.info(f"\n Pradzia {start_time},\n Pabaiga {end_time}, \n Ivykdymo laikas {execution_time}")
    
