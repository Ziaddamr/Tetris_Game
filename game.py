from renderer import Renderer
import time
import gameplay
from utilities import clear
from utilities import hide_cursor
import msvcrt
from block import Block
import validation


class Game():
    @classmethod
    def start(cls):
        clear()
        hide_cursor()
        print(
            "===========================WELCOME TO TETRIS GAME===========================")
        print("\n\n===========================Press 1 to play==================================")
        print("\n\n===========================Press 2 for leaderboard===========================")
        choice = msvcrt.getch()
        Score = dict(score=0)
        if choice == b"1":
            renderer = Renderer()
            frame = renderer.generateFrame()
            while True:
                x_coordinate, y_coordinate = renderer.WIDTH//2, renderer.HEIGHT//10
                should_continue = True
                clear()
                block = Block()
                validation.is_row_full(frame, Score, renderer)
                renderer.drawBlock(frame, block, x_coordinate, y_coordinate,
                                   block.width, block.height)
                renderer.drawFrame(frame, Score)
                while should_continue:
                    time.sleep(0.05)
                    start = time.time()
                    while time.time() - start < 0.05:
                        if msvcrt.kbhit():
                            key = msvcrt.getch()
                            x_coordinate, y_coordinate, block, should_continue = gameplay.movement(
                                frame, block, x_coordinate, y_coordinate, Score, renderer, key)

                        else:
                            x_coordinate, y_coordinate, block, should_continue = gameplay.movement(
                                frame, block, x_coordinate, y_coordinate, Score, renderer,  b"")
        elif choice == b"2":
            pass
