class Renderer:
    def __init__(self):
        self.HEIGHT, self.WIDTH = 30, 15
        self.frame = []

    def generateFrame(self):
        for y in range(self.HEIGHT):
            row = []
            for x in range(self.WIDTH):
                if y == 0 or y == self.HEIGHT-1:
                    row.append("_")
                elif x == 0 or x == self.WIDTH-1:
                    row.append("|")
                else:
                    row.append(".")
            self.frame.append(row)
        return self.frame

    def drawFrame(self, frame, Score):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                print(frame[y][x], end="")
            print()
        print(f"Score: {Score['score']}")

    def drawBlock(self, frame, block, x_coordinate, y_coordinate, width, height):
        for column in range(height):
            for row in range(width):
                if block.shape[-1-column][row] != " ":
                    frame[y_coordinate-column][x_coordinate +
                                               row] = block.shape[-1-column][row]

    def eraseBlock(self, frame, block, x_coordinate, y_coordinate, width, height):
        for h in range(height):
            for w in range(width):
                if block.shape[-1-h][w] != " ":
                    frame[y_coordinate-h][x_coordinate+w] = "."
