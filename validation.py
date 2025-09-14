import gameplay


def is_below_blocked(frame, block, x, y, w, h):
    for i in range(h):
        for j in range(w):
            if 0 <= x+j and x+j < len(frame[0]) and 0 <= y and y < len(frame):
                if block.shape[-1-i][j] == "#":
                    if y-i + 1 >= len(frame):
                        return True
                    if frame[y-i+1][x+j] in ("#", "_"):
                        return True
                    frame[y-i][x+j] = "."
    return False


def is_left_blocked(frame, block, x, y, w, h):
    for i in range(w):
        for j in range(h):
            if 0 <= y < len(frame) and 0 <= x-i < len(frame[0]):
                if block.shape[-1-j][i] == "#":
                    if x-i-1 >= len(frame[0]):
                        return True
                    if frame[y-j][x+i-1] in ("#", "|"):
                        return True
                frame[y-j][x+i] = "."
    return False


def is_right_blocked(frame, block, x, y, w, h):
    for i in range(w):
        for j in range(h):
            if 0 <= y < len(frame) and 0 <= x+w < len(frame[0]):
                if block.shape[-1-j][w-1-i] == "#":
                    if x+w-i >= len(frame[0]):
                        return True
                    if frame[y-j][x+w-i] in ("#", "|"):
                        return True
                frame[y-j][x+w-1-i] = "."
    return False


def is_row_full(frame, Score, renderer):
    flag = False
    for y in range(renderer.HEIGHT-2, 1, -1):
        for x in range(renderer.WIDTH):
            if frame[y][x] == ".":
                flag = False
                break
            flag = True
        while flag:
            gameplay.rows_shifting(frame, y, renderer)
            Score["score"] += 1
            for x in range(renderer.WIDTH):
                if frame[y][x] == ".":
                    flag = False
                    break
                flag = True
