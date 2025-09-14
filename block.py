import random


class Block:
    def __init__(self):
        self.shape, self.width, self.height = self.generateBlock(
            random.randint(1, 6))

    def rotate(self):

        transposed = list(zip(*self.shape))
        new_shape = []
        for row in range(len(transposed)):
            new_row = []
            for column in range(len(transposed[0])):
                new_row.append(transposed[len(transposed)-row-1][column])
            new_shape .append(new_row)
        self.shape = new_shape
        self.width = len(new_shape[0])
        self.height = len(new_shape)
        return self.shape

    def generateBlock(self, number):
        block_number = number
        width, height = 0, 0
        match block_number:
            case 1:
                shape = [
                    ["#", "#", "#", "#"]
                ]
                width, height = 4, 1
            case 2:
                shape = [
                    ["#", " ", " "],
                    ["#", "#", "#"]
                ]
                width, height = 3, 2
            case 3:
                shape = [
                    [" ", " ", "#"],
                    ["#", "#", "#"]
                ]
                width, height = 3, 2
            case 4:
                shape = [
                    [" ", "#", " "],
                    ["#", "#", "#"]
                ]
                width, height = 3, 2
            case 5:
                shape = [
                    ["#", "#"],
                    ["#", "#"]
                ]
                width, height = 2, 2
            case 6:
                shape = [
                    [" ", "#", "#"],
                    ["#", "#", " "]
                ]
                width, height = 3, 2
        return shape, width, height
