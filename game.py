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
                x, y = 7, 4
                Flag = True
                clear()
                block = Block()
                validation.is_row_full(frame, Score, renderer)
                renderer.drawBlock(frame, block, x, y, block.w, block.h)
                renderer.drawFrame(frame, Score)
                while Flag:
                    time.sleep(0.05)
                    start = time.time()
                    while time.time() - start < 0.05:
                        if msvcrt.kbhit():
                            key = msvcrt.getch()
                            x, y, block, Flag = gameplay.movement(
                                frame, block, x, y, Score, renderer, key)

                        else:
                            x, y, block, Flag = gameplay.movement(
                                frame, block, x, y, Score, renderer,  b"")
        elif choice == b"2":
            pass
