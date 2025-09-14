import random


class Block:
    def __init__(self):
        self.shape, self.w, self.h = self.generateBlock(random.randint(1, 6))

    def rotate(self):

        transposed = list(zip(*self.shape))
        Matrix = []
        for i in range(len(transposed)):
            rows = []
            for j in range(len(transposed[0])):
                rows.append(transposed[len(transposed)-i-1][j])
            Matrix.append(rows)
        self.shape = Matrix
        self.w = len(Matrix[0])
        self.h = len(Matrix)
        return self.shape

    def generateBlock(self, i):
        block = i
        w, h = 0, 0
        match block:
            case 1:
                shape = [
                    ["#", "#", "#", "#"]
                ]
                w, h = 4, 1
            case 2:
                shape = [
                    ["#", " ", " "],
                    ["#", "#", "#"]
                ]
                w, h = 3, 2
            case 3:
                shape = [
                    [" ", " ", "#"],
                    ["#", "#", "#"]
                ]
                w, h = 3, 2
            case 4:
                shape = [
                    [" ", "#", " "],
                    ["#", "#", "#"]
                ]
                w, h = 3, 2
            case 5:
                shape = [
                    ["#", "#"],
                    ["#", "#"]
                ]
                w, h = 2, 2
            case 6:
                shape = [
                    [" ", "#", "#"],
                    ["#", "#", " "]
                ]
                w, h = 3, 2
        return shape, w, h
