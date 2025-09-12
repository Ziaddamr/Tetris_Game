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

    def drawBlock(self, frame, block, x, y, w, h):
        for i in range(h):
            for j in range(w):
                if block.shape[-1-i][j] != " ":
                    frame[y-i][x+j] = block.shape[-1-i][j]

    def eraseBlock(self, frame, block, x, y, width, height):
        for h in range(height):
            for w in range(width):
                if block.shape[-1-h][w] != " ":
                    frame[y-h][x+w] = "."
