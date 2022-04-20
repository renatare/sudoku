from sudoku_solver import Sudoku
from datetime import datetime
from loginimas import logger

if __name__ == "__main__":
    start_time = datetime.now()

    def load_puzzle_from_file():
        gameboard = []
        with open('sudoku_puzzle.txt', 'r') as file:
            for line in file.readlines():
                gameboard_line = [int(element) for element in line.strip()]
                gameboard.append(gameboard_line)
        return gameboard

    def upload_puzzle_to_file():
        with open("sudoku_puzzle_result.txt", 'w', encoding="utf-8") as failas:
            failas.write("---------------------------- \n UNSOLVED SUDOKU GAMEBOARD\n----------------------------\n")
            failas.write(sudoku.print_gameboard())
            failas.close()

    def upload_puzzle_result_to_file():
        with open("sudoku_puzzle_result.txt", 'a', encoding="utf-8") as failas:
            failas.write("\n---------------------------- \n      SOLVED SUDOKU\n----------------------------\n")
            failas.write(sudoku.print_gameboard())
            failas.close()

    gameboard = load_puzzle_from_file()
    sudoku = Sudoku(gameboard)

    sudoku.validate_gameboard()
    upload_puzzle_to_file()

    sudoku.solve_sudoku()
    upload_puzzle_result_to_file()

    end_time = datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds()

    logger.info(f"\n Pradzia {start_time},\n Pabaiga {end_time}, \n Ivykdymo laikas {execution_time}")
