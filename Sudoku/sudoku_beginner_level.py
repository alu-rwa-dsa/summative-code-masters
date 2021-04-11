# Authors: Marthely237 and Sammyiel
# Group Name: Codemasters

# Importing modules
import random

from sudoku import Sudoku

class Sudoku_Beginner_Level(Sudoku):
    def __init__(self):
        super().__init__(self)

    # Method to fill random integers to rows
    # The method assigns 6 unique integers
    def fill_6_cells(self):
        no_columns = 0
        row = []
        while True:
            for i in range(1000):
                row_value = random.randint(1, 9)
                if row_value not in row:
                    row.append(row_value)
                    no_columns = len(row)
                    if no_columns > 5:
                        break

            # print(no_columns)
            # print(row)
            # print(len(row))

            return no_columns
    # fill_6_cells('self')

user_actions = 'Run Sudoku beginner level'



