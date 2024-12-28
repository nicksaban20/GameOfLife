from functions import load_board_state, next_board_state, render, random_state, pygame_render
import time
import os
import pygame


# input_columns = 100
# input_rows = 100

# randomstate = random_state(input_columns, input_rows)
# render(randomstate)

# nextstate = next_board_state(randomstate)
# render(nextstate)


# initial_state = load_board_state("./Python/GameOfLife/toad.txt")
# initial_state = load_board_state("./Python/GameOfLife/beacon.txt")
# initial_state = load_board_state("./Python/GameOfLife/blinker.txt")
# initial_state = load_board_state("./Python/GameOfLife/glider.txt")

# initial_state = load_board_state("./Python/GameOfLife/GGG.txt")
# render(initial_state)

# while True:
#     os.system('clear')
#     next_state = next_board_state(initial_state)
#     render(next_state)
#     initial_state = next_state
#     time.sleep(0.1)

pygame.init()
pygame.display.set_caption("Game of Life")
initial_state = random_state(100, 100)
pygame_render(initial_state, 10)


while True:
    next_state = next_board_state(initial_state)
    pygame_render(next_state, 10)
    initial_state = next_state
    time.sleep(0.1)