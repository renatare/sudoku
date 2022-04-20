Sudoku Puzzle Solver.
(without GUI)

This is a Python script that solves Sudoku puzzles. 

You need to know how Sudoku works.
In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. No number in that row, column and 3 x 3 subgrid can repeat.

Requirements.
This code was written using Python 3.10.4, but it should work with any recent Python 3 version.
You can check the code by running main.py file.

Sudoku Puzzle files.
To define a sudoku puzzle to solve, you need to save the "grid" to a txt file. The format is: 9 rows with 9 digits per row. For empty cells in the grid use 0.
3 files are given as Sudoku puzzle examples in the folder named "files".

Algorithm to solve the puzzle:
1. Iterate through the cells row-by-row until you find an empty cell.
2. Test numbers from 1 to 9 for that cell. Find a valid number and fill the cell with that number.
3. Once you find a valid number, repeat steps 1 and 2.
4. If no number is valid in the empty cell, backtrack and move to previous cell filled by the algorithm to find the next valid number and repeat steps 1 and 2.
5. Repeat process until no empty cell exists in the puzzle.

The main functions of Sudoku solver are in sudoku_solver.py file.
Unit tests are written in test_sudoku_solver.py file.
