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

    def test_validate_fields(self):
        # def validate_fields(number, y, x)
        self.assertTrue(self.sudoku.validate_fields(5, 0, 0))
        self.assertTrue(self.sudoku.validate_fields(8, 0, 2))
        self.assertTrue(self.sudoku.validate_fields(9, 0, 4)) 
        
    def test_validate_fields_rows(self):
        self.assertFalse(self.sudoku.validate_fields(8, 2, 1)) # jei assertTrue: gausim False is not true
        self.assertFalse(self.sudoku.validate_fields(5, 2, 4))
        self.assertFalse(self.sudoku.validate_fields(9, 4, 3))

    def test_validate_fields_columns(self):
        self.assertFalse(self.sudoku.validate_fields(9, 0, 0))
        self.assertFalse(self.sudoku.validate_fields(7, 8, 2))
        self.assertFalse(self.sudoku.validate_fields(4, 8, 4))

    def test_validate_fields_block3x3(self):
        self.assertFalse(self.sudoku.validate_fields(1, 1, 1))
        self.assertFalse(self.sudoku.validate_fields(3, 6, 8))
        self.assertFalse(self.sudoku.validate_fields(9, 8, 0))

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

    def test_print_gameboard(self):
        expected_result = """| 0 6 0 | 3 0 2 | 0 0 1 |
| 3 0 0 | 0 0 0 | 0 6 8 |
| 7 0 1 | 5 0 0 | 9 0 0 |
- - - - - - - - - - - - - 
| 0 8 0 | 9 0 3 | 7 0 0 |
| 9 0 0 | 0 2 0 | 0 0 0 |
| 6 0 7 | 0 0 1 | 2 5 0 |
- - - - - - - - - - - - - 
| 1 0 9 | 0 0 6 | 0 0 0 |
| 0 5 0 | 7 4 0 | 0 3 0 |
| 0 2 0 | 0 0 5 | 0 0 0 |
"""
        result = self.sudoku.print_gameboard()
        self.assertEqual(expected_result, result)

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

    def test_find_all_empty_fields(self):
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
        empty_fields = [
            (0, 0), (0, 2), (0, 4), (0, 6), (0, 7),
            (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
            (2, 1), (2, 4), (2, 5), (2, 7), (2, 8),
            (3, 0), (3, 2), (3, 4), (3, 7), (3, 8),
            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 1), (5, 3), (5, 4), (5, 8),
            (6, 1), (6, 3), (6, 4), (6, 6), (6, 7), (6, 8),
            (7, 0), (7, 2), (7, 5), (7, 6), (7, 8),
            (8, 0), (8, 2), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8)
        ]

        sudoku = Sudoku(gameboard)
        empty = sudoku.find_all_empty_fields()
        for coord in empty:
            self.assertIn(coord, empty_fields)
        self.assertEqual(empty_fields, empty)
        
    def test_find_all_empty_fields2(self):
        gameboard = [
            [0, 6, 0, 3, 0, 2],
            [3, 0, 4, 0, 5, 0],
            [7, 0, 1, 5, 0, 6],
        ]

        empty_fields = [(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (1, 5), (2, 1), (2, 4)]
        sudoku = Sudoku(gameboard)
        empty = sudoku.find_all_empty_fields()
        for coord in empty:
            self.assertIn(coord, empty_fields)
        self.assertEqual(empty_fields, empty)

    def test_find_empty_field(self):
        gameboard = [
            [1, 2, 3],
            [3, 0, 2],
            [2, 3, 1],
        ]

        sudoku = Sudoku(gameboard)

        self.assertEqual((1, 1), sudoku.find_empty_field())

if __name__ == "__main__":
    unittest.main()
