
# Group Name: Codemasters

# Import modules
import unittest
import sudoku


class TestSudoku(unittest.TestCase):

    # Method that runs before any test is run
    @classmethod
    def setUpClass(cls) -> None:
        print('===== Your test cases have begun executing =====\n')

    # Method that runs after all tests have run
    @classmethod
    def tearDownClass(cls) -> None:
        print('===== All your test cases have run =====\n')

    # Test that checks that all grid values are single digits
    def test_single_grid_values(self):
        self.assertLess(sudoku.Sudoku.no_grid_columns(self), 10)
        self.assertLess(sudoku.Sudoku.no_grid_columns(self), 10)

    # Test that checks the number of columns
    def test_no_columns(self):
        self.assertEqual(sudoku.Sudoku.no_grid_columns(self), 9)
        self.assertEqual(sudoku.Sudoku.no_grid_columns(self) + sudoku.Sudoku.no_grid_columns(self), 18)
        self.assertEqual(sudoku.Sudoku.no_grid_columns(self) * sudoku.Sudoku.no_grid_columns(self), 81)

    # Test that checks the number of rows in the grid
    def test_no_rows(self):
        self.assertEqual(sudoku.Sudoku.no_grid_rows(self), 9)
        self.assertEqual(sudoku.Sudoku.no_grid_rows(self) + sudoku.Sudoku.no_grid_rows(self), 18)
        self.assertEqual(sudoku.Sudoku.no_grid_rows(self) * sudoku.Sudoku.no_grid_rows(self), 81)

    # Test that checks that grid is a square grid i.e., n x n
    def test_if_square_grid(self):
        self.assertEqual(sudoku.Sudoku.no_grid_rows(self), sudoku.Sudoku.no_grid_columns(self))
        self.assertEqual(sudoku.Sudoku.no_grid_rows(self) * sudoku.Sudoku.no_grid_columns(self), 81)

    # Test that checks number of columns equal that of rows
    def test_equal_rows_columns(self):
        self.assertEqual(sudoku.Sudoku.no_grid_rows(self), sudoku.Sudoku.no_grid_columns(self))

if __name__ == '__main__':
    unittest.main()

user_actions = 'Run tests for sudoku.py'