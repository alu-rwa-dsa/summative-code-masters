# # Group Name: Codemasters

import random

# Importing modules
import pygame
from numpy import random


class Sudoku:
    # def __init__(self, no_rows, no_columns):
    #     self.no_rows = no_rows
    #     self.no_columns = no_columns
    #
    # # Method to assign random integers to rows
    # # The method assigns unique integers
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

    # Method to assign random integers to columns
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

print('Choose level\nB. Beginner\nI. Intermediate\nA. Advanced')

grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Initializing font
pygame.font.init()

# Game window
screen = pygame.display.set_mode((600, 600))



x = 0
y = 0
dif = 500 / 9
val = 0

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsansms", 20)


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    # Function to draw required lines for making Sudoku grid


def draw():
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (255, 180, 255), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill gird with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
            # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(screen, (255, 100, 50), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (255, 100, 50), (i * dif, 0), (i * dif, 500), thick)

    # Fill value entered in cell


def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it) == True:
            grid[i][j] = it
            global x, y
            x = i
            y = j
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            # white color background\
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


# Display instruction for the game
def instruction():
    text1 = font2.render("Press R: RESET  Press C: CLEAR", 1, (0, 0, 0))
    text2 = font2.render("Press B: Beginner  I: Intermediate  A: Advanced", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or C", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0


# The game loop
while run:
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_c:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]

            if event.key == pygame.K_b:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
            if event.key == pygame.K_i:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 8, 0, 4, 0, 0, 1, 0, 0],
                    [6, 0, 0, 0, 0, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 9, 3, 0],
                    [9, 0, 4, 0, 0, 0, 0, 0, 0],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 0, 2, 0, 6, 0, 0, 7]
                ]
            if event.key == pygame.K_a:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 8, 0, 0, 0, 0, 1, 2, 0],
                    [0, 0, 0, 0, 0, 5, 0, 0, 0],
                    [0, 0, 0, 6, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 4, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 9, 0, 0],
                    [9, 0, 4, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 0, 2, 0, 0, 0, 0, 0]
                ]

    if flag2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)
        # print(x)
        # print(y)
        if valid(grid, int(x), int(y), val) == True:
            grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    # Update window
    pygame.display.update()

# Quit pygame window
pygame.quit()

user_actions = 'Run sudoku.py'