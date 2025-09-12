import validation
import copy
import time
import os
from block import Block


def clear():
    if os.name == 'nt':
        os.system('cls')


def movement(frame, block,  x, y, Score, renderer, key=""):
    time.sleep(0.05)
    if key == b"":
        if not validation.is_below_blocked(copy.deepcopy(frame), block, x, y, block.w, block.h):
            clear()
            renderer.eraseBlock(frame, block, x, y, block.w, block.h)
            y += 1
            renderer.drawBlock(frame, block, x, y, block.w, block.h)
            renderer.drawFrame(frame, Score)
            print()
            return x, y, block, True
        else:
            return x, y, block, False
    elif key == b"r":
        renderer.eraseBlock(frame, block, x, y, block.w, block.h)
        block.rotate()
        return x, y, block, True
    elif key == b"a":
        if not validation.is_left_blocked(copy.deepcopy(frame), block,  x, y, block.w, block.h):
            clear()
            renderer.eraseBlock(frame, block, x, y, block.w, block.h)
            x -= 1
            renderer.drawBlock(frame, block, x, y, block.w, block.h)
            renderer.drawFrame(frame, Score)

            return x, y, block, True
        else:
            return x, y, block, True

    elif key == b"d":
        if not validation.is_right_blocked(copy.deepcopy(frame), block,  x, y, block.w, block.h):
            clear()
            renderer.eraseBlock(frame, block, x, y, block.w, block.h)
            x += 1
            renderer.drawBlock(frame, block, x, y, block.w, block.h)
            renderer.drawFrame(frame, Score)
            return x, y, block, True
        else:
            return x, y, block, True
    else:
        return x, y, block, True


def rows_shifting(frame, row, renderer):
    for y in range(row, 2, -1):
        for x in range(renderer.WIDTH):
            frame[y][x] = frame[y-1][x]
    for i in range(renderer.WIDTH):
        if frame[1][i] == "|":
            continue
        else:
            frame[1][i] = "."
