# # Group Name: Codemasters

# Importing modules
import pygame
import random
import numpy as np
from numpy import random


class Board:
    def __init__(self, no_rows, no_columns):
        self.no_rows = no_rows
        self.no_columns = no_columns

    # Method to fill random integers to rows
    # The method assigns unique integers
    def no_grid_columns(self):
        row = []
        for i in range(100):
            row_value = random.randint(1, 10)
            if row_value not in row:
                row.append(row_value)
        no_columns = len(row)
        # print(row)

        return no_columns
    # no_grid_columns('self')

    # Method to fill random integers to columns
    # The method assigns unique integers
    def no_grid_rows(self):
        no_rows = 0
        col_list = []
        column = [0]
        for i in range(100):
            col_value = random.randint(1, 10)
            if col_value not in col_list:
                current_value = col_value
                col_list.append(current_value)

        for j in col_list:
            for rows in column:
                if rows == 0:
                    rows = [j]
                    no_rows = no_rows + 1
            # print(rows)
        # print(no_rows)
        return no_rows

user_actions = 'Run board.py'