import unittest
from sudoku_solver import *

class TestSudoku(unittest.TestCase):
    def setUp(self):
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

        self.sudoku = Sudoku(gameboard)

    def test_solve_sudoku(self):
        expected_result = [
            [5, 6, 8, 3, 9, 2, 4, 7, 1],
            [3, 9, 2, 1, 7, 4, 5, 6, 8],
            [7, 4, 1, 5, 6, 8, 9, 2, 3],
            [2, 8, 4, 9, 5, 3, 7, 1, 6],
            [9, 1, 5, 6, 2, 7, 3, 8, 4],
            [6, 3, 7, 4, 8, 1, 2, 5, 9],
            [1, 7, 9, 2, 3, 6, 8, 4, 5],
            [8, 5, 6, 7, 4, 9, 1, 3, 2],
            [4, 2, 3, 8, 1, 5, 6, 9, 7]
        ]

        self.assertTrue(self.sudoku.solve_sudoku())
        self.assertEqual(expected_result, self.sudoku.gameboard)

    def test_validate_gameboard_rows(self):
        gameboard = [
            [0, 6, 0, 3, 0, 2, 0, 0, 1],
            [3, 0, 0, 0, 0, 0, 0, 6, 8],
            [7, 0, 1, 5, 0, 0, 9, 0, 0],
            [0, 8, 0, 9, 0, 3, 7, 0, 0],
            [9, 0, 0, 0, 2, 0, 0, 0, 0],
            [6, 0, 7, 0, 0, 1, 2, 5, 0],
            [1, 0, 9, 0, 0, 6, 0, 0, 0],
            [0, 5, 0, 7, 4, 0, 0, 3, 0]
        ]

        sudoku = Sudoku(gameboard)

        with self.assertRaises(ValueError) as error:
            sudoku.validate_gameboard()
        self.assertEqual("Klasikiniame Sudoku turi būti 9 eilutės", str(error.exception))

    def test_validate_gameboard_columns(self):
        gameboard = [
            [0, 6, 0, 3, 0, 2, 0, 0, 1],
            [3, 0, 0, 0, 0, 0, 0, 6, 8],
            [7, 0, 1, 5, 0, 0, 9, 0],
            [0, 8, 0, 9, 0, 3, 7, 0, 0],
            [9, 0, 0, 0, 2, 0, 0, 0, 0],
            [6, 0, 7, 0, 0, 1, 2, 5, 0],
            [1, 0, 9, 0, 0, 6, 0, 0, 0],
            [0, 5, 0, 7, 4, 0, 0, 3, 0],
            [0, 2, 0, 0, 0, 5, 0, 0, 0]
        ]

        sudoku = Sudoku(gameboard)

        with self.assertRaises(ValueError) as error:
            sudoku.validate_gameboard()
        self.assertEqual("Klasikiniame Sudoku turi būti 9 stulpeliai", str(error.exception))


if __name__ == "__main__":
    unittest.main()
