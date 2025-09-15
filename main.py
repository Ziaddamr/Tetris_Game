from game import Game
import time
if __name__ == "__main__":
    Game.start()
print("Game Over!!")
print(f"Your score is {Game.Score["score"]}")
time.sleep(3)
