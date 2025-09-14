import gameplay


def is_below_blocked(frame, block, x_coordinate, y_coordinate, width, height):
    for column in range(height):
        for row in range(width):
            if 0 <= x_coordinate+row and x_coordinate+row < len(frame[0]) and 0 <= y_coordinate and y_coordinate < len(frame):
                if block.shape[-1-column][row] == "#":
                    if y_coordinate-column + 1 >= len(frame):
                        return True
                    if frame[y_coordinate-column+1][x_coordinate+row] in ("#", "_"):
                        return True
                    frame[y_coordinate-column][x_coordinate+row] = "."
    return False


def is_left_blocked(frame, block, x_coordinate, y_coordinate, width, height):
    for row in range(width):
        for column in range(height):
            if 0 <= y_coordinate < len(frame) and 0 <= x_coordinate-row < len(frame[0]):
                if block.shape[-1-column][row] == "#":
                    if x_coordinate-row-1 >= len(frame[0]):
                        return True
                    if frame[y_coordinate-column][x_coordinate+row-1] in ("#", "|"):
                        return True
                frame[y_coordinate-column][x_coordinate+row] = "."
    return False


def is_right_blocked(frame, block, x_coordinate, y_coordinate, width, height):
    for row in range(width):
        for column in range(height):
            if 0 <= y_coordinate < len(frame) and 0 <= x_coordinate + width < len(frame[0]):
                if block.shape[-1-column][width - 1-row] == "#":
                    if x_coordinate + width - row >= len(frame[0]):
                        return True
                    if frame[y_coordinate - column][x_coordinate + width - row] in ("#", "|"):
                        return True
                frame[y_coordinate - column][x_coordinate + width - 1-row] = "."
    return False


def is_row_full(frame, Score, renderer):
    isFull = False
    for y in range(renderer.HEIGHT-2, 1, -1):
        for x in range(renderer.WIDTH):
            if frame[y][x] == ".":
                isFull = False
                break
            isFull = True
        while isFull:
            gameplay.rows_shifting(frame, y, renderer)
            Score["score"] += 1
            for x in range(renderer.WIDTH):
                if frame[y][x] == ".":
                    isFull = False
                    break
                isFull = True
