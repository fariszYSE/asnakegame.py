import os
import time
import random
import msvcrt

# Game settings
WIDTH = 35
HEIGHT = 15
FPS = 5
FRAME_TIME = 1.0 / FPS

# Directions (dx, dy)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initial snake
snake = [(5, 5)]
direction = RIGHT

# Place first food
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

def draw():
    os.system("cls")  # Clear console
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if (x, y) in snake:
                line += "O"
            elif (x, y) == food:
                line += "X"
            else:
                line += "."
        print(line)

def update_direction():
    global direction
    if msvcrt.kbhit():
        key = msvcrt.getch()

        # Arrow keys send a prefix byte first
        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()  # actual code

            if key == b'H' and direction != DOWN:   # Up arrow
                direction = UP
            elif key == b'P' and direction != UP:   # Down arrow
                direction = DOWN
            elif key == b'K' and direction != RIGHT:  # Left arrow
                direction = LEFT
            elif key == b'M' and direction != LEFT:   # Right arrow
                direction = RIGHT

def move_snake():
    global food
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # Check walls
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        return False  # Game over

    # Check self collision
    if new_head in snake:
        return False  # Game over

    # Move snake
    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.pop()

    return True

# Main game loop
while True:
    start = time.time()
    update_direction()
    if not move_snake():
        print("Game Over!, click any button to quit")
        msvcrt.getch() #add a "hit any button to play again" instead
        break
    draw()
    elapsed = time.time() - start
    time.sleep(max(0, FRAME_TIME - elapsed))