# Group Name: Codemasters

# Import modules
import unittest
import board


class TestBoard(unittest.TestCase):

    # Method that runs before any test is run
    @classmethod
    def setUpClass(cls) -> None:
        print('===== Your test cases have begun executing =====\n')

    # Method that runs after all tests have run
    @classmethod
    def tearDownClass(cls) -> None:
        print('===== All your test cases have run =====\n')

    # Test that checks the number of columns in the grid is 9
    def test_no_columns(self):
        self.assertEqual(board.Board.no_grid_columns(self), 9)
        self.assertEqual(board.Board.no_grid_columns(self) + board.Board.no_grid_columns(self), 18)
        self.assertEqual(board.Board.no_grid_columns(self) * board.Board.no_grid_columns(self), 81)

    # Test that checks the number of rows in the grid is 9
    def test_no_rows(self):
        self.assertEqual(board.Board.no_grid_rows(self), 9)
        self.assertEqual(board.Board.no_grid_rows(self) + board.Board.no_grid_rows(self), 18)
        self.assertEqual(board.Board.no_grid_rows(self) * board.Board.no_grid_rows(self), 81)

    # Test that checks that grid is a square grid i.e., 9 x 9
    def test_if_square_grid(self):
        self.assertEqual(board.Board.no_grid_rows(self), board.Board.no_grid_columns(self))
        self.assertEqual(board.Board.no_grid_rows(self) * board.Board.no_grid_columns(self), 81)

    # Test that checks number of columns equal that of rows
    def test_equal_row_column(self):
        self.assertEqual(board.Board.no_grid_rows(self), board.Board.no_grid_columns(self))

    #  Test that checks only single digits are filled
    def test_single_grid_values(self):
        self.assertLess(board.Board.no_grid_rows(self), 10)
        self.assertLess(board.Board.no_grid_columns(self), 10)


if __name__ == '__main__':
    unittest.main()

user_actions = 'Run tests for board class'