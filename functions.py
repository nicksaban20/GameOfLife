import random

board_state =  [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]

def dead_state(input_columns, input_rows):
    return [[0 for x in range(input_columns)] for y in range(input_rows)]

def random_state(input_columns, input_rows):
    state = dead_state(input_columns, input_rows)
    for row in range(input_rows):
        for column in range(input_columns):
            random_number = random.random()
            if random_number >= 0.5:
                state[row][column] = 0
            else:
                state[row][column] = 1
    return state

def render(board):
    for column in range(len(board[0]) + 4):
        print("-", end='')
    print()
    for row in range(len(board)):
        print("| ", end='')
        for column in range(len(board[0])):
            # print(board[row][column] , end='')
            if board[row][column] == 1:
                print("#" , end='')
            else:
                print(" ", end='')
        print(" |")
    for column in range(len(board[0]) + 4):
        print("-", end='')
    print()

def next_board_state(board):
    new_board = dead_state(len(board[0]), len(board))
    for row in range(len(board)):
        for column in range(len(board[0])):
            live_neighbors = 0
            try:
                if board[row - 1][column] == 1 and row - 1 >= 0:
                    live_neighbors += 1
            except:
                pass
            try:            
                if board[row - 1][column - 1] == 1 and row - 1 >= 0 and column - 1 >= 0:
                    live_neighbors += 1
            except:
                pass
            try:
                if board[row][column - 1] == 1 and column - 1 >= 0:
                    live_neighbors += 1
            except:
                pass
            try:
                if board[row + 1][column - 1] == 1 and column - 1 >= 0:
                    live_neighbors += 1
            except:
                pass
            try:
                if board[row + 1][column] == 1 and row + 1 < len(board):
                    live_neighbors += 1
            except:
                pass
            try:
                if board[row + 1][column + 1] == 1 and row + 1 < len(board):
                    live_neighbors += 1
            except:
                pass
            try:
                if board[row][column + 1] == 1 and column + 1 < len(board[0]):
                    live_neighbors += 1   
            except:
                pass
            try:
                if board[row - 1][column + 1] == 1 and row - 1 >= 0 and column + 1 < len(board[0]):
                    live_neighbors += 1
            except:
                pass


            if live_neighbors < 2 and board[row][column] == 1:
                new_board[row][column] = 0
            elif live_neighbors == 2 and board[row][column] == 1 or live_neighbors == 3 and board[row][column] == 1:
                new_board[row][column] = 1
            elif live_neighbors > 3 and board[row][column] == 1:
                new_board[row][column] = 0
            elif live_neighbors == 3 and board[row][column] == 0:
                new_board[row][column] = 1

    return new_board

def load_board_state(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        board_state = [[0 for _ in range(len(lines[0].strip()))] for _ in range(len(lines))]
        for line in range(len(lines)):
            lines[line] = lines[line].strip()
            for column in range(len(lines[line])):
                if lines[line][column] == "1":
                    board_state[line][column] = 1
                else:
                    board_state[line][column] = 0
    return board_state
