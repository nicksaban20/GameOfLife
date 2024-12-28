from functions import load_board_state, next_board_state, render
import time
import os


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
initial_state = load_board_state("./Python/GameOfLife/GGG.txt")
render(initial_state)

while True:
    os.system('clear')
    next_state = next_board_state(initial_state)
    render(next_state)
    initial_state = next_state
    time.sleep(0.1)
