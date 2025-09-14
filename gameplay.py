import validation
import copy
import time
import os
from block import Block


def clear():
    if os.name == 'nt':
        os.system('cls')


def movement(frame, block,  x_coordinate, y_coordinate, Score, renderer, key=""):
    time.sleep(0.05)
    if key == b"":
        if not validation.is_below_blocked(copy.deepcopy(frame), block, x_coordinate, y_coordinate, block.width, block.height):
            clear()
            renderer.eraseBlock(frame, block, x_coordinate,
                                y_coordinate, block.width, block.height)
            y_coordinate += 1
            renderer.drawBlock(frame, block, x_coordinate,
                               y_coordinate, block.width, block.height)
            renderer.drawFrame(frame, Score)
            print()
            return x_coordinate, y_coordinate, block, True
        else:
            return x_coordinate, y_coordinate, block, False
    elif key == b"r":
        renderer.eraseBlock(frame, block, x_coordinate,
                            y_coordinate, block.width, block.height)
        block.rotate()
        return x_coordinate, y_coordinate, block, True
    elif key == b"a":
        if not validation.is_left_blocked(copy.deepcopy(frame), block,  x_coordinate, y_coordinate, block.width, block.height):
            clear()
            renderer.eraseBlock(frame, block, x_coordinate,
                                y_coordinate, block.width, block.height)
            x_coordinate -= 1
            renderer.drawBlock(frame, block, x_coordinate,
                               y_coordinate, block.width, block.height)
            renderer.drawFrame(frame, Score)

            return x_coordinate, y_coordinate, block, True
        else:
            return x_coordinate, y_coordinate, block, True

    elif key == b"d":
        if not validation.is_right_blocked(copy.deepcopy(frame), block,  x_coordinate, y_coordinate, block.width, block.height):
            clear()
            renderer.eraseBlock(frame, block, x_coordinate,
                                y_coordinate, block.width, block.height)
            x_coordinate += 1
            renderer.drawBlock(frame, block, x_coordinate,
                               y_coordinate, block.width, block.height)
            renderer.drawFrame(frame, Score)
            return x_coordinate, y_coordinate, block, True
        else:
            return x_coordinate, y_coordinate, block, True
    else:
        return x_coordinate, y_coordinate, block, True


def rows_shifting(frame, row, renderer):
    for y in range(row, 2, -1):
        for x in range(renderer.WIDTH):
            frame[y][x] = frame[y-1][x]
    for i in range(renderer.WIDTH):
        if frame[1][i] == "|":
            continue
        else:
            frame[1][i] = "."
