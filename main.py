from sudoku_solver import Sudoku
from file_opener import FileOpener
from datetime import datetime
from loginimas import logger

if __name__ == "__main__":
    start_time = datetime.now()

    file_opener = FileOpener()
    gameboard = file_opener.read_from_file('sudoku_puzzle.txt')
    sudoku = Sudoku(gameboard)

    sudoku.validate_gameboard()
    file_opener.upload_to_file(
        'sudoku_puzzle_result.txt',
        f'\n-------------------------\nUNSOLVED SUDOKU GAMEBOARD\n-------------------------\n{sudoku.print_gameboard()}'
    )

    sudoku.solve_sudoku()
    file_opener.append_to_file(
        'sudoku_puzzle_result.txt',
        f'\n-------------------------\n SOLVED SUDOKU GAMEBOARD\n-------------------------\n{sudoku.print_gameboard()}'
    )

    end_time = datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds()

    logger.info(f"\n Pradzia {start_time},\n Pabaiga {end_time}, \n Ivykdymo laikas {execution_time}")
